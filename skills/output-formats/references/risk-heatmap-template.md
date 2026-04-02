# Risk Heat Map Template

A risk heat map visualizes risk exposure across likelihood and impact dimensions, helping prioritize mitigation efforts. Use this to identify and manage risks systematically.

## Framework

**Axes:**
- X-axis: Likelihood (1-5 scale, left to right)
- Y-axis: Impact (1-5 scale, bottom to top)
- Score: Likelihood x Impact (1-25 scale)

**Color Coding:**
- Red (Score 16-25): Critical, immediate action required
- Orange (Score 10-15): High, action plan required
- Yellow (Score 5-9): Medium, monitor and plan
- Green (Score 1-4): Low, acknowledge and monitor

## Heat Map Grid

```
IMPACT
   5 |  5  10  15  20  25
   4 |  4   8  12  16  20
   3 |  3   6   9  12  15
   2 |  2   4   6   8  10
   1 |  1   2   3   4   5
     +--------------------
       1   2   3   4   5  LIKELIHOOD

Color coding by score:
- 16-25: RED (Critical)
- 10-15: ORANGE (High)
- 5-9: YELLOW (Medium)
- 1-4: GREEN (Low)
```

## Risk Categories

Standard categories for technology adoption:

1. **Technical Risks** - Implementation, performance, scalability, architectural issues
2. **Security Risks** - Vulnerability, data breach, compliance violation
3. **Vendor Risks** - Vendor viability, lock-in, support availability
4. **Compliance Risks** - Regulatory, legal, audit, certifications
5. **Operational Risks** - Team capability, hiring, training, support burden
6. **Market Risks** - Technology obsolescence, competitor actions, market shifts

## Scoring Methodology

### Likelihood Scale (1-5)

| Score | Definition | Probability | Examples |
|-------|-----------|-------------|----------|
| 5 | Almost certain | 80-100% | Regular occurrence, proven to happen before |
| 4 | Likely | 50-80% | Probable given conditions, industry precedent |
| 3 | Possible | 25-50% | Could happen, has happened to similar organizations |
| 2 | Unlikely | 5-25% | Could happen but unlikely given controls |
| 1 | Rare | <5% | Very unlikely, no recent precedent |

### Impact Scale (1-5)

| Score | Definition | Business Effect | Examples |
|-------|-----------|-----------------|----------|
| 5 | Catastrophic | Organization-wide impact, major revenue loss | Business fails, critical data loss, major breach |
| 4 | Severe | Department-wide impact, significant costs | Project delay (6+ months), 6-figure costs, customer-facing outage |
| 3 | Major | Significant impact but recoverable | Project delay (1-3 months), 5-figure costs, some customer impact |
| 2 | Minor | Manageable, contained impact | Project delay (weeks), lower costs, limited scope |
| 1 | Negligible | Minimal impact, easily absorbed | Minor delays, <$10k impact, internal only |

## Complete Example: WebAssembly Adoption Risk Heat Map

