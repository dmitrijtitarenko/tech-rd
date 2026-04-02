---
description: Patent landscape analysis for technologies
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [technology]
---

# Patent Scan Command

Analyze patent landscape for a technology area.

## Workflow

1. **Parse Technology Input**
   - Identify technology/technique to research
   - Define scope: core technology vs related techniques
   - Determine geographic focus (US, EU, global)

2. **Patent Database Search**
   - Search USPTO (United States Patent Office) database via WebSearch
   - Research Google Patents for broader coverage
   - Identify key patents in the technology area
   - Look for patent families (related patents across jurisdictions)

3. **Key Patent Identification**
   - Find foundational/seminal patents (high citations)
   - Identify recent patent filings
   - Look for patents held by major tech companies
   - Research patent pools and cross-licensing agreements

4. **Patent Landscape Mapping**
   - Identify major patent holders by company
   - Categorize patents by:
     - Core technology patents (essential)
     - Implementation patents (specific methods)
     - Application patents (use cases)
   - Track patent filing trends over time
   - Identify white space (unpatented areas)

5. **Patent Analysis**
   - Review claims to understand protection scope
   - Assess claim breadth: narrow vs broad coverage
   - Check expiration dates (patent lifetime ~20 years)
   - Research invalidation challenges or litigation
   - Evaluate prior art and novelty

6. **Freedom to Operate Assessment**
   - Identify patents that could block implementation
   - Assess licensing availability and terms
   - Check for defensive patent portfolios
   - Research patent litigation history
   - Evaluate workaround feasibility

7. **Competitive Intelligence**
   - Which companies are patenting in this space?
   - Patent filing intensity by player
   - Strategic focus of patent filings
   - Patent licensing deals and cross-licenses
   - Acquisitions for patent portfolios

8. **Output: Patent Landscape Report**
   - Executive Summary: Patent landscape overview and risks
   - Landscape Timeline: Patent filing trends 2015-present
   - Key Patents Table:
     - Patent number/title
     - Assignee/Holder
     - Filing date and expiration
     - Claims summary
     - Citation count
   - Major Patent Holders: Companies with significant portfolios
   - Freedom to Operate Assessment:
     - High Risk: Patents that directly block implementation
     - Medium Risk: Patents with potential claims conflict
     - Low Risk: Patents with narrow scope
   - Licensing Landscape: Available licenses and terms
   - Strategic Recommendations: How to navigate patent landscape

9. **Risk Assessment**
   - Patent Risk Level: High/Medium/Low
   - Litigation History: Any notable cases?
   - Defensive Patent Strategies: How industry approaches this
   - Design Around Feasibility: Can implementation avoid patents?
   - Licensing Cost Impact: Typical royalty rates

10. **Special Considerations**
    - Software patents vs hardware patents implications
    - Open source implications (patent trolls, GPL)
    - Standards-essential patents (FRAND licensing)
    - Emerging patent pools and consortia

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Focus on currently enforceable patents (check expiration)
- Consider jurisdiction differences (patent validity varies)
- Flag litigation-prone areas with heavy patent activity
- Recommend professional patent counsel for legal risk assessment
- Track patent landscape evolution over time
