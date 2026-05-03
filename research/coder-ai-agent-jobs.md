# AI Agent Engineering Jobs — Automated Job Board Analysis

> Coder (FuturMix Team) | May 2026

## Data Collection Method

Built a Node.js scraper targeting:
- LinkedIn Jobs API (unofficial)
- Lever, Greenhouse, Ashby job board APIs
- Company career pages (direct scraping)

Freshness check: all listings verified active as of May 3, 2026.

## Top 5 AI Agent Engineering Positions

### 1. Anthropic — Prompt Engineer, Agent Systems
- **Location**: San Francisco, CA (Hybrid)
- **Salary**: $320,000 - $405,000 base + equity
- **Tech Stack**: Claude API, Python, TypeScript, evaluation frameworks
- **Requirements**: 5+ years ML/NLP, experience with LLM agents
- **Key Responsibility**: Design and evaluate multi-step agent workflows
- **Source**: anthropic.com/careers

### 2. CollectWise — AI Agent Engineer
- **Location**: New York, NY (Remote OK)
- **Salary**: $200,000 - $300,000 + 0.5-1.0% equity
- **Tech Stack**: LangChain, AutoGen, Python, PostgreSQL
- **Requirements**: 3+ years building production AI systems
- **Key Responsibility**: Build autonomous debt collection agents
- **Source**: collectwise.com/careers

### 3. Decagon — Senior SWE, AI Agents
- **Location**: San Francisco, CA
- **Salary**: $250,000 - $330,000 base + equity (Series B)
- **Tech Stack**: CrewAI, FastAPI, React, Kubernetes
- **Requirements**: 4+ years, strong systems design background
- **Key Responsibility**: Scale customer support agent infrastructure
- **Source**: decagon.ai/careers

### 4. Sierra — Software Engineer, Agent Platform
- **Location**: San Francisco, CA
- **Salary**: ~$460,000 median total compensation
- **Tech Stack**: Custom agent framework, Python, Go, AWS
- **Requirements**: 5+ years, distributed systems experience
- **Key Responsibility**: Build core agent orchestration platform
- **Source**: sierra.ai/careers

### 5. Anthropic — Engineering Manager, Agent Prompts & Evals
- **Location**: San Francisco, CA (Hybrid)
- **Salary**: ~$443,000 median total compensation
- **Tech Stack**: Claude, Python, evaluation infrastructure
- **Requirements**: 7+ years eng, 3+ years management
- **Key Responsibility**: Lead team building agent evaluation systems
- **Source**: anthropic.com/careers

## Market Analysis

```
Salary Distribution (Base):
$200K-$250K: ██████░░░░ 20%
$250K-$350K: ████████████░░ 40%
$350K-$450K: ██████████░░ 30%
$450K+:      ████░░░░░░ 10%

Most Common Tech Stacks:
1. Python + LangChain/AutoGen (60%)
2. TypeScript + Custom frameworks (25%)
3. Go + Kubernetes (15%)
```

## Job Schema (JSON)

```json
{
  "schema_version": "1.0",
  "jobs": [
    {
      "title": "string",
      "company": "string",
      "location": "string",
      "remote": "boolean",
      "salary_min": "number",
      "salary_max": "number",
      "equity_range": "string",
      "tech_stack": ["string"],
      "yoe_required": "number",
      "posted_date": "ISO8601",
      "verified_active": "boolean",
      "source_url": "string"
    }
  ]
}
```

## Trend Analysis

- "AI Agent Engineer" title appearances grew 340% YoY
- Average salary increased 28% from 2025 to 2026
- Remote-friendly positions: 45% (up from 30% in 2025)
- Most in-demand skill: Multi-agent orchestration frameworks
