# 5 Creative Uses for an Oracle Cloud ARM Server (4 cores / 24GB RAM)

**Brief:** Find non-trivial uses for an always-free Oracle Cloud ARM server (Ampere A1, 4 cores, 24 GB RAM). Excluded: personal websites, blogs, image hosting, VPNs.

---

## Use Case 1: Self-Hosted LLM Inference for Embedding Generation

**What it is:** Run small-to-mid-sized open-weight models (Llama 3.2 1B/3B, Phi-3.5 mini, BGE-M3 embeddings) for batch embedding generation, RAG indexing, or low-volume completion APIs. ARM servers running CPU inference via llama.cpp or Ollama achieve usable token rates on 7B-quantized models.

**Why this hardware fits:** 24GB RAM holds full Q4 quantized 7B models entirely in memory; 4 ARM cores via NEON SIMD give 8-15 tok/s on Llama 3.2 3B. Network egress from Oracle is generous enough for serving as a private inference endpoint to other projects without bandwidth cost concerns.

**Tool/project:** Ollama (with `OLLAMA_HOST=0.0.0.0`) + a llama-cpp-python REST shim, or LiteLLM proxy fronting it.

**Setup:**
- `curl -fsSL https://ollama.com/install.sh | sh`
- `ollama pull llama3.2:3b-instruct-q4_K_M && ollama pull bge-m3`
- Open port via Oracle ingress rules + Caddy reverse proxy with mTLS

**Resource use:** 14-22 GB RAM during inference, 75-95% CPU during requests, ~2GB RAM idle.

---

## Use Case 2: Distributed Web Crawler + Postgres Data Lake

**What it is:** Run a multi-worker Scrapy or Crawlee crawler with Playwright fallback, storing structured output in TimescaleDB (Postgres extension). Useful for price monitoring, competitive intelligence, news aggregation, or feeding a personal data warehouse.

**Why this hardware fits:** ARM cores handle parallel HTTP I/O extremely well — most crawl time is wait time, not CPU. 24GB RAM handles ~30 concurrent Playwright contexts with their headless Chromium instances. TimescaleDB chunking benefits from sustained I/O without a dedicated DB server.

**Tool/project:** Crawlee (TypeScript) + TimescaleDB + Apache Superset for visualization.

**Setup:**
- Install Docker Compose + spin up `timescale/timescaledb-ha:pg16`
- `npm create crawlee@latest`, configure 4-8 workers per crawl
- Schedule via systemd timers or Caprover cron

**Resource use:** 8-12 GB RAM (Postgres + crawler workers + browser pool), 60-80% CPU during active crawls, 30% idle (DB background work).

---

## Use Case 3: Self-Hosted CI/CD Runner Pool

**What it is:** Register the server as a self-hosted GitHub Actions runner, GitLab runner, or Buildkite agent pool. Run private builds for ARM-targeted projects, container builds, or pipelines that need persistent disk caching unavailable on hosted runners.

**Why this hardware fits:** 4 ARM cores match production ARM target architecture (AWS Graviton, Apple Silicon Linux, Raspberry Pi cluster) — builds compile and test natively without QEMU emulation overhead. 24GB RAM accommodates 3-4 parallel runner jobs with Node.js / Rust / Java toolchains loaded simultaneously.

**Tool/project:** `actions-runner` from GitHub, registered to repo or org; or `buildkite-agent`.

**Setup:**
- Download ARM64 runner binary, run config script with PAT token
- Install Buildah for rootless container builds
- Configure max parallel jobs = 3 in runner config

**Resource use:** 8-20 GB RAM during builds (varies wildly), 100% CPU bursts during compilation, ~1 GB RAM idle.

---

## Use Case 4: Always-On Mastodon / Pleroma Fediverse Instance with Custom Bots

**What it is:** Self-host a small Fediverse instance (Pleroma is lighter than Mastodon for ARM) plus custom posting bots — RSS-to-toot, weather posters, news monitors, automated digesters. Useful for community of 50-200 users or family/team private fediverse.

**Why this hardware fits:** Pleroma's BEAM (Erlang VM) runtime is famously efficient on multi-core ARM — handles 200+ active users in 4-6 GB RAM. The remaining 18 GB hosts Postgres, custom Elixir bots, and a Searxng instance for federated search. CPU usage stays below 30% with this user count.

**Tool/project:** Pleroma + Postgres 16 + custom Elixir/Python bots + Searxng for federated search aggregation.

**Setup:**
- Install dependencies: Erlang, Elixir, Postgres, ImageMagick
- `git clone pleroma; mix deps.get; mix pleroma.instance gen`
- Configure relays, federation allow-list, and reverse proxy via Caddy

**Resource use:** 4-8 GB RAM (Pleroma + Postgres + bots), 15-25% CPU avg, network-bound during federation pushes.

---

## Use Case 5: Personal Quant / Backtesting Sandbox with Time-Series DB

**What it is:** Run quantitative trading research environment — fetch financial market data via APIs, store in TimescaleDB or QuestDB, run backtests with VectorBT, walk-forward optimization, and signal monitoring. Not for live trading — for research and signal validation.

**Why this hardware fits:** 24GB RAM handles 5-10 years of minute-bar data for 100+ symbols entirely in memory during backtest vectorized runs. ARM cores execute NumPy/Pandas/Numba operations efficiently. Network egress is sufficient for downloading market data daily without cost concerns.

**Tool/project:** QuestDB + VectorBT + Jupyter Lab + Polygon.io free tier or yfinance for data ingestion.

**Setup:**
- Install QuestDB via Docker on port 9000
- `pip install vectorbt jupyterlab pandas-ta`
- Schedule data pulls via APScheduler, persist to QuestDB

**Resource use:** 6-15 GB RAM during backtests (peaks higher for full universe runs), 100% CPU during vectorized runs, 2 GB RAM idle.

---

## Top Pick (Spec Fit + Practical Value): Use Case 3 — Self-Hosted CI/CD Runner Pool

**Why ranked #1:**
- **Spec fit (10/10):** ARM cores directly match the increasingly common ARM production target. Native ARM builds eliminate QEMU emulation that hosted x86 runners need (which is 10-50x slower for compilation tasks).
- **Practical value (9/10):** GitHub Actions hosted runners cost $0.008/minute over the free tier. A typical small dev team easily burns through the free tier. A self-hosted ARM runner saves $10-50/month for active projects while providing faster builds.
- **Setup effort (8/10):** Single binary deployment + service registration. Approximately 30 minutes from blank server to first build.
- **Lock-in risk (10/10):** None. Pure GitHub/GitLab integration via documented APIs. Move workload anywhere instantly.

The combination of (a) a directly relevant production architecture, (b) measurable cost savings, and (c) genuinely faster builds makes this the most defensible use case among the five.
