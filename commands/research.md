---
description: Deep multi-source technology research
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [topic]
---

# Research Command

Execute deep research on any technology topic across multiple sources.

## Workflow

1. **Scope & Clarify (MANDATORY — do NOT skip this step)**
   - Before doing ANY research, engage the user in a brief scoping conversation:
     - If the request contains a URL, fetch and summarize it first
     - Summarize what you understood from their request (1-2 sentences)
     - Ask 2-3 targeted questions to narrow scope, surface assumptions, and understand their actual goal
     - Examples of good scoping questions:
       - "Are you looking for a specific technology recommendation, or do you want to explore the solution space first?"
       - "What constraints matter most — budget, timeline, team skills, or something else?"
       - "Is there an existing system this needs to integrate with?"
   - **If the request is exploratory or open-ended** (e.g., "research possible solutions", "explore approaches", "what's the best way to"), trigger the **interactive-brainstorming** skill FIRST to collaboratively define the research scope with the user
   - **If the request is specific and well-scoped** (e.g., "compare React vs Vue for SSR performance"), confirm your understanding and proceed
   - Only proceed to step 2 AFTER the user has confirmed the research direction
   - This step exists because premature research wastes effort on the wrong question

2. **Parse Input**
   - Extract topic and detect if it's a technology, architecture pattern, or framework
   - Check for specific aspects (e.g., "React security considerations")

3. **Multi-Source Search Strategy**
   - Primary: WebSearch for recent trends, benchmarks, and community discussions
   - Secondary: WebFetch official documentation, GitHub README files, architecture guides
   - Tertiary: Search for academic papers, whitepapers, and technical reports
   - When available, use ~~research (academic papers), ~~source-control (repo analysis)

4. **Information Gathering**
   - Collect key features, use cases, maturity level, adoption patterns
   - Find performance metrics, scaling characteristics, trade-offs
   - Identify notable projects and companies using the technology
   - Research community size, ecosystem, and support availability

5. **Synthesis and Analysis**
   - Create executive summary (2-3 paragraphs)
   - Organize findings into: What It Is, Key Benefits, Limitations, When To Use, Alternatives
   - Highlight important considerations, gotchas, and best practices
   - Note recent developments and forward-looking direction

6. **Output Structure**
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

**CRITICAL for Interactive Web output:** You MUST read and follow `skills/output-formats/SKILL.md` Tier 3 specification exactly. This means:
- Full Vite 5 + React + Tailwind v3 + shadcn project structure (NOT a single JSX file)
- shadcn Card, Badge, Tabs components (NOT raw HTML/div)
- CSS variable colors ONLY: `hsl(var(--chart-1))`, `bg-primary`, etc. (NO hardcoded hex colors)
- cn() utility from clsx + tailwind-merge
- Dark mode toggle
- See `skills/output-formats/SKILL.md` → "Tier 3: Interactive Web" for the full spec

Before producing ANY output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- For very complex topics, consider spawning an agent for investigation
- Always include publication dates and source credibility assessment
- Flag contradictory findings with context
- Suggest follow-up research areas