```markdown
# WebAssembly Adoption: Risk Heat Map
Date: September 2024
Project: WASM Pilot Implementation

## Risk Assessment Summary

| Risk ID | Risk | Category | Likelihood | Impact | Score | Color | Mitigation |
|---------|------|----------|-----------|--------|-------|-------|-----------|
| T-001 | First project timeline exceeds estimate | Technical | 4 | 3 | 12 | ORANGE | Hire experienced engineers, external consultants |
| T-002 | Performance improvement misses target | Technical | 2 | 3 | 6 | YELLOW | Detailed workload profiling, conservative estimates |
| T-003 | WASM performance slower than JavaScript | Technical | 1 | 4 | 4 | GREEN | Thorough testing, right workload selection |
| S-001 | WASM security vulnerability discovered | Security | 1 | 4 | 4 | GREEN | Monitor security advisories, auto-update |
| V-001 | Hired WASM engineers leave after 6 months | Vendor | 3 | 4 | 12 | ORANGE | Retention bonuses, knowledge documentation |
| V-002 | WASM tooling becomes abandoned | Vendor | 1 | 3 | 3 | GREEN | Rust+WASM backed by Mozilla, strong community |
| C-001 | No compliance issues for WASM usage | Compliance | 1 | 2 | 2 | GREEN | No identified regulatory barriers |
| O-001 | Team capability gaps slow adoption | Operational | 3 | 3 | 9 | YELLOW | Training program, hire specialists |
| O-002 | Infrastructure costs higher than budgeted | Operational | 2 | 2 | 4 | GREEN | Detailed cost modeling, margin of safety |
| M-001 | Competing technology replaces WASM | Market | 1 | 2 | 2 | GREEN | WASM is standardized, unlikely to be displaced |
| M-002 | Serverless computing eliminates WASM demand | Market | 2 | 3 | 6 | YELLOW | Hybrid approach (WASM on serverless) emerging |
| M-003 | Infrastructure innovation reduces WASM advantage | Market | 2 | 2 | 4 | GREEN | WASM advantage is not competitive; nice-to-have |

## Risk Heat Map Visualization

```
         IMPACT
           5 |
           4 |  S-001  T-003
           3 |              V-001   T-002   M-002
           2 |  V-002  M-001        C-001   O-002
           1 |
             +-----------------------------------
               1    2    3    4    5  LIKELIHOOD

