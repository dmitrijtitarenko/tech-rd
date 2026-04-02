---
description: Current trending technologies and techniques
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [domain] [timeframe]
---

# Trending Command

Identify what's trending in tech right now with flexible filtering.

## Workflow

1. **Parse Input Parameters**
   - Domain filter (optional): specific domain or "all" for broad view
   - Timeframe (optional): default 7 days, support 1d, 7d, 30d, 90d
   - Parse flexibility: "past week", "last month", "trending now" etc.

2. **Multi-Source Trend Detection**
   - GitHub Trending: Repository activity, new projects, growing interest
   - Hacker News: Discussion volume, comment engagement, ranking trajectory
   - ArXiv/Papers: New research, algorithm breakthroughs
   - Product Hunt: New launches, maker excitement
   - Twitter/Social: Community discussion spikes
   - When available: ~~source-control (GitHub trending), ~~ml-platform (model rankings), ~~ui-components (for web output generation)

3. **Trend Classification**
   - Language & Framework Trends
   - Infrastructure & DevOps Trends
   - Data & AI/ML Trends
   - Cloud & Architecture Trends
   - Developer Tool Trends
   - Emerging Pattern Trends

4. **Signal Analysis for Each Trend**
   - Velocity: How fast is adoption/discussion growing?
   - Substrate: Developer adoption vs hype (GitHub activity confirms viability)
   - Duration: Spike or sustained interest?
   - Reach: Broad or niche community?
   - Credibility: Why is this trending? (real problem or hype?)

5. **Output Structure**
   - Report date and timeframe specified
   - Executive Summary: Top 5-7 most significant trends
   - Trend Details (grouped by domain):
     - Trend name and description
     - Why it's trending (catalyst, problem it solves)
     - Current adoption level
     - Key projects/companies leading adoption
     - Hype level assessment
   - Actionable Insights: Which trends to watch vs adopt
   - Contrarian View: Overhyped trends worth skipping

6. **Assessment Framework**
   - Early Signal: Just appearing, high uncertainty
   - Gaining Momentum: Clear trajectory, growing adoption
   - Peak Hype: Maximum discussion, may or may not deliver
   - Adoption Phase: Practical use cases emerging
   - Mature: Well-established, normal technology

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Distinguish between genuine innovation and marketing hype
- Cross-reference multiple sources to confirm trends
- Consider seasonal patterns (conference releases, etc.)
- Flag technologies being oversold relative to actual maturity
