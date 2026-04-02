---
description: Head-to-head technology comparison
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [tech-a] vs [tech-b]
---

# Compare Command

Execute head-to-head comparison of two technologies across multiple dimensions.

## Workflow

1. **Parse Input**
   - Extract technology A and technology B names
   - Normalize names (handle version numbers, aliases)

2. **Establish Comparison Dimensions**
   - Performance (throughput, latency, resource usage)
   - Maturity & Stability (release cadence, breaking changes)
   - Community & Support (user base, forums, professional support)
   - Security & Compliance (vulnerability tracking, audit readiness)
   - Total Cost of Ownership (licensing, infrastructure, training)
   - Developer Experience (learning curve, tooling, documentation)
   - Ecosystem & Integration (libraries, plugins, third-party support)

3. **Research Phase**
   - WebSearch for benchmarks, comparisons, case studies
   - WebFetch official documentation and architecture guides
   - Find real-world implementations and performance data
   - Identify companies/projects using each technology
   - When available: ~~source-control (check if either in current stack), ~~ui-components (for web output generation)

4. **Comparative Analysis**
   - Build comparison matrix with scores (1-5 scale per dimension)
   - Document assumptions and data sources for each score
   - Flag areas where direct comparison is difficult
   - Identify use-case dependent dimensions

5. **Output Generation**
   - HTML table with visual comparison (color-coded cells)
   - Summary grid showing advantages/disadvantages
   - Head-to-head narrative for each dimension
   - Use-case based recommendation with confidence level (High/Medium/Low)
   - Migration path analysis if switching from one to other

6. **Conclusion**
   - Final recommendation with decision framework
   - When to choose Technology A vs Technology B
   - Hybrid/complementary use cases
   - Risk factors in each choice

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Use consistent, credible sources for metrics
- Acknowledge subjective assessments (DX is harder to measure)
- Consider recency of data (some benchmarks may be outdated)
- Flag conflicting information from different sources
