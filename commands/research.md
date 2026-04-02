---
description: Deep multi-source technology research
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [topic]
---

# Research Command

Execute deep research on any technology topic across multiple sources.

## Workflow

1. **Parse Input**
   - Extract topic and detect if it's a technology, architecture pattern, or framework
   - Check for specific aspects (e.g., "React security considerations")

2. **Multi-Source Search Strategy**
   - Primary: WebSearch for recent trends, benchmarks, and community discussions
   - Secondary: WebFetch official documentation, GitHub README files, architecture guides
   - Tertiary: Search for academic papers, whitepapers, and technical reports
   - When available, use ~~research (academic papers), ~~source-control (repo analysis)

3. **Information Gathering**
   - Collect key features, use cases, maturity level, adoption patterns
   - Find performance metrics, scaling characteristics, trade-offs
   - Identify notable projects and companies using the technology
   - Research community size, ecosystem, and support availability

4. **Synthesis and Analysis**
   - Create executive summary (2-3 paragraphs)
   - Organize findings into: What It Is, Key Benefits, Limitations, When To Use, Alternatives
   - Highlight important considerations, gotchas, and best practices
   - Note recent developments and forward-looking direction

5. **Output Structure**
   - Title and metadata (date, sources)
   - Executive Summary
   - Detailed Findings (5-7 key topics)
   - Recommendations and Use Cases
   - Key Metrics and Benchmarks (if available)
   - Sources and Links
   - Related Topics for Follow-up Research

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- For very complex topics, consider spawning an agent for investigation
- Always include publication dates and source credibility assessment
- Flag contradictory findings with context
- Suggest follow-up research areas
