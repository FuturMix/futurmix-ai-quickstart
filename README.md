# FuturMix AI Quickstart

[![Try Free](https://img.shields.io/badge/Try_Free-FuturMix_API-CC6B3A?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMMiA3bDEwIDUgMTAtNS0xMC01ek0yIDE3bDEwIDUgMTAtNS0xMC01LTEwIDV6TTIgMTJsMTAgNSAxMC01LTEwLTUtMTAgNXoiIGZpbGw9IndoaXRlIi8+PC9zdmc+)](https://futurmix.ai/register?utm_source=github&utm_medium=readme&utm_campaign=badge)
[![Docs](https://img.shields.io/badge/Docs-API_Reference-blue?style=flat-square)](https://futurmix.ai/docs?utm_source=github&utm_medium=readme&utm_campaign=badge)
[![Models](https://img.shields.io/badge/Models-22%2B-green?style=flat-square)](https://futurmix.ai)
[![Discount](https://img.shields.io/badge/Save-Up_to_30%25-red?style=flat-square)](https://futurmix.ai)


Code examples for accessing 22+ AI models through one OpenAI-compatible API.

## Setup

```bash
pip install openai
```

Get your API key at [futurmix.ai](https://futurmix.ai?utm_source=github&utm_medium=repo&utm_campaign=quickstart)

## Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://futurmix.ai/v1",
    api_key="your-api-key"
)

# Claude Sonnet 4.6
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Explain quantum computing in 3 sentences"}]
)
print(response.choices[0].message.content)
```

## Node.js

```bash
npm install openai
```

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
    baseURL: 'https://futurmix.ai/v1',
    apiKey: 'your-api-key'
});

const response = await client.chat.completions.create({
    model: 'gpt-5.5',
    messages: [{ role: 'user', content: 'Write a haiku about code' }]
});

console.log(response.choices[0].message.content);
```

## cURL

```bash
curl https://futurmix.ai/v1/chat/completions \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Available Models

| Provider | Models | Discount |
|----------|--------|----------|
| **Anthropic** | Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 | 10% off |
| **OpenAI** | GPT-5.5, GPT-5.4 Pro, o3-pro | 30% off |
| **Google** | Gemini 3.1 Pro, 3 Flash | 20% off |
| **DeepSeek** | DeepSeek V3, R1 | 30% off |

Full model list: [futurmix.ai/pricing](https://futurmix.ai/pricing?utm_source=github&utm_medium=repo&utm_campaign=quickstart)

## Streaming

```python
stream = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Write a short story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

## Multi-Model Routing

Use different models for different tasks:

```python
def smart_completion(task_type, prompt):
    models = {
        "code": "claude-sonnet-4-6",
        "creative": "gpt-5.5",
        "fast": "claude-haiku-4-5",
        "reasoning": "claude-opus-4-7",
        "cheap": "deepseek-v3",
    }
    
    return client.chat.completions.create(
        model=models.get(task_type, "claude-sonnet-4-6"),
        messages=[{"role": "user", "content": prompt}]
    )

# Best model for each job
code_review = smart_completion("code", "Review this function...")
blog_post = smart_completion("creative", "Write about AI trends...")
quick_answer = smart_completion("fast", "What is 2+2?")
```

## Tool Integrations

FuturMix works with any OpenAI-compatible tool:

| Tool | Config |
|------|--------|
| **Claude Code** | `base_url: https://futurmix.ai/v1` |
| **Cursor** | Settings → Models → Custom API Base |
| **Aider** | `--openai-api-base https://futurmix.ai/v1` |
| **Continue** | `apiBase: "https://futurmix.ai/v1"` |
| **LangChain** | `ChatOpenAI(base_url="https://futurmix.ai/v1")` |
| **LlamaIndex** | `OpenAI(api_base="https://futurmix.ai/v1")` |

## Why FuturMix?

- **One API for all models** — Claude, GPT, Gemini, DeepSeek through one endpoint
- **Up to 30% cheaper** — volume-negotiated rates with providers
- **99.99% SLA** — automatic failover between providers
- **Zero data retention** — TLS 1.3, no logging, no training on your data
- **OpenAI-compatible** — change one line of code to switch

## Links

- Website: [futurmix.ai](https://futurmix.ai?utm_source=github&utm_medium=repo&utm_campaign=quickstart)
- Pricing: [futurmix.ai/pricing](https://futurmix.ai/pricing?utm_source=github&utm_medium=repo&utm_campaign=quickstart)
- Multi-Model Guide: [enterprise-ai-agent-guide](https://github.com/FuturMix/enterprise-ai-agent-guide)
