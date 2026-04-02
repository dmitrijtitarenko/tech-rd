---
name: tech-trend-synthesis
description: >
  Synthesizes cross-domain technology trends via Gartner hype cycle analysis, technology
  adoption lifecycle (Rogers diffusion model), funding/investment correlation, emerging
  signals from multiple sources. Triggered by "tech trends", "emerging technology",
  "hype cycle", "technology adoption", "what's trending". Outputs trend synthesis report
  with adoption curve visualization and forecast.
---

## Overview

This skill synthesizes disparate signals (funding, GitHub activity, job postings, conference mentions, patent filings) into cohesive technology trend analysis. It helps organizations understand where technologies sit in their lifecycle and when to invest.

## Gartner Hype Cycle Framework

Gartner publishes annual hype cycles across 20+ domains (Cloud, AI, Emerging Tech, etc.)

### Five Phases

1. **Technology Trigger** (Peak of Inflated Expectations)
   - Initial breakthrough or proof of concept announced
   - Media hype drives unrealistic expectations
   - Example: ChatGPT launch (Nov 2022) → peak hype (Dec 2022-Jan 2023)
   - Reality: Few production deployments; most are POCs

2. **Peak of Inflated Expectations**
   - Massive investment and venture capital funding
   - Numerous startups founded overnight
   - "This will change everything" pronouncements
   - Example: Blockchain (2017-2018): ICO bubble, valuations reach peaks
   - Reality check: Most projects fail; only few achieve escape velocity

3. **Trough of Disillusionment**
   - Reality fails to match hype
   - Early adopters report mixed/poor results
   - Funding dries up; startups shut down
   - Media coverage turns negative
   - Example: Blockchain (2018-2020): Most ICO projects fail; Bitcoin/Ethereum persist
   - Survivor effect: Viable projects emerging from wreckage

4. **Slope of Enlightenment**
   - Realistic use cases identified
   - Methodologies and best practices emerge
   - Targeted investments by enterprises
   - Example: Kubernetes (2017-2019): Overcomplicated initially → patterns emerge
   - Reality: Legitimate problems being solved; not panacea

5. **Plateau of Productivity**
   - Widespread adoption in appropriate use cases
   - Tools/platforms mature and standardize
   - ROI proven and measurable
   - Example: Cloud computing (2010+): Universal adoption; AWS dominance
   - Reality: Mature market; competition on features/cost

### Time Scales
- **Trigger to Peak**: 1-2 years (explosive growth)
- **Peak to Trough**: 3-5 years (disillusionment)
- **Trough to Plateau**: 5-10+ years (slow climb to productivity)
- Total: 10-15 year transformation cycle for major technologies

## Technology Adoption Lifecycle (Rogers)

Complements Gartner; focuses on adoption speed and market penetration

### Adopter Categories
- **Innovators** (2.5%): First to adopt; risk tolerant; tech enthusiasts
- **Early Adopters** (13.5%): Opinion leaders; high education; connected
- **Early Majority** (34%): Pragmatists; deliberate decision; peer influence
- **Late Majority** (34%): Skeptics; adopt out of necessity; social pressure
- **Laggards** (16%): Tradition-bound; may never adopt; skeptical of change

### Adoption S-Curve
- **Slow start**: Only innovators; small market share
- **Inflection point**: Early majority crosses threshold; rapid acceleration
- **Plateau**: Late majority saturates; growth slows
- Example: Smartphones took 10 years (2007-2017) to plateau at 85%+ in developed markets

**Implication**: Where is YOUR organization on the curve? Late adopters may lose competitive advantage

## Funding & Investment Signals

### VC Funding Patterns
- **Uptick in funding**: New category attracting investor capital (AI 2017→2023)
- **Average funding size**: Larger rounds = investor conviction + business model clarity
- **Series stage**: Seed-only = early; Series C+ = proven model
- **Exit events**: IPOs, acquisitions validate market opportunity

**Example Analysis**:

```
AI/ML Funding Trend:
- 2015-2016: $5-10B annually
- 2017-2019: $20-30B (explosive growth; hype cycle trigger)
- 2020-2022: $40-50B (peak; large bets on established companies)
- 2023+: Consolidation; focus on applications vs foundational models
→ Signal: AI moving from "trigger" phase toward "enlightenment"
```

