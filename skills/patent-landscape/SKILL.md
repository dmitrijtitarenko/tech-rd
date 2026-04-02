---
name: patent-landscape
description: >
  Analyzes technology patents via USPTO and Google Patents. Performs prior art search,
  filing trends analysis, competitive patent portfolio assessment, freedom-to-operate
  evaluation, patent quality analysis. Triggered by "patent landscape", "patent search",
  "freedom to operate", "patent portfolio". Outputs patent landscape map with risk assessment.
---

## Overview

This skill helps organizations understand the patent landscape relevant to their technology strategy. It identifies competitive threats, licensing opportunities, freedom-to-operate risks, and R&D priorities based on patent activity and prior art.

## Patent Databases & Resources

### US Patents (USPTO)
- **Patent Search**: patents.google.com, uspto.gov/patents/search
- **Patent Grant**: 20 years from filing date (17 years from issue date, pre-1995)
- **Patent Application**: Published 18 months after filing (unless not disclosed)
- **Design Patents**: 15 years protection (design/appearance only)
- **Plant Patents**: 20 years protection (botanical innovations)
- **Utility Patents**: Most common for software/hardware/methods (20 years)

**Filing Types**:
- **Provisional**: Lower cost; doesn't require claims; buys 1-year priority
- **Non-Provisional**: Full patent application with claims, drawings, specifications
- **PCT (Patent Cooperation Treaty)**: International filing covering 150+ countries

### Google Patents
- **Advanced search**: Assignee, inventor, filing date, CPC/IPC classification
- **Citation analysis**: Cited by (newer patents referencing), cites (references used)
- **Patent family**: Same invention filed across countries
- **Generics**: Timeline when patent expires (generic drug availability)

## Prior Art Search

**Search Strategy**:
1. **Keyword search**: Problem domain language (e.g., "machine learning recommendation", "distributed caching")
2. **Classification search**: CPC/IPC codes (standardized technology classification)
3. **Inventor/Assignee**: Known competitors or research institutions
4. **Citation network**: Patents cited frequently = foundational prior art

**Interpretation**:
- **Anticipatory prior art**: Existing patent covers your exact invention (death knell)
- **Obvious prior art**: Combination of existing patents/publications = likely non-patentable
- **Non-obvious prior art**: Prior art exists but significant innovation beyond it = may be patentable

**Example**: Searching "blockchain consensus":
- Bitcoin (2008) foundational; many derivatives filed 2011+
- Proof-of-stake variations (Ethereum, Cardano): novel mechanisms but building on Bitcoin
- Sharding (Zilliqa, Polkadot): avoiding prior art by focusing on scalability angle

## Patent Filing Trends Analysis

**Metrics**:
- **Filing volume**: Rising (company investing in R&D) vs declining (mature product)
- **Grant rate**: % of applications granted (higher = stronger patents)
- **Time-to-grant**: Months between filing and grant (20-40 months typical)
- **Continuation applications**: Re-filing with broader/narrower claims (indication of quality)

**Trend Interpretation**:

| Trend | Signal | Implication |
|-------|--------|---|
| Spike in AI patents (2016+) | Early mover advantage | Company positioned in AI market |
| Declining wireless patents | Shifting away from connectivity | Company deprioritizing hardware |
| Increasing blockchain patents (2017-2020 peak) | Hype cycle | Assess technology fit before investing |

**Competitive Analysis**:

```
Filing volume by company (2020-2024):
- Apple: 2,000+ (diversified: ML, hardware, services)
- Google: 1,500+ (AI/ML heavy, cloud infrastructure)
- Microsoft: 800+ (cloud, enterprise software, AI)
- Startup X: 15 (focused, early-stage IP)

Interpretation: Apple/Google have IP breadth; Startup X has deep focus
```

## Patent Portfolio Assessment

### Strengths & Weaknesses

**Strong Patent Portfolio**:
- High claim breadth (covers variations of core idea)
- Key foundational patents with many citations
- Geographic coverage (US + EU + Asia filings)
- Continuation applications showing refinement

**Weak Patent Portfolio**:
- Narrow claims (easy to design around)
- Low citation count (less foundational)
- Single jurisdiction (US only = limited protection)
- Single-filing strategy (one-shot approach vs strategic refinement)

### Licensing Opportunities

**Patent Monetization**:
1. **Cross-licensing**: Trade patents with competitors (reduces litigation risk)
2. **Patent pools**: Industry consortiums sharing core patents (wireless, video codecs)
3. **Licensing**: Charging royalties for patent usage (example: Qualcomm business model)
4. **Assertion**: Patent troll strategy (buying patents, litigating infringement) - high risk/reward

**Patent Quality Signals**:
- **Forward citations**: Patents citing this one = high impact
- **Continuations**: Multiple filings = company refining and protecting variations
- **International coverage**: USPTO + EPO (Europe) + WIPO = serious IP strategy

## Freedom-to-Operate Assessment

**Question**: Can we safely commercialize our product without infringing third-party patents?

**Process**:
1. **Claim chart mapping**: Map our product features to competitor patent claims
2. **Infringement analysis**: Does our implementation read on patent claims?
3. **Invalidation research**: Can this patent be challenged as obvious/anticipated?
4. **Design-around options**: Can we alter product to avoid infringing claims?

**Risk Matrix**:

| Risk Level | Patent Strength | Infringement Risk | Action |
|---|---|---|---|
| Green | Weak (narrow, few citations) | Low | Proceed with caution |
| Yellow | Medium (standard claims, some citations) | Moderate | Design-around assessment; invalidation research |
| Red | Strong (broad, many citations, recent issue) | High | Licensing negotiation or major redesign |

