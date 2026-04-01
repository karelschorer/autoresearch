"""SSLM experiment runner (invoked via `uv run train.py`).

Runs a bounded baseline-vs-adaptive experiment using the SSLM seed model.
"""

from __future__ import annotations

import math
import os
import time
from pathlib import Path

import pyarrow.parquet as pq
import torch

from prepare import TIME_BUDGET
from sslm_seed import SSLMConfig, SSLMSeed

VOCAB_SIZE = 256
SEQ_LEN = int(os.environ.get("SEQ_LEN", "128"))
BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "16"))
EVAL_BATCHES = int(os.environ.get("EVAL_BATCHES", "32"))
TRAIN_SECONDS = int(os.environ.get("TRAIN_SECONDS", str(TIME_BUDGET)))
DEVICE_ENV = os.environ.get("DEVICE", "cpu").strip().lower()

DATA_DIR = Path.home() / ".cache" / "autoresearch" / "data"
VAL_SHARD = "shard_06542.parquet"


def resolve_device() -> torch.device:
    if DEVICE_ENV == "cuda" and torch.cuda.is_available():
        return torch.device("cuda")
    if DEVICE_ENV == "cuda":
        print("DEVICE=cuda requested but CUDA is unavailable; using CPU.")
    return torch.device("cpu")


def load_corpus_bytes() -> tuple[torch.Tensor, str]:
    if DATA_DIR.exists():
        files = sorted(p for p in DATA_DIR.glob("shard_*.parquet"))
        train_files = [p for p in files if p.name != VAL_SHARD]
        val_file = DATA_DIR / VAL_SHARD
        if train_files and val_file.exists():
            train_text = []
            for shard in train_files[:2]:
                table = pq.read_table(shard, columns=["text"])
                train_text.extend(table["text"].to_pylist()[:2000])
            val_text = pq.read_table(val_file, columns=["text"])["text"].to_pylist()[:2000]
            corpus = "\n".join(train_text + val_text).encode("utf-8", errors="ignore")
            return torch.tensor(list(corpus), dtype=torch.long), "climbmix parquet shards (byte-level)"

    fallback = Path("README.md").read_bytes()
    return torch.tensor(list(fallback * 100), dtype=torch.long), "README.md fallback corpus"


def make_batches(data: torch.Tensor, seq_len: int, batch_size: int, seed: int):
    g = torch.Generator().manual_seed(seed)
    max_start = len(data) - seq_len - 1
    while True:
        starts = torch.randint(0, max_start, (batch_size,), generator=g)
        chunk = torch.stack([data[s : s + seq_len + 1] for s in starts])
        yield chunk[:, :-1], chunk[:, 1:]


@torch.no_grad()
def eval_bpb(model: SSLMSeed, data: torch.Tensor, device: torch.device) -> float:
    model.eval()
    losses = []
    loader = make_batches(data, SEQ_LEN, BATCH_SIZE, seed=777)
    for _ in range(EVAL_BATCHES):
        x, y = next(loader)
        x, y = x.to(device), y.to(device)
        tokens = torch.cat([x, y[:, -1:]], dim=1)
        loss, _ = model(tokens)
        losses.append(loss.item())
    return (sum(losses) / len(losses)) / math.log(2)


def run_variant(name: str, adaptive: bool, train_data: torch.Tensor, val_data: torch.Tensor, budget_s: int, device: torch.device):
    cfg = SSLMConfig()
    model = SSLMSeed(cfg, use_fast_memory=adaptive).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3)
    loader = make_batches(train_data, SEQ_LEN, BATCH_SIZE, seed=42 if not adaptive else 43)

    t0 = time.time()
    steps = 0
    last_loss = 0.0
    while time.time() - t0 < budget_s:
        x, y = next(loader)
        x, y = x.to(device), y.to(device)
        tokens = torch.cat([x, y[:, -1:]], dim=1)
        loss, stats = model(tokens)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        steps += 1
        last_loss = loss.item()
        if steps % 50 == 0:
            print(f"{name} step={steps:05d} loss={loss.item():.4f} gate={stats['gate']:.4f}")

    elapsed = time.time() - t0
    val_bpb = eval_bpb(model, val_data, device=device)
    tok_s = int((steps * BATCH_SIZE * SEQ_LEN) / max(elapsed, 1e-6))
    return {
        "name": name,
        "val_bpb": val_bpb,
        "steps": steps,
        "tok_s": tok_s,
        "loss": last_loss,
        "seconds": elapsed,
        "params": sum(p.numel() for p in model.parameters()),
    }


def main():
    device = resolve_device()
    data, source = load_corpus_bytes()
    split = int(0.9 * len(data))
    train_data, val_data = data[:split], data[split:]

    print(f"device: {device}")
    print(f"training_data_source: {source}")
    print(f"training_tokens(bytes): {len(data):,}")

    half = max(TRAIN_SECONDS // 2, 60)
    baseline = run_variant("baseline_gru", False, train_data, val_data, half, device)
    adaptive = run_variant("adaptive_fastmem", True, train_data, val_data, half, device)

    better = adaptive if adaptive["val_bpb"] < baseline["val_bpb"] else baseline

    print("---")
    print(f"baseline_val_bpb: {baseline['val_bpb']:.6f}")
    print(f"adaptive_val_bpb: {adaptive['val_bpb']:.6f}")
    print(f"delta_bpb_baseline_minus_adaptive: {baseline['val_bpb'] - adaptive['val_bpb']:+.6f}")
    print("---")
    print(f"val_bpb:          {better['val_bpb']:.6f}")
    print(f"training_seconds: {baseline['seconds'] + adaptive['seconds']:.1f}")
    print(f"total_seconds:    {baseline['seconds'] + adaptive['seconds']:.1f}")
    print(f"peak_vram_mb:     {torch.cuda.max_memory_allocated() / (1024**2):.1f}" if device.type == "cuda" else "peak_vram_mb:     0.0")
    print("mfu_percent:      0.00")
    print(f"total_tokens_M:   {((baseline['steps'] + adaptive['steps']) * BATCH_SIZE * SEQ_LEN) / 1e6:.1f}")
    print(f"num_steps:        {baseline['steps'] + adaptive['steps']}")
    print(f"num_params_M:     {better['params'] / 1e6:.3f}")
    print("depth:            1")


if __name__ == "__main__":
    main()
