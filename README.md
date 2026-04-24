# FuturMix — Enterprise-Grade AI Access for Teams of Any Size

> One API key for GPT, Claude, Gemini & Seedance. OpenAI-compatible. Automatic failover. 99.99% uptime.

FuturMix is a unified AI gateway that gives every team — from solo developers to enterprises — reliable, secure access to the world's best AI models through a single endpoint. No vendor lock-in. No downtime. No complexity.

**Why teams choose FuturMix over calling providers directly (or using OpenRouter):**

- **22 models, one API key** — GPT-5.4, Claude Opus 4.7, Gemini 3.1 Pro, Seedance 2.0, and more
- **20-30% lower cost** than OpenRouter, with transparent per-model pricing
- **99.99% SLA** with automatic failover — if one provider goes down, your app doesn't
- **Zero data retention** — we never log, store, or train on your prompts
- **OpenAI-compatible** — migrate in 2 lines of code

**Base URL:** `https://futurmix.ai/v1`

[![Models](https://img.shields.io/badge/models-22-blue)](https://futurmix.ai/models)
[![SLA](https://img.shields.io/badge/SLA-99.99%25-green)](https://futurmix.ai)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-compatible-orange)](https://futurmix.ai)

---

## Get Started in 30 Seconds

### 1. Create an account and get your API key

Sign up at [futurmix.ai/console](https://futurmix.ai/console) → API Keys → Create New Key.

### 2. Make your first request

**curl:**

```bash
curl https://futurmix.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

**Python (OpenAI SDK):**

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://futurmix.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**Node.js (OpenAI SDK):**

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://futurmix.ai/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-5.4",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(response.choices[0].message.content);
```

### 3. Switch models — no other changes needed

```python
# OpenAI
model = "gpt-5.4"

# Anthropic
model = "claude-sonnet-4-5-20250929"

# Google
model = "gemini-2.5-pro"

# Video generation
model = "doubao-seedance-2-0-260128"
```

---

## Why FuturMix?

| Problem | FuturMix Solution |
|---------|-------------------|
| Managing 4+ API keys and billing dashboards | One key, one invoice |
| App breaks when a provider has an outage | Automatic failover to next available model |
| No visibility into cost per model | Per-model latency, cost & error tracking |
| Vendor lock-in | Switch providers by changing one string |
| Overpaying for API access | 20-30% savings vs. OpenRouter |
| Data privacy concerns | Zero data retention, TLS 1.3 encryption |

---

## Migrate from OpenAI in 2 Lines

```python
# Before
client = OpenAI(api_key="sk-...")

# After — that's it
client = OpenAI(
    api_key="YOUR_FUTURMIX_KEY",
    base_url="https://futurmix.ai/v1"
)
```

All existing OpenAI SDK code works unchanged.

---

## Supported Models

| Provider | Models | Pricing (per 1M tokens) |
|----------|--------|------------------------|
| **OpenAI** | GPT-5.4, GPT-5.4 Mini, GPT-5.4 Nano | From $0.20 / $1.25 |
| **Anthropic** | Claude Opus 4.7, Opus 4.6, Sonnet 4.6, Sonnet 4.5, Haiku 4.5 | From $1.00 / $5.00 |
| **Google** | Gemini 3.1 Pro, Gemini 2.5 Pro, Gemini 2.5 Flash | From $0.10 / $0.40 |
| **ByteDance** | Seedance 2.0 (Video) | $3.00 / generation |

**Full list with pricing:** [futurmix.ai/models](https://futurmix.ai/models)

---

## Use with Your Favorite Tools

FuturMix works with any OpenAI-compatible tool or framework. It also supports the Anthropic Messages API format natively. Change one config value — nothing else.

### Cursor / Windsurf

```json
// .cursor/settings.json
{
  "openai.baseURL": "https://futurmix.ai/v1",
  "openai.apiKey": "YOUR_FUTURMIX_API_KEY",
  "openai.models": ["gpt-5.4", "claude-sonnet-4-5-20250929", "gemini-2.5-pro"]
}
```

### Claude Desktop (Cowork)

FuturMix supports the Anthropic `/v1/messages` format natively, so you can use it as a third-party inference provider in Claude Desktop:

1. Open Claude Desktop → Help → Troubleshooting → **Enable Developer Mode**
2. Go to Developer → **Configure third-party inference**
3. Set:
   - **Base URL:** `https://futurmix.ai`
   - **API Key:** Your FuturMix API key
4. Select a Claude model and start chatting

> **Note:** Use `https://futurmix.ai` (without `/v1`) as the base URL — Claude Desktop appends `/v1` automatically. Authentication uses Bearer token format.

### Cline (VS Code)

Set your API base to `https://futurmix.ai/v1` in Cline settings. Choose "OpenAI Compatible" as the provider, enter your FuturMix API key, and select any model.

### Roo Code (VS Code)

Same as Cline — set provider to "OpenAI Compatible", base URL to `https://futurmix.ai/v1`, and enter your API key.

### Aider

```bash
export OPENAI_API_KEY="YOUR_FUTURMIX_KEY"
export OPENAI_API_BASE="https://futurmix.ai/v1"
aider --model openai/claude-sonnet-4-6
```

### Anthropic SDK (Python)

```python
import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_FUTURMIX_KEY",
    base_url="https://futurmix.ai/v1"
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(message.content[0].text)
```

### LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://futurmix.ai/v1",
    model="gpt-5.4",
)
```

### LlamaIndex

```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    api_key="YOUR_API_KEY",
    api_base="https://futurmix.ai/v1",
    model="gpt-5.4"
)
```

### Terminal / CLI

```bash
export OPENAI_API_KEY="YOUR_FUTURMIX_KEY"
export OPENAI_BASE_URL="https://futurmix.ai/v1"
# Any tool that uses the OpenAI SDK now goes through FuturMix
```

---

## Examples in This Repo

| Example | Description |
|---------|-------------|
| `examples/basic_chat.py` | Simple chat completion |
| `examples/multi_model.py` | Call multiple models, compare latency & cost |
| `examples/failover_demo.py` | Manual failover pattern (GPT → Claude → Gemini) |
| `examples/streaming.py` | Streaming responses |
| `examples/model_routing.py` | Route by task type (code, writing, classification) |
| `examples/image_generation.py` | Image generation |

---

## Enterprise Features

- **99.99% SLA** with multi-region deployment (US-East, EU-West, AP-South)
- **Automatic failover** — 1,400+ degraded requests intercepted and rerouted daily
- **248ms global average latency**
- **Zero data retention** — prompts are never stored or used for training
- **TLS 1.3 encryption** on all traffic
- **Tenant isolation** with dedicated VPC for enterprise plans
- **Audit logs** for compliance

---

## Links

- [Website](https://futurmix.ai)
- [Models & Pricing](https://futurmix.ai/models)
- [Console / Sign Up](https://futurmix.ai/console)
- [API Documentation](https://futurmix.ai/v1)

---

## License

MIT