**Example Scenarios**:
- **Amazon vs Synchronoss**: US patent on "cloud computing" too broad; likely unenforceable (risk: low)
- **Qualcomm's FRAND patents**: Standard-essential patents (5G, WiFi) - must license at reasonable rates (risk: licensing cost, not infringement)
- **Tesla's battery patents**: Defensive publications; limited offensive use (risk: medium if directly competing)

## Patent Quality Indicators

### Examination History
- **Office actions**: Examiner rejections before grant; many = hard-fought patent
- **Claims granted**: Original vs final claims (narrowed = examiner skepticism)
- **Continuation chain**: Series of related applications = strategic refinement

### Technical Depth
- **Drawings clarity**: Detailed technical drawings = strong prosecution
- **Specification breadth**: Generic specification = likely invalid; narrow specification = vulnerable to design-around
- **Dependent claims**: Specific variations = stronger position (independent claims often too narrow)

### Enforceability Factors
- **Claim clarity**: Indefinite language reduces enforceability
- **Written description**: Must adequately describe invention (prevents overly broad claims)
- **Enablement**: Specification must enable someone to make/use invention
- **Prosecution history**: Admissions during prosecution ("estoppel") limit scope

## Competitive Intelligence from Patents

**Signals**:
- **CPC/IPC classification**: Where company thinks invention belongs
- **Claims scope**: Broad (defending position) vs narrow (coexisting with others)
- **Licensing statements**: Published licenses indicate market willingness to pay
- **Patent families**: International filings indicate market priorities

**Example: Video Codec Patents**
- HEVC/H.265 (2013): Patent pool with ~200 patents; royalty rates published (~0.5-2% of product price)
- AV1 (2018): Alliance (Google, Amazon, Netflix) pursued royalty-free codec
- Implication: Codec selection depends on licensing cost vs performance trade-off

## When to Use This Skill

- **Freedom-to-operate assessment**: Before launching new product/feature in competitive market
- **IP strategy**: Building patent portfolio in emerging technology (AI, quantum, blockchain)
- **Prior art search**: Validating patent-ability before filing expensive patent applications
- **Competitive intelligence**: Understanding competitor IP strategy (filing trends, portfolio strength)
- **Licensing evaluation**: Should we license this patent or design around it?
- **M&A analysis**: Patent portfolio as part of company valuation
- **Invalidation research**: Challenging competitor patents in litigation

## Output Examples

- Patent landscape map (filing trends, key players, gaps in coverage)
- Prior art report (closest patents found, patentability assessment)
- Freedom-to-operate analysis (risk matrix, design-around options)
- Competitive patent portfolio assessment (strengths, weaknesses, licensing leverage)
- Patent filing roadmap (strategic priorities, geographic coverage strategy)
- Licensing negotiation guidance (comparable royalty rates, negotiation leverage)

## Computational Workflows

### Pre-built Analysis Scripts

**prior_art_search_engine.py**: Searches USPTO and Google Patents using keyword, CPC/IPC classification, inventor/assignee filters. Inputs: invention description, domain keywords, competitors to exclude. Outputs: ranked prior art matches, citation analysis (cited-by relationships), novelty assessment score.

**patent_portfolio_analyzer.py**: Analyzes company's patent filings (via USPTO). Tracks: filing velocity (applications/year), grant rate (% approved), continuation patterns (claim refinement), geographic coverage (US, EU, Asia). Outputs: portfolio strength score, claim breadth assessment, competitive positioning.

**fto_risk_scorer.py**: Maps product features to competitor patent claims. Inputs: product feature list, competitor patents (via Google Patents). Outputs: infringement risk matrix (green/yellow/red per feature), invalidation research recommendations, design-around options.

**licensing_negotiation_modeler.py**: Analyzes comparable patent licenses (royalty rates, field-of-use restrictions). Inputs: patent strength, competitor licenses, market size. Outputs: licensing negotiation range (floor/ceiling), comparable precedents, risk/reward trade-off.

### Dynamic Computation Examples

1. **Patent Landscape Trend Analysis**: Input: patent filing data for technology domain (AI, blockchain, quantum) from 2015-2025. Compute: filing velocity trend, emerging companies (increasing filers), dominant players (citation count), technology maturity signals. Output: competitive positioning map, market opportunity gaps, FTO risk zones.

2. **Freedom-to-Operate Risk Model**: Input: product features, competitor patent portfolios. Identify: features with high infringement risk, design-around feasibility, licensing cost vs design change ROI. Output: mitigation strategy (license, design-around, invalidation challenge), cost-benefit analysis.

3. **Patent Value Assessment**: Input: patent claims breadth, forward citations (who references this?), backward citations (what did it build on?), family size (international filings). Compute: patent quality score, licensing revenue potential, defensive value (blocking competitors), litigation strength.

### Output Artifacts

- **Patent Landscape Map**: Filing trends over time by company and technology domain, key players identified, market opportunity gaps (underpatented areas), technology maturity assessment
- **Prior Art Report**: Closest patents found, anticipatory risk (exact match?), non-obvious prior art combinations, patentability confidence score with caveats
- **Freedom-to-Operate Analysis**: Risk matrix (feature vs competitor patents), design-around feasibility for high-risk features, licensing negotiation strategy, cost estimates
- **Patent Portfolio Strength Assessment**: Claim breadth analysis, geographic coverage (US/EU/Asia), citation metrics (quality of patents), licensing precedents, competitive positioning score

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~web research**: Patent databases (USPTO, Google Patents), filing trends, prior art searches
- **~~financial data**: Patent valuation data, licensing precedents, competitive intelligence

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: USPTO API, Google Patents API (structured patent data), legal databases (litigation histories), scientific citation databases (prior art validation), patent analytics platforms (Lex Machina, Google Patents for trend analysis)