Red Zone (16-25): None identified
Orange Zone (10-15): T-001, V-001
Yellow Zone (5-9): T-002, O-001, M-002
Green Zone (1-4): S-001, T-003, V-002, C-001, O-002, M-001, M-003
```

## Risk Details with Mitigation

### ORANGE Zone Risks (Action Required)

#### T-001: First Project Timeline Exceeds Estimate
- **Risk:** WebAssembly projects typically take 12-16 weeks; initial estimate may be too aggressive
- **Likelihood:** 4 (Likely - common with new technology)
- **Impact:** 3 (Major - delays roadmap impact)
- **Score:** 12 (ORANGE)
- **Mitigation Strategy:**
  1. Hire experienced WASM engineers (reduces learning curve 30-40%)
  2. Engage external WASM consultant for 4-6 weeks (external expertise accelerates)
  3. Use proven frameworks/libraries (don't build from scratch)
  4. Budget conservatively: 20 weeks instead of 16 weeks
  5. Define MVP feature (limit scope to essential work)
- **Contingency:** If milestone 1 (week 8) shows 25%+ slip, reduce feature scope immediately
- **Owner:** Engineering Lead
- **Target:** Mitigate to GREEN by end of month 2

#### V-001: Hired WASM Engineers Leave After 6 Months
- **Risk:** Specialized skills create retention risk; WASM engineers command premium salaries
- **Likelihood:** 3 (Possible - industry-standard skill migration)
- **Impact:** 4 (Severe - loss of specialized knowledge, momentum loss)
- **Score:** 12 (ORANGE)
- **Mitigation Strategy:**
  1. Hire 2 WASM engineers minimum (redundancy, not single point of failure)
  2. Offer retention bonus: 20% salary increase, vesting over 2 years
  3. Create WASM knowledge base: patterns, runbooks, code examples (portable knowledge)
  4. Pair programming: have junior engineers work with specialists (knowledge transfer)
  5. Mentoring rotation: specialists mentor different teams (broader engagement)
  6. Plan for replacement hire: budget approved, interview process prepared
- **Contingency:** If key engineer leaves, outsource critical work while recruiting replacement
- **Owner:** HR / VP Engineering
- **Target:** Implement retention strategy before hiring completes

### YELLOW Zone Risks (Monitor and Plan)

#### T-002: Performance Improvement Misses Target
- **Risk:** Expected 15-25% performance improvement may not materialize
- **Likelihood:** 2 (Unlikely - workload selection is critical)
- **Impact:** 3 (Major - project ROI questioned)
- **Score:** 6 (YELLOW)
- **Mitigation Strategy:**
  1. Detailed workload profiling BEFORE PoC begins (identify CPU bottlenecks)
  2. Verify assumptions with real data (don't estimate, measure)
  3. Conservative targets: plan for 15% (bottom of range), anything above is bonus
  4. Select feature carefully: pure CPU-bound, minimal I/O
  5. Benchmark both JavaScript and WASM thoroughly
- **Contingency:** If performance gap is 5-10% (below target), adjust messaging: "efficiency gain" not "major improvement"
- **Owner:** Technical Lead
- **Measurement:** First PoC performance results (week 12)

#### O-001: Team Capability Gaps Slow Adoption
- **Risk:** Team lacks systems programming experience; WASM learning curve affects velocity
- **Likelihood:** 3 (Possible - systems concepts are different from web)
- **Impact:** 3 (Major - timeline delays)
- **Score:** 9 (YELLOW)
- **Mitigation Strategy:**
  1. Training program: 8 hours/engineer on WASM concepts
  2. Online courses: encourage Rust and WASM learning paths
  3. Pair programming: team members work with specialists
  4. Code review focus: early code reviews highlight learning opportunities
  5. Build gradually: start with isolated module (low risk learning)
- **Contingency:** Hire additional specialist if velocity below 60% of plan by week 8
- **Owner:** Engineering Manager
- **Timeline:** Training begins month 1

#### M-002: Serverless Computing Eliminates WASM Demand
- **Risk:** If serverless platforms dominate, WASM optimization less relevant
- **Likelihood:** 2 (Unlikely - browsers are still the platform)
- **Impact:** 3 (Major - strategic misdirection)
- **Score:** 6 (YELLOW)
- **Mitigation Strategy:**
  1. Hybrid approach: WASM works with serverless backends (complementary, not competing)
  2. Monitor market: track serverless adoption vs browser applications
  3. Diversify benefit: sell WASM on user experience, not just cost
  4. Build on standards: WASM is portable, works with any backend
- **Contingency:** Worst-case scenario: WASM benefits reduced but not eliminated. ROI recalculation happens in month 6 review.
- **Owner:** Product Strategy
- **Monitoring:** Quarterly market review

### GREEN Zone Risks (Acknowledge and Monitor)

#### S-001: WASM Security Vulnerability Discovered
- **Likelihood:** 1 (Rare - WASM is extensively audited)
- **Impact:** 4 (Severe - if discovered)
- **Score:** 4 (GREEN)
- **Mitigation:** Monitor Mozilla/W3C security advisories; auto-update WASM runtime

#### T-003: WASM Performance Slower Than JavaScript
- **Likelihood:** 1 (Very unlikely - WASM is designed for speed)
- **Impact:** 4 (Severe - project fails entirely)
- **Score:** 4 (GREEN)
- **Mitigation:** Thorough testing before PoC deployment; only use for compute-bound work

## ASCII Risk Heatmap

Alternative visualization (text-based):

```
Risk Heat Map: WebAssembly Adoption Initiative

IMPACT
5  [ ][ ][ ][R ][R ]  RED: Catastrophic
4  [ ][R ][O ][O ][T ]  ORANGE: Severe
3  [Y ][O ][Y ][O ][M ]  YELLOW: Major
2  [Y ][G ][Y ][O ][G ]  GREEN: Minor
1  [G ][G ][G ][G ][G ]
   1  2  3  4  5
      LIKELIHOOD

Legend:
R = Red (16-25): Critical, immediate action
O = Orange (10-15): High, action plan needed
Y = Yellow (5-9): Medium, monitor and plan
G = Green (1-4): Low, acknowledge and monitor

