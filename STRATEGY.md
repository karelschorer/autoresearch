# Building a Databricks competitor — strategy & technical roadmap

> Living strategy doc. Grounded in the 2026 landscape, not vibes. The point of
> M0 (the `photon/` autoresearch loop) was to learn the discipline we apply
> here: **understand the problem before building; the obvious move is often
> already done for you.** That lesson applies at the company scale too.

## 1. What Databricks actually is

Not one product — a stack. You can't "rebuild Databricks"; you pick a layer.

| Layer | What it is | Open-source equivalents |
|---|---|---|
| **Platform / control plane** | multi-cloud SaaS, notebooks, collaboration, billing | — (this is the business, not the tech) |
| **Governance** | Unity Catalog: metadata, lineage, access control | Apache Polaris, Nessie, Lakekeeper |
| **Orchestration** | Workflows, Delta Live Tables (declarative ETL) | Airflow, Dagster, dbt |
| **SQL / optimizer** | Databricks SQL, Catalyst planner | Calcite, DataFusion planner |
| **Execution engine** | **Photon** (C++ vectorized), Spark (JVM) | **Velox, DataFusion, DuckDB, ClickHouse** |
| **Table format** | Delta Lake (+ now Iceberg) | Apache Iceberg, Hudi, Delta (all OSS) |
| **Storage** | object storage (S3/ADLS/GCS) | — (commodity) |

## 2. The honest 2026 landscape (this is the key finding)

**The execution-engine layer is commoditized.** The thing that took Databricks
years to build (Photon) now has multiple mature open-source equivalents:

- **Apache DataFusion** (Rust, Arrow-native) is now the *fastest single-node
  Parquet engine* — beating DuckDB and ClickHouse — and is the default
  substrate teams build new data systems on top of.
- **Velox** (C++, Meta) is Photon's open twin; Meta/IBM/Intel back it.
- **DuckDB** owns embedded/single-node analytics.

**The table format war is over — Iceberg won the neutrality fight.** Databricks
bought Tabular (the Iceberg company) in 2024 and added native Iceberg to Unity
Catalog; Snowflake, AWS, Google all back Iceberg. Format is now a *standard*,
not a moat.

**Implication:** Re-building "another Spark + another Photon + another Delta"
is a multi-hundred-million-dollar effort to ship a *commodity*. That is the
losing move. The hard part is no longer the engine.

Sources at the bottom.

## 3. So where is the actual wedge?

The moat is no longer "go faster." It is one of:

1. **Self-optimizing execution** — an engine that profiles its own workloads
   and recompiles/retunes hot paths automatically. This is *our* DNA: the
   `photon/autoresearch/` loop is a toy version of exactly this. Nobody ships a
   truly self-tuning lakehouse engine today. **This is our differentiator.**
2. **Radical cost** — same open formats (Iceberg/Parquet), a fraction of the
   $/query, by being leaner than JVM-Spark. (DuckDB/DataFusion already attack
   this single-node; the gap is *distributed*.)
3. **Single-node → distributed continuum** — start as a fast local engine
   (DuckDB-class), scale the *same* engine to a cluster without a rewrite. The
   "Snowflake-simple but open and cheap" pitch.
4. **AI-native** — the data platform an agent drives, not a human. Natural-
   language → plan → execute, with the engine optimizing for agent access
   patterns.

## 4. Recommended strategy: **stand on OSS, differentiate with self-optimization**

Do **not** rebuild the engine from scratch in C++. That reinvents
DataFusion/Velox and burns our whole runway on a commodity.

Instead:

- **Substrate:** build *on* Apache DataFusion (Rust, Arrow, trait-extensible,
  Substrait plan interchange). We inherit a world-class vectorized engine,
  Parquet/Iceberg readers, and a SQL planner for free.
- **Moat:** a **self-optimizing layer** — the productionized descendant of the
  autoresearch loop. It watches real query plans, identifies hot operators,
  and swaps in specialized/recompiled kernels (and tuning knobs like vector
  width, which M0 proved is worth ~8% for one flag) per workload, with a
  correctness gate so it can never ship a wrong answer.
- **Wedge:** open formats (Iceberg-first), single-node-to-distributed, sold on
  $/query and "it tunes itself."

What M0 already proved we can do, in miniature: hold a fixed correctness gate,
generate candidate implementations, measure honestly, and let data (not
intuition) pick the winner — *including the discipline to reject our own
rewrites when the compiler already won.* That governance is the seed of the
self-optimizing engine.

## 5. Technical roadmap (concrete, runnable increments)

- **M0 — done.** Vectorized kernel + autoresearch loop + honest benchmarking
  discipline (`photon/`).
- **M1 — columnar core.** Adopt Arrow as the in-memory batch format; build a
  tiny operator framework (scan → filter → project → aggregate) over Arrow
  batches, with our kernels pluggable. *Decision point: from-scratch vs.
  embed DataFusion.*
- **M2 — query frontend.** SQL → logical plan → physical plan (or use
  DataFusion's planner). One end-to-end `SELECT ... WHERE ... GROUP BY`.
- **M3 — open table format.** Read Parquet, then an Iceberg table (snapshot +
  manifest). This is table-stakes for "lakehouse."
- **M4 — self-optimizing layer.** Wire the autoresearch loop into the running
  engine: per-operator candidate kernels, runtime profiling, gated hot-swap.
  *This is the product.*
- **M5 — distribution.** Shard scan/exchange across workers. Only once
  single-node is compelling.

## 6. Recommendation in one line

**Be the self-optimizing, open-format lakehouse engine: build on DataFusion,
make the autoresearch loop the product, start single-node on Iceberg, win on
$/query and "it tunes itself" — not on rebuilding Photon.**

---

### Sources
- DataFusion fastest single-node Parquet engine; default substrate for new
  platforms; Substrait federation with Velox/DuckDB —
  https://datalakehousehub.com/blog/2026-05-composable-query-engines/ ,
  https://www.tinybird.co/blog/best-database-for-olap
- Photon architecture (C++ vectorized engine accelerating Spark SQL) —
  https://docs.databricks.com/aws/en/compute/photon ,
  https://www.databricks.com/product/photon
- Iceberg now native in Unity Catalog; format convergence —
  https://www.sigmoid.com/ebooks-whitepapers/choosing-between-delta-lake-and-apache-iceberg-in-databricks-for-modern-data-platforms/ ,
  https://www.capitalone.com/software/blog/databricks-top-features-announced-data-engineers-2025/
