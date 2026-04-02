# Examples and Quick Reference

This document shows how to use each of the 12 tech-rd commands with real invocations and expected output structures.

## Commands at a Glance

| Command | Purpose | Example |
|---------|---------|---------|
| `/research` | Deep multi-source research | `/research Rust async runtimes` |
| `/tech-radar` | ThoughtWorks-style radar | `/tech-radar data engineering` |
| `/compare` | Head-to-head comparison | `/compare PostgreSQL vs CockroachDB` |
| `/landscape` | Market overview | `/landscape observability platforms` |
| `/trending` | Adoption trends | `/trending WebAssembly` |
| `/oss-audit` | Open-source health audit | `/oss-audit apache/kafka` |
| `/patent-scan` | Patent landscape | `/patent-scan LLM inference optimization` |
| `/tech-dd` | Due diligence | `/tech-dd Snowflake` |
| `/standards` | Compliance tracking | `/standards NIST AI RMF` |
| `/stack-detect` | Technology profiling | `/stack-detect vercel/next.js` |
| `/build-vs-buy` | Build vs buy evaluation | `/build-vs-buy authentication system` |
| `/migration` | Migration planning | `/migration monolith to microservices` |

## Worked Examples

### /research

**Input:**
```
/research vector databases for RAG pipelines
```

**What happens:**
1. Research Director classifies the request as a deep technology evaluation.
2. Tech Scout scans GitHub, HuggingFace, and web sources for vector DB solutions.
3. Trend Analyst pulls adoption curves (GitHub stars, npm downloads) for top candidates.
4. Deep Researcher performs architecture analysis on the top 5 solutions.
5. Evidence Validator cross-references performance claims across sources.
6. Research Director synthesizes into a unified report.

**Output includes:**
- Executive summary (2-3 paragraphs)
- Comparison table of top solutions with computed metrics
- Architecture diagrams (Mermaid)
- Performance benchmarks (computed via `scripts/benchmark_comparison.py`)
- Recommendations by use case
- Source list with credibility assessment

### /compare

**Input:**
```
/compare Kubernetes vs Nomad for container orchestration
```

**Output includes:**
- Feature comparison matrix (scored 1-10 per dimension)
- Decision matrix with weighted criteria (via `scripts/scoring_model.py`)
- TCO projection for both options (via `scripts/tco_calculator.py`)
- Risk assessment (via `scripts/risk_scorer.py`)
- "When to choose X" recommendation section

### /tech-radar

**Input:**
```
/tech-radar frontend 2026
```

**Output includes:**
- Radar visualization (SVG or interactive React component)
- Four quadrants: Languages & Frameworks, Tools & Platforms, Infrastructure & Architecture, Techniques & Methodologies
- Ring placement with justification for each technology
- Movement indicators (technologies changing rings since last period)
- Radar data file (via `scripts/radar_generator.py`)

### /oss-audit

**Input:**
```
/oss-audit facebook/react
```

**Output includes:**
- Repository health scorecard (maintenance, community, security, documentation)
- Contributor analysis (bus factor, corporate backing)
- Dependency tree risk assessment
- License compliance check
- CVE and security advisory summary
- Market share estimate (via `scripts/market_share_estimator.py`)

### /build-vs-buy

**Input:**
```
/build-vs-buy feature flag system
```

**Output includes:**
- Build cost estimate (engineering hours, infrastructure, maintenance)
- Buy options with TCO (via `scripts/tco_calculator.py`)
- 36-month cost projection comparison
- Risk matrix for both paths (via `scripts/risk_scorer.py`)
- Decision recommendation with confidence score
- SWOT analysis for each option

### /migration

**Input:**
```
/migration Oracle to PostgreSQL
```

**Output includes:**
- Compatibility assessment (data types, stored procedures, extensions)
- Migration phases with timeline
- Risk heat map (via `scripts/risk_scorer.py`)
- Scaling simulation for target system (via `scripts/scaling_simulator.py`)
- Rollback strategy
- Cost comparison: current vs target (via `scripts/tco_calculator.py`)

## Output Formats

Every command supports three output tiers. When prompted, specify your preference:

1. **Markdown** (default) -- Scientific structured document with inline LaTeX math and Mermaid diagrams.
2. **LaTeX/PDF** -- IEEE Academic format with bibliography, TikZ diagrams, and mathematical notation.
3. **Interactive Web** -- React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation.

See `examples/` for sample outputs in all three formats.

## Output Templates

The plugin includes 9 professional templates in `skills/output-formats/references/`:

| Template | Best for |
|----------|----------|
| `tech-radar-template.md` | /tech-radar output |
| `comparison-matrix-template.md` | /compare output |
| `swot-template.md` | Strategic analysis sections |
| `decision-matrix-template.md` | /build-vs-buy weighted scoring |
| `deep-report-template.md` | /research long-form reports |
| `scorecard-template.md` | /oss-audit health scores |
| `executive-brief-template.md` | Leadership summaries |
| `risk-heatmap-template.md` | /migration and /tech-dd risk sections |
| `adoption-curve-template.md` | /trending adoption analysis |
