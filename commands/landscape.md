---
description: Technology landscape mapping for domains
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [domain]
---

# Landscape Command

Map the technology landscape for a domain (e.g., observability, vector databases).

## Workflow

1. **Parse Domain Input**
   - Identify domain/category
   - Research scope and boundaries (what belongs in this landscape)

2. **Discover Market Participants**
   - Use WebSearch to find all significant players
   - Categories: Leaders, Challengers, Niche Players, Emerging
   - Research company stage, funding, market position
   - When available: ~~financial-data (funding rounds, valuations), ~~ui-components (for web output generation)

3. **Leader Identification**
   - Highest adoption/market share
   - Proven track record and stability
   - Strong ecosystem and integrations
   - Examples: Datadog (observability), Pinecone (vector databases)

4. **Challenger Analysis**
   - Strong growth, growing adoption
   - Innovative approaches or better DX
   - Competing effectively on specific dimensions
   - May eventually displace current leaders

5. **Niche Player Mapping**
   - Specialized use cases
   - Smaller market share but loyal users
   - Unique capabilities or approaches
   - Examples: open-source projects, specialized tools

6. **Emerging Technology Tracking**
   - Pre-1.0 or recently launched tools
   - High potential for disruption
   - Monitor closely but not yet recommended for production

7. **Output Generation**
   - Landscape visualization (2D plot: Market Share vs Innovation)
   - Player directory with: name, stage, positioning, key differentiators
   - Trend analysis (consolidation, fragmentation, new entrants)
   - Switching costs and lock-in factors
   - Recommended evaluation criteria for selection

8. **Assessment and Insights**
   - Market health and trajectory
   - Risks (vendor lock-in, consolidation, abandonment)
   - Opportunity areas for new entrants
   - Technology gaps or unmet needs

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Focus on production-ready or near-production solutions
- Include open-source and commercial players
- Consider licensing and support models
- Flag companies with uncertain financial health or acquisition risk
