---
description: Technical due diligence for companies
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [company or product]
---

# Tech DD Command

Technical due diligence report for companies or products.

## Workflow

1. **Target Identification**
   - Identify company/product
   - Gather basic information: founding, stage, funding, industry
   - Determine scope: entire company or specific product

2. **Stack Analysis**
   - Detect frontend technology (framework, build tools, static analysis)
   - Identify backend language(s) and framework(s)
   - Research infrastructure: cloud provider, containerization, orchestration
   - Use BuiltWith-style signals: IP addresses, DNS records, headers
   - When available: ~~web-research (deep crawl), ~~source-control (repo analysis), ~~ui-components (for web output generation)
   - Review public GitHub repositories if available

3. **Engineering Team Assessment**
   - Research team size and growth trajectory
   - Analyze job postings for skill requirements and gaps
   - Check LinkedIn profiles of engineering leadership
   - Assess team experience: depth in relevant domains
   - Flag high turnover or departures of key people

4. **Technical Debt Signal Detection**
   - Search for technology postmortems or incident reports
   - Analyze technical blog for architectural challenges
   - Check if they're maintaining legacy systems
   - Look for frequent technology rewrites or migrations
   - Assess code quality signals (if repos public)

5. **Scalability & Performance**
   - Research infrastructure scale: data centers, regions, global distribution
   - Check capacity and growth patterns
   - Assess handling of peak load events
   - Review any published performance metrics or benchmarks
   - Evaluate database architecture choices

6. **Security Posture Evaluation**
   - Search for published security incidents or breaches
   - Check if they have bug bounty program
   - Review security certifications (SOC2, ISO27001, etc.)
   - Assess compliance requirements they meet
   - Look for security hiring and investment signals

7. **Open Source Usage**
   - Identify major open source dependencies
   - Check for contributions back to open source community
   - Assess license compliance risks
   - Evaluate reliance on community vs proprietary tech
   - Flag single-vendor dependencies

8. **Product Architecture Signals**
   - Analyze product maturity and stability
   - Check for major refactors or rewrites in recent years
   - Research API design choices and evolution
   - Assess product-market fit signals
   - Evaluate technical moats (difficult to replicate features)

9. **Output: Due Diligence Report**
   - Executive Summary (1-2 paragraphs): Overall technical health assessment
   - Stack Summary: Technologies and architecture overview
   - Team Assessment: Capabilities and gaps
   - Technical Debt Assessment: Liabilities and risk areas
   - Security & Compliance: Posture and incident history
   - Open Source Assessment: Dependency landscape
   - Scalability Review: Growth capacity evaluation
   - Risk Assessment: Red flags and concerns
   - Recommendations: Strategic implications and risk mitigation

10. **Risk Scoring**
    - Technology Stack: Green/Yellow/Red
    - Team: Green/Yellow/Red
    - Scalability: Green/Yellow/Red
    - Security: Green/Yellow/Red
    - Overall Risk: High/Medium/Low

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- For acquisitions: assess technical integration feasibility
- For partnerships: evaluate capability to deliver
- For investments: gauge technical runway and moats
- Flag unrealistic or unsustainable technology choices
- Consider market fit vs technical soundness trade-offs