Actual risks:
T-001: 12 (ORANGE) - Timeline risk
T-002: 6 (YELLOW) - Performance target
T-003: 4 (GREEN) - Technical failure
S-001: 4 (GREEN) - Security vulnerability
V-001: 12 (ORANGE) - Engineer retention
V-002: 3 (GREEN) - Tooling abandonment
C-001: 2 (GREEN) - Compliance risk
O-001: 9 (YELLOW) - Team capability
O-002: 4 (GREEN) - Cost overrun
M-001: 2 (GREEN) - Technology obsolescence
M-002: 6 (YELLOW) - Market shift
M-003: 4 (GREEN) - Competitive advantage
```

## Risk Prioritization

### By Score (Highest to Lowest)

1. **T-001: 12** (Timeline exceeds) - ORANGE, Address immediately
2. **V-001: 12** (Engineer retention) - ORANGE, Address immediately
3. **O-001: 9** (Team capability) - YELLOW, Action plan
4. **T-002: 6** (Performance target) - YELLOW, Monitor closely
5. **M-002: 6** (Market shift) - YELLOW, Monitor and adjust
6. All GREEN risks (Acknowledge, monitor, have contingencies ready)

### By Timing (When to Act)

**Immediate (This Month):**
- T-001: Hire experienced engineers
- V-001: Offer retention packages
- O-001: Launch training program

**Month 2:**
- T-002: Conduct detailed workload profiling
- M-002: Begin market analysis

**Ongoing:**
- Monitor all YELLOW and GREEN risks
- Monthly risk review with team

## Risk Review Cadence

- **Weekly:** Check status of ORANGE risks (T-001, V-001)
- **Bi-weekly:** Review YELLOW risks (T-002, O-001, M-002)
- **Monthly:** Full risk review, update scores if conditions change
- **Quarterly:** Comprehensive risk reassessment

## Risk Tolerance Statement

**Risk Acceptance Criteria:**
- ORANGE zone risks (16-25): Not acceptable; must mitigate or halt project
- YELLOW zone risks (5-15): Acceptable with mitigation plan and contingencies
- GREEN zone risks (1-4): Acceptable; acknowledge and monitor
- Unknown risks: Unacceptable; must identify and assess

**Current Position:** Project is in Yellow zone with two Orange risks identified. Both Orange risks have mitigation plans. Project is approved to proceed with risk management.
```

## Best Practices

1. **Involve cross-functional team:** Get input from technical, product, and operations perspectives
2. **Base on evidence:** Scores should reflect real data, not gut feeling
3. **Be honest about likelihood:** Optimism bias is common; challenge assumptions
4. **Differentiate impact:** Total project failure (5) is different from cost overrun (2)
5. **Update regularly:** Monthly minimum; quarterly comprehensive review
6. **Track mitigation efforts:** Score should improve as mitigations are implemented
7. **Share transparently:** Stakeholders should see risks and understand mitigation strategy
8. **Prepare contingencies:** For each ORANGE risk, have a backup plan

## Adapting to Your Context

### For Technology Adoption
- Emphasize: Technical, Operational, Market, Vendor risks
- De-emphasize: Compliance (unless regulated industry)

### For Open Source Projects
- Emphasize: Community, Vendor (bus factor), Technical debt
- De-emphasize: Operational (unless supporting production)

### For Regulated Industries
- Emphasize: Compliance, Security, Vendor, Operational
- De-emphasize: Market (regulatory environment is stable)

### For Startups
- Emphasize: Market, Operational (hiring), Vendor
- De-emphasize: Compliance (until growth triggers need)

## Risk Score Trending Over Time

Track how scores change as project progresses:

```markdown
## Risk Score Trends (Months 1-6)

| Risk | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Direction |
|------|---------|---------|---------|---------|---------|---------|-----------|
| T-001 | 12 | 10 | 8 | 6 | 4 | 3 | Decreasing (mitigating) |
| V-001 | 12 | 10 | 8 | 6 | 6 | 6 | Stable (ongoing retention) |
| O-001 | 9 | 8 | 6 | 4 | 3 | 2 | Decreasing (team learning) |
| T-002 | 6 | 4 | 4 | 4 | 3 | 2 | Decreasing (validation) |
| M-002 | 6 | 6 | 5 | 5 | 5 | 4 | Slight decrease |

Ideal trajectory: Scores decrease over time as mitigations take effect and risk is de-risked.
```
