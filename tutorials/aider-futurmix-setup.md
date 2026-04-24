# How to Use FuturMix with Aider

> Use GPT-5.4, Claude, Gemini, and 19 more models in Aider through one gateway — cheaper, with automatic failover.

## Setup (1 minute)

### Step 1: Get your FuturMix API key

Sign up at [futurmix.ai/console](https://futurmix.ai/console) and create an API key.

### Step 2: Set environment variables

```bash
export OPENAI_API_KEY="your-futurmix-key"
export OPENAI_API_BASE="https://futurmix.ai/v1"
```

Add these to your `~/.bashrc` or `~/.zshrc` to persist across sessions.

### Step 3: Launch Aider with any model

```bash
# Use GPT-5.4
aider --model openai/gpt-5.4

# Use Claude Sonnet
aider --model openai/claude-sonnet-4-5-20250929

# Use Claude Opus (strongest reasoning)
aider --model openai/claude-opus-4-7-20250424

# Use Gemini 2.5 Pro (long context)
aider --model openai/gemini-2.5-pro

# Budget mode — GPT-5.4 Nano
aider --model openai/gpt-5.4-nano
```

Note: Prefix all models with `openai/` since FuturMix uses an OpenAI-compatible endpoint.

## Available models

| Model | Price (Input/Output per 1M tokens) | Best for |
|-------|-------------------------------------|----------|
| `openai/gpt-5.4` | $2.50 / $15.00 | General coding |
| `openai/gpt-5.4-mini` | $0.75 / $4.50 | Quick edits |
| `openai/gpt-5.4-nano` | $0.20 / $1.25 | Budget tasks |
| `openai/claude-sonnet-4-5-20250929` | $3.00 / $15.00 | Complex code |
| `openai/claude-opus-4-7-20250424` | $5.00 / $25.00 | Hardest problems |
| `openai/gemini-2.5-pro` | $1.25 / $10.00 | Long context |
| `openai/gemini-2.5-flash` | $0.30 / $2.50 | Speed + cost |

Full model list: [futurmix.ai/models](https://futurmix.ai/models)

## Why FuturMix?

- **22+ models, one key** — Stop managing separate API keys for each provider
- **20-30% cheaper** — Bulk pricing from upstream providers
- **Switch models in one flag** — `--model openai/claude-opus-4-7-20250424` → `--model openai/gpt-5.4`
- **99.99% SLA** — Enterprise-grade reliability with automatic failover
- **Zero data retention** — Your code is never stored or used for training

## Tips

**Model warnings**: Aider may show "Unknown model" warnings for non-standard model names. This is expected and doesn't affect functionality.

**Streaming**: FuturMix supports streaming responses, so you'll see Aider's real-time output as usual.

**Cost tracking**: Monitor your usage at futurmix.ai/console to see per-model spending.

---

*[futurmix.ai](https://futurmix.ai) — One API for 22+ AI models.*
