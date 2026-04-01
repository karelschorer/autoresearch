"""Minimal CPU-native SSLM seed baseline.

Runs short byte-level next-token experiments comparing:
1) plain GRU streaming baseline
2) GRU + surprise/learning-progress-gated fast associative memory
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass, replace
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F


VOCAB_SIZE = 256


@dataclass
class SSLMConfig:
    emb_dim: int = 128
    hidden_dim: int = 256
    fast_slots: int = 16
    ema_beta: float = 0.02
    surprise_threshold: float = 5.0


class SSLMSeed(nn.Module):
    def __init__(self, cfg: SSLMConfig, use_fast_memory: bool):
        super().__init__()
        self.cfg = cfg
        self.use_fast_memory = use_fast_memory

        self.emb = nn.Embedding(VOCAB_SIZE, cfg.emb_dim)
        self.x2h = nn.Linear(cfg.emb_dim, 3 * cfg.hidden_dim)
        self.h2h = nn.Linear(cfg.hidden_dim, 3 * cfg.hidden_dim, bias=False)
        self.out = nn.Linear(cfg.hidden_dim, VOCAB_SIZE)

        self.key = nn.Linear(cfg.hidden_dim, cfg.hidden_dim, bias=False)
        self.val = nn.Linear(cfg.hidden_dim, cfg.hidden_dim, bias=False)
        self.gate_w = nn.Parameter(torch.tensor([0.35, 0.35]))
        self.gate_b = nn.Parameter(torch.tensor(-2.0))

    def init_state(self, batch_size: int, device: torch.device):
        h = torch.zeros(batch_size, self.cfg.hidden_dim, device=device)
        mem_k = torch.zeros(batch_size, self.cfg.fast_slots, self.cfg.hidden_dim, device=device)
        mem_v = torch.zeros(batch_size, self.cfg.fast_slots, self.cfg.hidden_dim, device=device)
        mem_age = torch.zeros(batch_size, self.cfg.fast_slots, device=device)
        ema_surprise = torch.full((batch_size,), self.cfg.surprise_threshold, device=device)
        return h, mem_k, mem_v, mem_age, ema_surprise

    def gru_step(self, x_t: torch.Tensor, h: torch.Tensor) -> torch.Tensor:
        gx = self.x2h(x_t)
        gh = self.h2h(h)
        xz, xr, xn = gx.chunk(3, dim=-1)
        hz, hr, hn = gh.chunk(3, dim=-1)
        z = torch.sigmoid(xz + hz)
        r = torch.sigmoid(xr + hr)
        n = torch.tanh(xn + r * hn)
        return (1 - z) * h + z * n

    def memory_read(self, h: torch.Tensor, mem_k: torch.Tensor, mem_v: torch.Tensor) -> torch.Tensor:
        q = F.normalize(self.key(h), dim=-1)
        keys = F.normalize(mem_k, dim=-1)
        att = torch.einsum("bd,bsd->bs", q, keys)
        w = F.softmax(att * 4.0, dim=-1)
        return torch.einsum("bs,bsd->bd", w, mem_v)

    def memory_write(
        self,
        h: torch.Tensor,
        mem_k: torch.Tensor,
        mem_v: torch.Tensor,
        mem_age: torch.Tensor,
        gate: torch.Tensor,
    ):
        k_new = F.normalize(self.key(h).detach(), dim=-1)
        v_new = self.val(h).detach()

        mem_k_new = mem_k.clone()
        mem_v_new = mem_v.clone()
        mem_age_new = mem_age + 1.0
        slot = torch.argmax(mem_age_new, dim=-1)
        b = torch.arange(h.size(0), device=h.device)

        keep = (1.0 - gate).unsqueeze(-1)
        write = gate.unsqueeze(-1)
        mem_k_new[b, slot] = keep * mem_k_new[b, slot] + write * k_new
        mem_v_new[b, slot] = keep * mem_v_new[b, slot] + write * v_new
        mem_age_new[b, slot] = 0.0
        return mem_k_new, mem_v_new, mem_age_new

    def forward(self, tokens: torch.Tensor):
        bsz, seq = tokens.shape
        h, mem_k, mem_v, mem_age, ema_surprise = self.init_state(bsz, tokens.device)

        losses = []
        gate_mean = []
        surprise_mean = []

        for t in range(seq - 1):
            x_t = self.emb(tokens[:, t])
            h = self.gru_step(x_t, h)
            mem = self.memory_read(h, mem_k.detach(), mem_v.detach()) if self.use_fast_memory else torch.zeros_like(h)

            logit = self.out(h + mem)
            nll = F.cross_entropy(logit, tokens[:, t + 1], reduction="none")

            lp = (ema_surprise - nll).detach()
            ema_surprise = (1 - self.cfg.ema_beta) * ema_surprise + self.cfg.ema_beta * nll.detach()

            if self.use_fast_memory:
                gate_in = torch.stack([nll.detach(), torch.relu(lp)], dim=-1)
                gate = torch.sigmoid(gate_in @ self.gate_w + self.gate_b)
                gate = gate * (nll.detach() > self.cfg.surprise_threshold)
                with torch.no_grad():
                    mem_k, mem_v, mem_age = self.memory_write(h, mem_k, mem_v, mem_age, gate)
                gate_mean.append(gate.mean())

            losses.append(nll)
            surprise_mean.append(nll.mean())

        loss = torch.stack(losses, dim=1).mean()
        stats = {
            "surprise": torch.stack(surprise_mean).mean().item(),
            "gate": torch.stack(gate_mean).mean().item() if gate_mean else 0.0,
        }
        return loss, stats

    @torch.no_grad()
    def generate(self, prompt: bytes, steps: int, temperature: float = 1.0) -> bytes:
        self.eval()
        if len(prompt) == 0:
            prompt = b"\n"

        device = next(self.parameters()).device
        h, mem_k, mem_v, mem_age, ema_surprise = self.init_state(1, device)
        seq = list(prompt)

        for tok in seq[:-1]:
            x_t = self.emb(torch.tensor([tok], device=device))
            h = self.gru_step(x_t, h)
            if self.use_fast_memory:
                mem = self.memory_read(h, mem_k, mem_v)
                _ = self.out(h + mem)
            else:
                _ = self.out(h)

        cur = seq[-1]
        for _ in range(steps):
            x_t = self.emb(torch.tensor([cur], device=device))
            h = self.gru_step(x_t, h)
            mem = self.memory_read(h, mem_k, mem_v) if self.use_fast_memory else torch.zeros_like(h)
            logits = self.out(h + mem) / max(temperature, 1e-4)
            probs = F.softmax(logits, dim=-1)
            cur = int(torch.multinomial(probs[0], num_samples=1).item())
            seq.append(cur)

            if self.use_fast_memory:
                nll = -torch.log(probs[0, cur] + 1e-8)
                lp = (ema_surprise - nll).detach()
                ema_surprise = (1 - self.cfg.ema_beta) * ema_surprise + self.cfg.ema_beta * nll.detach()
                nll_vec = nll.detach().reshape(1)
                gate_in = torch.stack([nll_vec, torch.relu(lp)], dim=-1)
                gate = torch.sigmoid(gate_in @ self.gate_w + self.gate_b)
                gate = gate * (nll_vec > self.cfg.surprise_threshold)
                mem_k, mem_v, mem_age = self.memory_write(h, mem_k, mem_v, mem_age, gate)

        return bytes(seq)


def load_bytes() -> torch.Tensor:
    src = Path("README.md")
    data = src.read_bytes() if src.exists() else b"sslm tiny corpus\n" * 1000
    if len(data) < 20000:
        data = (data * (20000 // max(len(data), 1) + 1))[:20000]
    return torch.tensor(list(data), dtype=torch.long)


def make_batches(data: torch.Tensor, seq_len: int, batch_size: int, steps: int, seed: int):
    g = torch.Generator().manual_seed(seed)
    max_start = len(data) - seq_len - 1
    for _ in range(steps):
        starts = torch.randint(0, max_start, (batch_size,), generator=g)
        yield torch.stack([data[s : s + seq_len] for s in starts])


@torch.no_grad()
def evaluate(model: SSLMSeed, data: torch.Tensor, seed: int, seq_len: int = 128) -> float:
    model.eval()
    losses = []
    for batch in make_batches(data, seq_len=seq_len, batch_size=16, steps=20, seed=seed):
        loss, _ = model(batch)
        losses.append(loss.item())
    return (sum(losses) / len(losses)) / math.log(2)


def run_experiment(name: str, cfg: SSLMConfig, use_fast_memory: bool, train_data: torch.Tensor, val_data: torch.Tensor, train_steps: int, seed: int):
    torch.manual_seed(seed)
    model = SSLMSeed(cfg, use_fast_memory=use_fast_memory)
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3)

    t0 = time.time()
    model.train()
    for step, batch in enumerate(make_batches(train_data, seq_len=128, batch_size=16, steps=train_steps, seed=seed + 1), start=1):
        loss, stats = model(batch)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        if step % max(train_steps // 3, 1) == 0:
            print(f"{name} step={step:03d}/{train_steps} loss={loss.item():.4f} surprise={stats['surprise']:.4f} gate={stats['gate']:.4f}")

    val_bpb = evaluate(model, val_data, seed=seed + 2)
    elapsed = time.time() - t0
    tokens = train_steps * 16 * 128
    tok_s = int(tokens / elapsed)
    params = sum(p.numel() for p in model.parameters())
    print(f"{name} result: val_bpb={val_bpb:.4f} tok/s={tok_s} params={params}")
    return {"name": name, "val_bpb": val_bpb, "tok_s": tok_s, "params": params, "cfg": cfg, "model": model}


def run_suite(train_steps: int, seed: int):
    data = load_bytes()
    split = int(0.9 * len(data))
    train_data, val_data = data[:split], data[split:]

    baseline_cfg = SSLMConfig()
    baseline = run_experiment("baseline_gru", baseline_cfg, False, train_data, val_data, train_steps, seed)

    variants = [
        ("adaptive_thr5_slots16", replace(baseline_cfg, surprise_threshold=5.0, fast_slots=16)),
        ("adaptive_thr4_slots16", replace(baseline_cfg, surprise_threshold=4.0, fast_slots=16)),
        ("adaptive_thr4_slots8", replace(baseline_cfg, surprise_threshold=4.0, fast_slots=8)),
    ]

    rows = [baseline]
    for i, (name, cfg) in enumerate(variants, start=1):
        rows.append(run_experiment(name, cfg, True, train_data, val_data, train_steps, seed + i * 10))

    print("---")
    print("hypothesis: lowering surprise threshold should increase useful fast-memory updates and improve bpb")
    print("name,val_bpb,delta_vs_baseline,tok_s,params")
    for row in rows:
        delta = baseline["val_bpb"] - row["val_bpb"]
        print(f"{row['name']},{row['val_bpb']:.4f},{delta:+.4f},{row['tok_s']},{row['params']}")
    best = min(rows, key=lambda r: r["val_bpb"])
    return rows, best


def save_checkpoint(path: Path, row: dict):
    ckpt = {
        "state_dict": row["model"].state_dict(),
        "cfg": row["cfg"].__dict__,
        "use_fast_memory": row["name"] != "baseline_gru",
        "name": row["name"],
        "val_bpb": row["val_bpb"],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(ckpt, path)
    print(f"saved_checkpoint: {path}")


def load_checkpoint(path: Path) -> SSLMSeed:
    ckpt = torch.load(path, map_location="cpu")
    cfg = SSLMConfig(**ckpt["cfg"])
    model = SSLMSeed(cfg, use_fast_memory=bool(ckpt["use_fast_memory"]))
    model.load_state_dict(ckpt["state_dict"])
    model.eval()
    print(f"loaded_checkpoint: {path} name={ckpt.get('name')} val_bpb={ckpt.get('val_bpb')}")
    return model


def interactive_chat(model: SSLMSeed, gen_len: int, temperature: float):
    print("Interactive SSLM mode. Type a prompt and press enter. Ctrl-D to exit.")
    while True:
        try:
            prompt = input("prompt> ")
        except EOFError:
            print("\nbye")
            break
        out = model.generate(prompt.encode("utf-8", errors="ignore"), steps=gen_len, temperature=temperature)
        print(f"sample> {out.decode('utf-8', errors='ignore')}")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--train-steps", type=int, default=80)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--save", type=Path, default=None)
    p.add_argument("--load", type=Path, default=None)
    p.add_argument("--interactive", action="store_true")
    p.add_argument("--prompt", type=str, default="")
    p.add_argument("--gen-len", type=int, default=120)
    p.add_argument("--temperature", type=float, default=0.9)
    return p.parse_args()


def main():
    args = parse_args()
    if args.load is not None:
        model = load_checkpoint(args.load)
    else:
        _, best = run_suite(train_steps=args.train_steps, seed=args.seed)
        model = best["model"]
        print(f"best_variant: {best['name']} val_bpb={best['val_bpb']:.4f}")
        if args.save is not None:
            save_checkpoint(args.save, best)

    if args.prompt:
        out = model.generate(args.prompt.encode("utf-8", errors="ignore"), steps=args.gen_len, temperature=args.temperature)
        print(f"prompt: {args.prompt}")
        print(f"sample: {out.decode('utf-8', errors='ignore')}")

    if args.interactive:
        interactive_chat(model, gen_len=args.gen_len, temperature=args.temperature)


if __name__ == "__main__":
    main()
