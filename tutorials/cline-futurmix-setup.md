# How to Use FuturMix with Cline (VS Code)

> Access 22+ AI models through one API key in Cline — GPT-5.4, Claude Opus 4.7, Gemini 3.1 Pro, and more.

## What is FuturMix?

FuturMix is a unified AI gateway that gives you access to 22+ models from OpenAI, Anthropic, and Google through a single OpenAI-compatible endpoint. It's 20-30% cheaper than calling providers directly, with 99.99% SLA and automatic failover.

## Setup (2 minutes)

### Step 1: Get your FuturMix API key

1. Go to [futurmix.ai/console](https://futurmix.ai/console)
2. Create an account (email or GitHub)
3. Navigate to **API Keys** → **Create New Key**
4. Copy your key

### Step 2: Configure Cline

1. Open VS Code
2. Open Cline settings (click the gear icon in the Cline sidebar)
3. Select **"OpenAI Compatible"** as the API Provider
4. Enter:
   - **Base URL**: `https://futurmix.ai/v1`
   - **API Key**: Your FuturMix key
   - **Model ID**: Choose from the list below

### Step 3: Pick a model

| Model | Best For | Price (Input/Output per 1M tokens) |
|-------|----------|-------------------------------------|
| `gpt-5.4` | General coding, fast | $2.50 / $15.00 |
| `gpt-5.4-mini` | Quick tasks, budget | $0.75 / $4.50 |
| `claude-sonnet-4-5-20250929` | Complex coding | $3.00 / $15.00 |
| `claude-opus-4-7-20250424` | Hardest problems | $5.00 / $25.00 |
| `gemini-2.5-pro` | Long context | $1.25 / $10.00 |
| `gemini-2.5-flash` | Speed + cost | $0.30 / $2.50 |

That's it. Cline will now route all requests through FuturMix.

## Why use FuturMix instead of direct API keys?

1. **One key for everything** — No need to manage separate OpenAI, Anthropic, and Google API keys
2. **Switch models instantly** — Change the model ID in settings, everything else stays the same
3. **20-30% cheaper** — Bulk upstream pricing passed through to you
4. **Auto failover** — If one provider goes down, your coding doesn't stop
5. **Zero data retention** — Your code is never logged or stored

## Switching models on the fly

The best part about using FuturMix with Cline: you can switch between GPT, Claude, and Gemini by just changing the model ID. No new API key, no new provider config.

```
# Quick task? Use the cheapest model
Model: gpt-5.4-nano

# Complex refactoring? Switch to the strongest
Model: claude-opus-4-7-20250424

# Need long context? Use Gemini
Model: gemini-2.5-pro
```

## Troubleshooting

**"Authentication failed"**: Make sure your API key is correct and your account has balance. Check at futurmix.ai/console.

**"Model not found"**: Double-check the model ID spelling. See the full list at [futurmix.ai/models](https://futurmix.ai/models).

**Slow responses**: Try a faster model like `gpt-5.4-mini` or `gemini-2.5-flash`.

---

*FuturMix is an OpenAI-compatible API gateway. Learn more at [futurmix.ai](https://futurmix.ai).*