### Patent Filing Trends
- **Spike in filings**: New technology space opening (blockchain 2014-2017 spike)
- **Breadth of filers**: Diverse companies (Google, Amazon, startups) = legitimate trend
- **Citation patterns**: New technology cited more = building on foundations
- **Maintenance rate**: Companies paying renewal fees = still valuable

### Job Market Demand
- **New job postings**: "Kubernetes expert" jobs appeared 2017; now standard 2023
- **Salary trends**: Emerging tech commands premium; mature tech normalizes
- **Geographic distribution**: Job clustering in tech hubs = adoption centers
- **Required experience**: "5+ years Rust" in 2023 shows Rust adoption trajectory

## Emerging Signal Detection

### Conference Submissions & Talks
- **Track trends**: Which sessions packed (hot) vs sparse (declining)?
- **Keynote themes**: Major conference keynotes = industry consensus
- **Example**: KubeCon growth 2017-2023 (1000→10000 attendees) = Kubernetes mainstream adoption

### GitHub Activity & Open Source
- **Repository creation rate**: New projects in category = ecosystem growth
- **Star growth**: Rising stars = community interest
- **Contributor diversity**: Multi-company contributions = legitimacy
- **Language shift**: Repos moving from Java → Go/Rust = technology preference evolution

### News Sentiment & Media Coverage
- **Volume**: Mentions in tech news (TechCrunch, ArsTechnica, InfoQ)
- **Sentiment**: Positive vs critical coverage tracks hype cycle phase
- **Publication quality**: Meta coverage in mainstream (Forbes, WSJ) = broader trend

### Academic Research
- **arxiv submissions**: Rising papers in field = active research
- **Conference papers**: NIPS, ICML, OSDI trends indicate research priorities
- **Citations**: Highly cited papers = foundational research directions

## Trend Synthesis Methodology

### Data Sources (Multi-Source Triangulation)
1. **Funding**: Crunchbase, PitchBook, public reports
2. **GitHub**: Repository metrics, language trends
3. **Job postings**: Indeed, LinkedIn, Stack Overflow Jobs
4. **Patents**: USPTO, Google Patents, filing trends
5. **News**: Hacker News, TechCrunch, arxiv, conference announcements
6. **Surveys**: Developer surveys (Stack Overflow, JetBrains), adopter surveys

### Cross-Domain Correlation
- **Example**: AI trend synthesis
  - Funding surge (2017+)
  - Patent filings spike (2016+)
  - GitHub activity exponential (2018+)
  - Job market demand 10x (2017-2023)
  - News hype cycle (trigger 2022, peak 2023, disillusionment 2024?)
  - Academic momentum (rising papers, citations)
  → Consensus: AI transitioning from "peak hype" to "enlightenment" phase

## Adoption Forecast

**Factors Predicting Adoption Speed**:
- **Relative advantage**: How much better than existing solution?
- **Compatibility**: Works with existing systems vs requires replacement?
- **Complexity**: Steep learning curve vs plug-and-play?
- **Observability**: Can people see results? (AI: very observable)
- **Trialability**: Can you test before committing? (POCs common)

**Forecast Examples**:

1. **WebAssembly**: Slow adoption prediction
   - Still in enlightenment phase (2020-2025)
   - Compatible but optional (not required)
   - Steep learning curve vs JavaScript
   - Adoption timeline: 2028-2035 plateau (15-20 year cycle)

2. **Kubernetes**: Already on plateau (2023+)
   - Proven scalability advantage
   - De facto standard (high compatibility for new systems)
   - Steep learning curve (mitigated by managed services)
   - Adoption: 80%+ in enterprise by 2023

3. **Vector Databases**: Early enlightenment (2023-2024)
   - Clear advantage for AI/embeddings
   - New category (no legacy compatibility issues)
   - Moderate complexity (Pinecone, Weaviate abstractions)
   - Adoption timeline: 2026-2032 plateau (specialized category, not universal)

## When to Use This Skill

