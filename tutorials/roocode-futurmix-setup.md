# How to Use FuturMix with Roo Code (VS Code)

> One API key, 22+ models, automatic failover — use GPT-5.4, Claude, and Gemini in Roo Code through FuturMix.

## What is FuturMix?

FuturMix is a unified AI gateway — one OpenAI-compatible endpoint for 22+ models from OpenAI, Anthropic, and Google. 20-30% cheaper than direct API pricing, with 99.99% SLA.

## Setup (2 minutes)

### Step 1: Get your FuturMix API key

1. Go to [futurmix.ai/console](https://futurmix.ai/console)
2. Create an account
3. Navigate to **API Keys** → **Create New Key**
4. Copy your key

### Step 2: Configure Roo Code

1. Open VS Code
2. Open Roo Code settings
3. Select **"OpenAI Compatible"** as the API Provider
4. Enter:
   - **Base URL**: `https://futurmix.ai/v1`
   - **API Key**: Your FuturMix key
   - **Model ID**: See model list below

### Step 3: Choose a model

| Model | Best For | Price (Input/Output per 1M tokens) |
|-------|----------|-------------------------------------|
| `gpt-5.4` | General coding | $2.50 / $15.00 |
| `gpt-5.4-mini` | Quick tasks | $0.75 / $4.50 |
| `claude-sonnet-4-5-20250929` | Complex coding | $3.00 / $15.00 |
| `claude-opus-4-7-20250424` | Hardest problems | $5.00 / $25.00 |
| `gemini-2.5-pro` | Long context | $1.25 / $10.00 |
| `gemini-2.5-flash` | Speed + cost | $0.30 / $2.50 |

Done. Roo Code now uses FuturMix for all AI requests.

## Advantages over direct API keys

- **One key** instead of managing OpenAI + Anthropic + Google keys separately
- **Switch models** by changing one string — no provider reconfiguration
- **20-30% savings** on per-token pricing
- **Failover** — if Claude is down, switch to GPT in seconds
- **No data retention** — your code stays private

## Model switching workflow

With FuturMix, you can dynamically pick the best model for each task:

- **Boilerplate / scaffolding**: `gpt-5.4-nano` ($0.20/1M input) — fast and cheap
- **Feature implementation**: `claude-sonnet-4-5-20250929` ($3.00/1M) — strong coding
- **Complex architecture**: `claude-opus-4-7-20250424` ($5.00/1M) — deepest reasoning
- **Large codebase context**: `gemini-2.5-pro` ($1.25/1M) — 1M+ token window

All through the same endpoint. Just change the model ID.

## Troubleshooting

**Auth errors**: Verify your key at futurmix.ai/console and ensure you have balance.

**Model not found**: Check exact model ID at [futurmix.ai/models](https://futurmix.ai/models).

---

*[futurmix.ai](https://futurmix.ai) — One API for 22+ AI models.*
