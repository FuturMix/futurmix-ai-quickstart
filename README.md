# FuturMix Quickstart

> One API key. GPT, Claude, Gemini & Seedance. Automatic failover.

FuturMix is a unified AI gateway that lets you call multiple AI providers through a single OpenAI-compatible endpoint. Switch models with one line of code. Never worry about a single provider going down.

**Base URL:** `https://futurmix.ai/v1`

---

## Get started in 30 seconds

### 1. Create an account and get your API key

Sign up at [futurmix.ai/console](https://futurmix.ai/console) → API Keys → Create New Key.

### 2. Make your first request

**curl:**
```bash
curl https://futurmix.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
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
    model="gpt-4o",
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
  model: "gpt-4o",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(response.choices[0].message.content);
```

### 3. Switch models — no other changes needed

```python
# GPT
model="gpt-4o"

# Claude
model="claude-3-5-sonnet-20240620"

# Gemini
model="gemini-2.0-flash"

# Image generation
model="gpt-image-1"
```

---

## Why FuturMix?

| Problem | FuturMix |
|---|---|
| Managing 4+ API keys and billing dashboards | One key, one invoice |
| App breaks when OpenAI has an outage | Automatic failover to next available model |
| No visibility into cost per model | Per-model latency, cost & error tracking |
| Vendor lock-in | Switch providers by changing `model` string |

---

## Migrate from OpenAI in 2 lines

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

| Provider | Models |
|---|---|
| OpenAI | gpt-4o, gpt-4o-mini, gpt-image-1, and more |
| Anthropic | claude-3-5-sonnet, claude-3-haiku, and more |
| Google | gemini-2.0-flash, gemini-1.5-pro, and more |
| Seedance | Video generation models |

Full list: [futurmix.ai/models](https://futurmix.ai/models)

---

## Examples in this repo

- [`examples/basic_chat.py`](examples/basic_chat.py) — Simple chat completion
- [`examples/multi_model.py`](examples/multi_model.py) — Call multiple models and compare latency/cost
- [`examples/failover_demo.py`](examples/failover_demo.py) — Manual failover pattern (gpt-4o → claude → gemini)
- [`examples/streaming.py`](examples/streaming.py) — Streaming responses
- [`examples/model_routing.py`](examples/model_routing.py) — Route by task type (code, writing, classification)
- [`examples/image_generation.py`](examples/image_generation.py) — Image generation with gpt-image-1

---

## Framework compatibility

FuturMix works with any OpenAI-compatible library. Change one config value — nothing else.

**LangChain:**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://futurmix.ai/v1",
    model="gpt-4o",
)
```

**LlamaIndex:**
```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    api_key="YOUR_API_KEY",
    api_base="https://futurmix.ai/v1",
    model="gpt-4o",
)
```

---

## Pricing

Pay-as-you-go via Stripe. Enterprise contracts available.
→ [futurmix.ai/pricing](https://futurmix.ai/pricing)

---

## Links

- Website: [futurmix.ai](https://futurmix.ai)
- Console: [futurmix.ai/console](https://futurmix.ai/console)
- Docs: [futurmix.ai/docs](https://futurmix.ai/docs)
- Models & pricing: [futurmix.ai/models](https://futurmix.ai/models)
