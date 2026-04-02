# tech-rd

[![CI](https://github.com/dtytarenko/tech-rd/actions/workflows/ci.yml/badge.svg)](https://github.com/dtytarenko/tech-rd/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests: 137 passed](https://img.shields.io/badge/tests-137%20passed-brightgreen.svg)]()
[![Skills: 37](https://img.shields.io/badge/skills-37-blueviolet.svg)]()
[![MCP Servers: 18](https://img.shields.io/badge/MCP%20servers-18-orange.svg)]()

Full-spectrum technology R&D intelligence for Claude. Research technologies, generate tech radars, analyze competitive landscapes, and make data-driven technology decisions with structured intelligence across 37 skills, 12 commands, 5 specialist agents, and 18 MCP integrations.

## Overview

tech-rd is a comprehensive research and intelligence platform for exploring any technology domain, from classical software engineering to frontier technologies. It combines 37 specialized skills, 12 research commands, a 5-agent orchestration system, and 18 MCP integrations to deliver computed, evidence-backed technology intelligence at scale.

Every research output involves real computation. When there is a number to calculate, Claude calculates it: TCO models in Python, scaling simulations with real data, statistical comparisons with confidence intervals, and formula derivations in LaTeX. Research outputs are structured scientific documents, not web summaries.

The plugin delivers results in three formats: scientific Markdown (default), IEEE Academic LaTeX/PDF (formal deliverables with proper typesetting), and interactive web dashboards (React + shadcn with sortable tables, Recharts visualizations, and tabbed navigation). Users choose their format per request.

tech-rd supports technology assessment across 31 domain verticals and 6 cross-functional capabilities including diagram generation, interactive brainstorming, scheduling, Notion knowledge base integration, and data export. It covers AI/ML, cloud infrastructure, cybersecurity, compliance, blockchain, quantum computing, fintech, biotech, military/government tech, and more.

The plugin is designed for technology leaders, engineers, architects, product managers, and research teams who need defensible, evidence-backed intelligence on the technology landscape. It produces professional deliverables in nine standardized output formats suitable for technical reviews, executive briefings, and strategic planning.

## Installation

### Option 1: Claude Code CLI

```bash
claude plugin add github:dtytarenko/tech-rd
```

### Option 2: Cowork Plugin Manager

Download the `.plugin` file from the [Releases](https://github.com/dtytarenko/tech-rd/releases) page and import via Cowork.

### Option 3: Manual Installation

```bash
git clone https://github.com/dtytarenko/tech-rd.git
cd tech-rd
claude plugin install ./tech-rd
```

## Commands

The following 12 commands provide entry points for different types of technology research:

| Command | Purpose | Example Input |
|---------|---------|--------------|
| /research | Deep multi-source investigation of any technology | `/research GraphQL for real-time APIs` |
| /tech-radar | Generate ThoughtWorks-style tech radar | `/tech-radar data engineering` |
| /compare | Head-to-head comparison of two technologies | `/compare PostgreSQL vs MongoDB` |
| /landscape | Market overview and competitive positioning | `/landscape observability platforms 2026` |
| /trending | Analyze adoption trends and market signals | `/trending machine learning frameworks` |
| /oss-audit | Audit open-source project health and risk | `/oss-audit dependencies in package.json` |
| /tech-dd | Technology due diligence for acquisition targets | `/tech-dd target-company cloud stack` |
| /standards | Track evolving technical standards and compliance | `/standards GDPR enforcement for SaaS` |
| /patent-scan | Search patent landscape for technology domains | `/patent-scan quantum error correction` |
| /stack-detect | Analyze and profile existing technology stacks | `/stack-detect our infrastructure` |
| /build-vs-buy | Evaluate custom development vs commercial solutions | `/build-vs-buy time-series database` |
| /migration | Plan technology migrations and modernization | `/migration legacy monolith to microservices` |

## Skills

The plugin includes 37 specialized skills organized into five categories:

### Core Engineering

| Skill | Domain Coverage |
|-------|-----------------|
| software-engineering | Design patterns, architecture, best practices |
| ai-ml-research | Machine learning, deep learning, model evaluation |
| cloud-infrastructure | Cloud platforms, infrastructure as code, deployment |
| data-engineering | Data pipelines, warehousing, streaming, lakes |
| devops-sre | Operations, observability, incident response |

### Security & Compliance

| Skill | Domain Coverage |
|-------|-----------------|
| cybersecurity | Threat modeling, vulnerability assessment, defense |
| regtech-compliance | Regulatory frameworks, audit, controls |

### Frontier Technologies

| Skill | Domain Coverage |
|-------|-----------------|
| graphics-3d-xr | Graphics engines, 3D rendering, immersive tech |
| hardware-iot-robotics | Embedded systems, IoT platforms, robotics |
| blockchain-web3 | Distributed ledger, smart contracts, Web3 |
| quantum-computing | Quantum algorithms, hardware, simulators |

### Vertical Markets

| Skill | Domain Coverage |
|-------|-----------------|
| miltech-govtech | Military tech, government systems, defense |
| edtech | Educational technology and learning platforms |
| fintech | Financial technology, payments, trading |
| biotech-healthtech | Life sciences, medical devices, health platforms |

### Cross-Cutting & New Domains

| Skill | Domain Coverage |
|-------|-----------------|
| database-technologies | SQL, NoSQL, graph, time-series, search |
| networking-telecom | Networks, protocols, 5G, infrastructure |
| programming-languages | Language design, type systems, runtimes |
| lowcode-nocode | Low-code platforms, automation, citizen dev |
| api-ecosystem | API design, REST, GraphQL, gRPC |
| observability | Monitoring, logging, tracing, alerting |
| tech-radar | Quadrant mapping, adoption curves |
| competitive-intelligence | Market analysis, positioning, vendor tracking |
| oss-intelligence | Open-source health, licensing, ecosystem |
| tech-due-diligence | Acquisition analysis, vendor evaluation |
| standards-tracker | Standards bodies, compliance tracking |
| patent-landscape | Patent analysis, IP strategy |
| tech-trend-synthesis | Market trends, adoption patterns |
| architecture-patterns | Architectural styles, design principles |
| cost-optimization | TCO analysis, pricing models |
| developer-experience | Tooling, documentation, community |

### Capabilities

| Skill | Purpose |
|-------|---------|
| diagram-generation | Publication-quality diagrams in Mermaid, D2, TikZ, or FigJam MCP |
| interactive-brainstorming | Assess-then-adapt discovery workflow with HTML intake forms |
| scheduling | Automated monitoring: watchlist, triggers, and digest modes |
| notion-knowledge-base | Optional per-user Notion workspace for research storage |
| data-export | JSON/CSV export compatible with ThoughtWorks radar and dashboards |
| output-formats | Nine professional templates plus scientific style guide |

### Output System

All research outputs support three delivery formats:

| Format | Description |
|--------|------------|
| Markdown | Scientific structured document with inline LaTeX math, Mermaid diagrams, numbered citations |
| LaTeX/PDF | IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation |
| Interactive Web | React + shadcn dashboard with Recharts charts, sortable tables, tabbed navigation |

Nine professional deliverable templates: Tech Radar, Comparison Matrix, SWOT Analysis, Decision Matrix, Deep Research Report, Scorecard, Executive Brief, Risk Heat Map, Adoption Curve.

## Agents

The plugin coordinates five specialized agents in an orchestrated research pipeline:

| Agent | Model | Role | Invoked For |
|-------|-------|------|------------|
| research-director | Opus | Orchestration, planning, synthesis | Primary entry point for all requests |
| tech-scout | Sonnet | Breadth scanning, discovery | Landscape and trend analysis |
| trend-analyst | Sonnet | Pattern recognition, adoption curves | Market signals and adoption timing |
| deep-researcher | Opus | Comprehensive investigation | Complex technical deep dives |
| evidence-validator | Opus | Cross-source verification, fact-checking | Validating findings and confidence |

The agents operate in a 7-stage pipeline: Classify, Plan (visible to user), Gather (parallel), Analyze, Validate, Synthesize, Deliver. The Research Director receives the user query, classifies the request, creates a visible research plan, delegates to specialist agents in parallel, validates findings through the Evidence Validator, and synthesizes a unified deliverable. All numeric claims are computed with Python, not estimated.

## MCP Integrations

The plugin comes pre-configured with 18 MCP servers spanning research, project management, cloud platforms, analytics, and design:

### Bundled MCP Servers

| Server | Purpose |
|--------|---------|
| GitHub | Source control, repository analysis, code patterns |
| Slack | Team communication, documentation, context |
| Notion | Knowledge base, research notes, team wiki |
| Linear | Project tracking, issue management, roadmaps |
| Atlassian | Jira integration, enterprise project tracking |
| Hugging Face | ML model registry, datasets, papers |
| Consensus | Academic research, peer-reviewed papers |
| Tavily | Web search, news, trending content |
| bioRxiv | Biomedical preprints, life sciences research |
| FactSet | Financial data, company intelligence, market data |
| PostHog | Product analytics, user behavior, feature tracking |
| AWS Marketplace | Cloud services catalog, pricing, vendor solutions |
| Cloudflare | CDN, security, performance data |
| Quartr | Earnings data, financial metrics, company analysis |
| PagerDuty | Incident tracking, SRE metrics, reliability data |
| Datadog | Infrastructure monitoring, observability, performance |
| Figma | FigJam diagrams, design system context, collaborative visuals |
| shadcn | UI component library, design system reference, component patterns |

### Tool-Agnostic Connectors

The plugin also supports category-based connectors for flexibility. Teams can substitute the bundled servers with alternatives in the same category:

| Category | Bundled | Alternatives |
|----------|---------|--------------|
| Source control | GitHub | GitLab, Bitbucket |
| Chat | Slack | Microsoft Teams, Discord |
| Project tracker | Linear, Atlassian | Asana, ClickUp, Shortcut |
| Knowledge base | Notion | Confluence, Guru, Coda |
| AI/ML platform | Hugging Face | Weights & Biases, MLflow |
| Academic research | Consensus, bioRxiv | Semantic Scholar, PubMed |
| Web research | Tavily | Perplexity, Exa |
| Cloud provider | AWS, Cloudflare | GCP, Azure |
| Monitoring | Datadog, PagerDuty | New Relic, Grafana, Splunk |
| Financial data | FactSet, Quartr | Bloomberg, PitchBook |
| Product analytics | PostHog | Amplitude, Mixpanel |
| Design system | shadcn, Figma | Storybook, Zeroheight |

See CONNECTORS.md for configuration details.

## Output Formats

The plugin can structure findings into nine professional formats, each designed for specific audiences and use cases:

| Format | Best For | Typical Audience |
|--------|----------|-----------------|
| Tech Radar | Technology adoption strategy and portfolio decisions | Technical teams, engineering leadership |
| Comparison Matrix | Choosing between 2-4 specific options | Engineers, architects, procurement |
| SWOT Analysis | Strategic positioning and market assessment | Product, strategy, executive teams |
| Decision Matrix | Weighted evaluation across multiple criteria | Leadership, steering committees |
| Deep Research Report | Comprehensive 3000+ word investigations | R&D, technical deep dives, board review |
| Scorecard | Health assessment of a technology or vendor | Operations, vendor management |
| Executive Brief | One-page summary for decision-makers | C-level, investors, board |
| Risk Heat Map | Identifying and prioritizing adoption risks | Risk management, compliance, security |
| Adoption Curve | Understanding market maturity and adoption lifecycle | Product, strategy, competitive intel |

## Architecture

The research pipeline operates across seven distinct stages, each contributing to the final deliverable:

**Classify**: The Research Director parses the incoming user query, detecting the research domain, required depth, comparison dimensions (if applicable), and appropriate specialist agents to invoke.

**Plan**: Based on classification, the system creates and displays a visible research plan showing which domains will be covered, which agents will work in parallel, which data sources will be queried, and the expected timeline and output format.

**Gather**: Specialist agents (Tech Scout for breadth, Deep Researcher for depth, Trend Analyst for signals) execute concurrent research using MCP integrations to query GitHub, Consensus, Tavily, financial data sources, and other relevant platforms. Raw data and evidence are collected systematically.

**Analyze**: The gathered evidence is synthesized into structured findings. Agents organize information by theme, identify patterns, build comparison matrices, and assess relative maturity and adoption. This phase bridges raw data to actionable intelligence.

**Validate**: The Evidence Validator cross-references findings across multiple sources, flags contradictions with context, assesses confidence levels, and identifies areas where more research is needed. This ensures defensible, high-confidence deliverables.

**Synthesize**: The Research Director aggregates findings from all agents, resolves conflicts, identifies themes, and structures results into the requested output format. This produces a unified, coherent narrative suitable for the target audience.

**Deliver**: The final deliverable is presented in the chosen format (tech radar, comparison matrix, executive brief, etc.), with sources cited, confidence levels noted, and next steps recommended.

## Configuration

### MCP Server Setup

All 18 bundled MCP servers are pre-configured in `.mcp.json`. To customize:

1. Edit `.mcp.json` to add, remove, or replace servers
2. Use category-based placeholders (e.g., `~~source control`, `~~financial data`) to make skills tool-agnostic
3. Provide credentials and authentication tokens via environment variables (see your MCP server documentation)

### Environment Variables

Optional configuration:

- `RESEARCH_DEPTH`: Set default research depth (quick, standard, deep)
- `CONFIDENCE_THRESHOLD`: Minimum confidence level for findings to be included
- `OUTPUT_FORMAT`: Default deliverable format (tech-radar, comparison-matrix, etc.)

### Optional Connectors

To add additional MCP servers beyond the bundled set:

1. Verify the MCP server is compatible with Claude
2. Add the server definition to `.mcp.json`
3. Update skill files to reference the new server
4. Test with `/research` or `/tech-radar` commands

See individual skill files in `/skills/` for specific server dependencies.

## Contributing

Contributions are welcome. The plugin follows a modular structure:

- Commands: `/commands/` — each command is a single workflow file
- Skills: `/skills/` — each skill folder contains a SKILL.md file with domain knowledge
- Agents: `/agents/` — agent definitions and orchestration logic
- Output templates: `/skills/output-formats/references/` — deliverable templates

To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-domain`)
3. Add or modify skills, commands, or agents in their respective directories
4. Test with Claude Code CLI
5. Submit a pull request with a clear description

For new skills, include:

- Domain coverage (what topics does this skill address)
- Key triggers (when should this skill be invoked)
- Key sources and data providers
- Output templates or formats

## License

MIT License. See LICENSE for details.

---

For issues, feature requests, or questions, open an issue on GitHub at https://github.com/dtytarenko/tech-rd
