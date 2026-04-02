---
description: ThoughtWorks-style tech radar generation
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [domain]
---

# Tech Radar Command

Generate a ThoughtWorks-style technology radar for any domain.

## Workflow

1. **Parse Domain Input**
   - Identify domain (e.g., "data engineering", "frontend", "cloud infrastructure")
   - Default to general tech if no domain specified

2. **Establish Quadrants**
   - Languages & Frameworks
   - Tools & Platforms
   - Infrastructure & Architecture
   - Techniques & Methodologies

3. **Research and Populate Entries**
   - Use WebSearch for current technology landscape
   - For each technology, research:
     - Maturity and adoption level
     - Community size and momentum
     - Production readiness
     - Integration with adjacent tools
   - When available: ~~source-control (detect current stack), ~~analytics (usage data)

4. **Classify in Rings**
   - **Adopt**: Proven, widely used, recommend confidently
   - **Trial**: Promising, worth investing time, early adopters using successfully
   - **Assess**: Interesting, not yet proven, monitor closely
   - **Hold**: Avoid or deprecate, not recommended for new projects

5. **Generate Output**
   - Create SVG/HTML visualization (radial diagram)
   - Add quadrants and rings with technology names
   - Include brief justification for ring placement
   - Generate markdown summary with rationale for key placements
   - Note technologies moving between rings from last period

6. **Documentation**
   - Timeline (generation date)
   - Domain focus
   - Key changes from previous version (if applicable)
   - Legend explaining rings and quadrants

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Bias towards practical, battle-tested technologies
- Consider team skill availability and market trends
- Flag technologies with license implications
- Highlight ecosystem health and maintenance status