- **Technology investment decision**: Is this trend worth the investment right now?
- **Roadmap prioritization**: Which emerging tech to invest in first?
- **Competitive watch**: Where are competitors investing? Should we follow?
- **Market positioning**: Which technologies will be table stakes in 3 years?
- **Talent planning**: Which skills will be in demand; plan hiring/training
- **Organizational readiness**: Are we ahead, at, or behind the adoption curve?

## Output Examples

- Hype cycle visualization (5 phases with 15+ technologies positioned)
- Adoption curve with forecast (timeline to plateau by technology category)
- Trend synthesis report (multi-source analysis, consensus signals)
- Investment recommendation (which emerging tech to fund, timeline)
- Risk assessment (hype cycle risk, competitor adoption pressure)
- Skills roadmap (which technical skills to develop by timeline)

## Computational Workflows

### Pre-built Analysis Scripts

**hype_cycle_positioner.py**: Takes technology (e.g., ChatGPT, Kubernetes, Vector DB) and calculates hype cycle phase (Trigger/Peak/Trough/Enlightenment/Plateau). Inputs: funding trends, GitHub activity, job postings, news volume, maturity signals. Outputs: phase classification with confidence score, predicted time to Plateau, recommendation (adopt/trial/assess/hold).

**adoption_curve_forecaster.py**: Fits Rogers adoption S-curve to historical data. Inputs: adoption percentage over time (GitHub stars, job postings, stack overflow questions). Outputs: inflection point estimate, plateau prediction, time-to-mainstream forecast, required critical mass for acceleration.

**technology_convergence_analyzer.py**: Identifies emerging technology combinations (AI + edge computing, blockchain + IoT). Inputs: patent filings, job postings, funding by combination. Outputs: convergence strength score, market opportunity, adoption timeline, companies leading integration.

**trend_signal_aggregator.py**: Pulls data from multiple sources (Crunchbase, GitHub, job boards, arXiv, news). Weights signals: funding (40%), GitHub activity (30%), job demand (20%), academic research (10%). Outputs: consensus trend score (multiple sources confirm trend?), confidence level, outlier signals flagged.

### Dynamic Computation Examples

1. **Multi-Source Hype Cycle Triangulation**: Input: six independent signals (VC funding, GitHub growth, job postings, conference mentions, patent filings, news sentiment). Compute: weighted score for each hype phase. Output: consensus phase with confidence (if all signals agree: high confidence; if divergent: watch carefully), risk of inflated expectations.

2. **Adoption Readiness Forecast**: Input: technology maturity signals (release stability, documentation quality, tool ecosystem), organizational readiness (skills availability, team size). Model: adoption S-curve with org-specific inflection point. Output: timeline for org adoption (we can move to mainstream in 12 months vs 3 years).

3. **Emerging Technology Risk-Return Model**: Input: emerging tech (e.g., Quantum computing). Compute: market timing (when to invest), ROI timeline, risk of failure (hype-to-reality gap). Output: portfolio recommendation (allocate X% exploration budget if high potential, Y% if speculative).

### Output Artifacts

- **Hype Cycle Visualization**: 5 phases with 20+ technologies positioned, movement arrows showing trajectory, adoption timeline annotations
- **Adoption S-Curve Forecasts**: Timeline to mainstream (2-year, 5-year, 10-year horizons) for 10+ tracked technologies with inflection point identified
- **Trend Synthesis Report**: Multi-source signal correlation (funding/GitHub/job postings aligned or divergent?), consensus confidence score, emerging technology discoveries, false signals debunked
- **Investment Recommendation Dashboard**: Technologies to invest in now (early-stage high-potential), monitor (approaching inflection), or wait (immature). Includes timeline, risk profile, required capabilities

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub activity metrics, project creation trends, language adoption signals
- **~~web research**: Conference announcements, news coverage, trend monitoring
- **~~research**: Academic paper submission trends, citation patterns, research momentum signals
- **~~financial data**: Funding trends, startup formation rates, venture capital allocation patterns

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: Funding databases (Crunchbase, PitchBook), GitHub API (activity metrics), job posting aggregators, patent APIs, news aggregation (RSS feeds, HackerNews API), survey data sources, conference talk archives
