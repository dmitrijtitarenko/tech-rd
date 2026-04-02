# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-02

### Added

- Initial release of tech-rd plugin
- 37 specialized skills covering 31 domain verticals and 6 cross-functional capabilities
- 12 research commands: /research, /tech-radar, /compare, /landscape, /trending, /oss-audit, /tech-dd, /standards, /patent-scan, /stack-detect, /build-vs-buy, /migration
- 5-agent orchestration system: Research Director, Tech Scout, Trend Analyst, Deep Researcher, Evidence Validator
- 7-stage research pipeline: Classify, Plan, Gather, Analyze, Validate, Synthesize, Deliver
- 18 pre-configured MCP servers: GitHub, Slack, Notion, Linear, Atlassian, Hugging Face, Consensus, Tavily, bioRxiv, FactSet, PostHog, AWS Marketplace, Cloudflare, Quartr, PagerDuty, Datadog, Figma, shadcn
- Tool-agnostic connector system with 12 connector categories (see CONNECTORS.md)
- 9 professional output templates: Tech Radar, Comparison Matrix, SWOT Analysis, Decision Matrix, Deep Research Report, Scorecard, Executive Brief, Risk Heat Map, Adoption Curve
- Three-tier delivery system: Markdown (scientific), LaTeX/PDF (IEEE Academic), Interactive Web (React + shadcn)
- 8 Python analysis scripts: TCO calculator, benchmark comparison, trend analyzer, scoring model, risk scorer, market share estimator, scaling simulator, radar generator
- Scientific style guide for consistent output quality
- 117 automated tests covering structure, MCP config, content quality, and script validation
- MIT License
