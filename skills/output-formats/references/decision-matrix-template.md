# Weighted Decision Matrix Template

A decision matrix provides a quantitative framework for making choices between multiple options when multiple criteria matter. Use this when subjective judgment needs to be structured and justified.

## Framework

A decision matrix consists of:

1. **Criteria** - The factors that matter to the decision
2. **Weights** - Relative importance of each criterion (sum to 100%)
3. **Scoring** - How each option performs on each criterion (1-5 scale)
4. **Calculation** - Weighted score = (Criterion Score × Weight) summed across criteria
5. **Sensitivity** - Testing how robust the decision is to weight changes

## Defining Criteria and Weights

### Step 1: Identify Decision Criteria

List all factors that influence your decision:

```markdown
## Criteria Candidates

### Must-Haves (Threshold)
These are non-negotiable minimums:
- Criterion: Minimum uptime SLA
- Threshold: 99.9% or higher
- Action: Eliminate options below threshold

- Criterion: Security certifications
- Threshold: Must support SOC 2 Type II
- Action: Eliminate options without certification

### Nice-to-Haves (Weighted)
These go into the decision matrix:
- Criterion: Cost
- Criterion: Performance
- Criterion: Ease of integration
- Criterion: Vendor stability
- Criterion: Community support
- Criterion: Feature completeness
- Criterion: Learning curve
```

### Step 2: Define Weights

Allocate importance across criteria. The sum must equal 100%:

```markdown
## Weight Assignment Process

### Step 2a: Initial Ranking
Rank criteria from most to least important:
1. Cost (fundamental budget constraint)
2. Performance (directly impacts user experience)
3. Integration (requires engineering effort)
4. Vendor stability (long-term viability)
5. Community support (enables faster problem-solving)
6. Feature completeness (prevents future rework)
7. Learning curve (team ramp-up time)

### Step 2b: Allocate Points
Use this method: Most important gets largest share, distribute remaining

| Rank | Criterion | Initial Points | Adjustment | Final Weight |
|------|-----------|-------|----------|--------------|
| 1 | Cost | 30 | -10 | 20% |
| 2 | Performance | 30 | +5 | 25% |
| 3 | Integration | 20 | 0 | 20% |
| 4 | Vendor Stability | 15 | +5 | 15% |
| 5 | Community Support | 10 | -5 | 10% |
| 6 | Feature Completeness | 10 | +5 | 10% |
| 7 | Learning Curve | 0 | 0 | 0% |
| **TOTAL** | | **115** | **-5** | **100%** |

### Rationale
- Reduced Cost from 30 to 20: Cost matters but not at expense of core functionality
- Increased Performance to 25: Directly tied to SLA commitments
- Kept Integration stable at 20: Significant engineering effort required
- Increased Vendor Stability to 15: Regulatory environment demands partner stability
- Reduced Community to 10: We have internal expertise, not critical
- Increased Feature Completeness to 10: Avoid multi-vendor complexity
- Set Learning Curve to 0: Team can learn anything quickly if needed
```

## Scoring Rubric

Apply consistent criteria across all options:

```markdown
| Score | Meaning | Examples |
|-------|---------|----------|
| 5 | Excellent | Exceeds requirements, clear best-in-class, standout performance |
| 4 | Strong | Meets requirements well, few concerns, good performance |
| 3 | Adequate | Meets basic requirements, acceptable tradeoffs, standard performance |
| 2 | Weak | Below expectations, notable gaps, workarounds needed |
| 1 | Poor | Fails to meet requirements, critical gaps, unsuitable |
```

### Criterion-Specific Scoring Guides

#### Cost (Budget Constraint)
- **5:** Free or <$10k annually all-inclusive
- **4:** $10k-30k annually, transparent pricing
- **3:** $30k-100k annually, some hidden costs
- **2:** $100k-500k annually, unclear pricing structure
- **1:** >$500k annually or prohibitively expensive

#### Performance (Speed/Throughput)
- **5:** <100ms response time, >10k ops/sec, exceeds SLA
- **4:** <500ms response time, >1k ops/sec, meets SLA
- **3:** <2s response time, 100-1k ops/sec, acceptable
- **2:** 2-10s response time, <100 ops/sec, below SLA
- **1:** >10s response time, single digit ops/sec, unacceptable

#### Integration (Ease of Connection)
- **5:** Plug-and-play, APIs available, <1 day integration
- **4:** Standard REST/GraphQL APIs, 1-3 days integration
- **3:** APIs available, moderate effort, 1-2 weeks
- **2:** Limited APIs, significant custom work, 2-4 weeks
- **1:** No APIs, requires complete custom development

#### Vendor Stability (Viability)
- **5:** Publicly traded, >$1B revenue, 10+ year track record
- **4:** Well-funded, >$100M revenue, 5+ year track record
- **3:** Stable, $10M+ revenue, 2-5 year track record
- **2:** Underfunded, <$10M revenue, <2 years or recent funding
- **1:** Unstable, series-stage risk, or history of shutdowns

#### Community Support (Help Available)
- **5:** 100k+ users, <1 hour response on forums, extensive docs
- **4:** 10k-100k users, <4 hour response, good documentation
- **3:** 1k-10k users, <1 day response, adequate docs
- **2:** <1k users, slow response, sparse documentation
- **1:** Abandoned or no community, no support resources

#### Feature Completeness (Covers Needs)
- **5:** 100% of required features, many bonus features
- **4:** 95%+ of required features, some nice-to-haves
- **3:** 80-95% of required features, basic coverage
- **2:** 60-80% of required features, major gaps
- **1:** <60% of required features, critical missing

#### Learning Curve (Time to Proficiency)
- **5:** <1 hour to first success, intuitive UI/API
- **4:** <1 day to basic proficiency, clear documentation
- **3:** 1-3 days to proficiency, acceptable learning materials
- **2:** 1-2 weeks to proficiency, sparse documentation
- **1:** >2 weeks to proficiency, difficult concepts

## Example: Database Selection

```markdown
## Decision: Database for Real-Time Analytics Platform

### Candidates
- Option A: PostgreSQL + TimescaleDB
- Option B: InfluxDB (managed)
- Option C: Elasticsearch

### Weights
| Criterion | Weight | Justification |
|-----------|--------|---------------|
| Cost | 20% | Budget constraint: Need sub-$50k/month |
| Performance | 25% | <1s query response required for dashboards |
| Integration | 20% | Must integrate with Kafka, Python, Grafana |
| Vendor Stability | 15% | Need reliable, long-term partner |
| Community Support | 10% | Team needs knowledge resources |
| Feature Completeness | 10% | Geo-temporal queries, aggregations required |
| **TOTAL** | **100%** | |

## Detailed Scores

### Option A: PostgreSQL + TimescaleDB

| Criterion | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Cost | 20% | 5 | Open source (free), self-hosted ($5-10k/month infra) |
| Performance | 25% | 4 | TimescaleDB handles time-series well, <500ms typical queries |
| Integration | 20% | 5 | Excellent PostgreSQL drivers, native Kafka support |
| Vendor Stability | 15% | 5 | PostgreSQL 25+ years stable, Timescale VC-backed |
| Community Support | 10% | 5 | Massive PostgreSQL community, strong TimescaleDB support |
| Feature Completeness | 10% | 4 | Full SQL, geo-temporal support, minor features missing |
| **WEIGHTED SCORE** | | **4.50** | Strong choice across all dimensions |

Calculation:
- Cost: 5 × 0.20 = 1.00
- Performance: 4 × 0.25 = 1.00
- Integration: 5 × 0.20 = 1.00
- Vendor Stability: 5 × 0.15 = 0.75
- Community Support: 5 × 0.10 = 0.50
- Feature Completeness: 4 × 0.10 = 0.40
- Total: 4.65

### Option B: InfluxDB (Managed)

| Criterion | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Cost | 20% | 2 | ~$60k/month at scale (exceeds budget) |
| Performance | 25% | 5 | Purpose-built for time-series, <100ms queries |
| Integration | 20% | 4 | Good APIs, Kafka connector available |
| Vendor Stability | 15% | 4 | Series-D funded, growing company, some acquisition risk |
| Community Support | 10% | 4 | Growing community, decent documentation |
| Feature Completeness | 10% | 3 | Time-series excellent, SQL queries limited |
| **WEIGHTED SCORE** | | **3.75** | Performance strong but cost prohibitive |

Calculation:
- Cost: 2 × 0.20 = 0.40
- Performance: 5 × 0.25 = 1.25
- Integration: 4 × 0.20 = 0.80
- Vendor Stability: 4 × 0.15 = 0.60
- Community Support: 4 × 0.10 = 0.40
- Feature Completeness: 3 × 0.10 = 0.30
- Total: 3.75

### Option C: Elasticsearch

| Criterion | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Cost | 20% | 3 | Managed ~$40k/month, licensing complexity |
| Performance | 25% | 3 | Good for logs, slower for complex time-series queries |
| Integration | 20% | 4 | Excellent Kafka connector, widely supported |
| Vendor Stability | 15% | 5 | Elastic public company, enterprise backing |
| Community Support | 10% | 5 | Massive ecosystem, extensive documentation |
| Feature Completeness | 10% | 3 | General-purpose, geo-temporal features adequate |
| **WEIGHTED SCORE** | | **3.60** | Solid choice but not optimized for use case |

Calculation:
- Cost: 3 × 0.20 = 0.60
- Performance: 3 × 0.25 = 0.75
- Integration: 4 × 0.20 = 0.80
- Vendor Stability: 5 × 0.15 = 0.75
- Community Support: 5 × 0.10 = 0.50
- Feature Completeness: 3 × 0.10 = 0.30
- Total: 3.70

## Summary and Recommendation

| Criterion | Weight | PostgreSQL+TimescaleDB | InfluxDB | Elasticsearch |
|-----------|--------|-------------|----------|---------------|
| Cost | 20% | 5 (1.00) | 2 (0.40) | 3 (0.60) |
| Performance | 25% | 4 (1.00) | 5 (1.25) | 3 (0.75) |
| Integration | 20% | 5 (1.00) | 4 (0.80) | 4 (0.80) |
| Vendor Stability | 15% | 5 (0.75) | 4 (0.60) | 5 (0.75) |
| Community Support | 10% | 5 (0.50) | 4 (0.40) | 5 (0.50) |
| Feature Completeness | 10% | 4 (0.40) | 3 (0.30) | 3 (0.30) |
| **TOTAL SCORE** | **100%** | **4.65 / 5.00** | **3.75 / 5.00** | **3.70 / 5.00** |

### Recommendation: PostgreSQL + TimescaleDB

**Confidence Level: HIGH (85%)**

PostgreSQL with TimescaleDB is the clear winner with a 4.65/5.00 score. It excels across cost (critical constraint) and integration (core requirement) while maintaining strong performance and community support.

**Why Option A Wins:**
1. Lowest cost (saves $50k+ annually vs InfluxDB)
2. Excellent integration story (all required systems supported)
3. Time-series optimized while maintaining full SQL
4. Largest community and longest track record
5. Open source prevents vendor lock-in

**Why Option B Was Considered:**
- Strongest performance for time-series queries
- Not selected due to cost exceeding budget and marginal performance benefit

**Why Option C Was Considered:**
- Excellent vendor stability and community
- Not selected because it's general-purpose (not optimized for time-series analytics)
- Cost comparable to Option A with worse performance fit

**Implementation Plan:**
1. Phase 1 (Weeks 1-2): Deploy TimescaleDB in staging, load historical data
2. Phase 2 (Week 3): Run parallel with current system, validate query performance
3. Phase 3 (Weeks 4-6): Migrate analytics workloads, monitor performance
4. Phase 4 (Weeks 7-8): Decommission legacy system
```

## Sensitivity Analysis

Test robustness of your decision to weight changes:

```markdown
## Sensitivity Analysis: How Robust Is This Decision?

### Scenario 1: What if Performance Becomes 35% (was 25%)?

| Option | Original Score | New Score | Change |
|--------|-------|----------|--------|
| PostgreSQL+TimescaleDB | 4.65 | 4.60 | -0.05 |
| InfluxDB | 3.75 | 4.05 | +0.30 |
| Elasticsearch | 3.70 | 3.85 | +0.15 |

**Result:** PostgreSQL still wins, but gap narrows. Decision still robust.

### Scenario 2: What if Cost Becomes 35% (was 20%)?

| Option | Original Score | New Score | Change |
|--------|-------|----------|--------|
| PostgreSQL+TimescaleDB | 4.65 | 4.75 | +0.10 |
| InfluxDB | 3.75 | 3.15 | -0.60 |
| Elasticsearch | 3.70 | 3.45 | -0.25 |

**Result:** PostgreSQL advantage increases. Decision becomes more certain.

### Scenario 3: What if Cost and Performance Swap (Cost=25%, Performance=20%)?

| Option | Original Score | New Score | Change |
|--------|-------|----------|--------|
| PostgreSQL+TimescaleDB | 4.65 | 4.60 | -0.05 |
| InfluxDB | 3.75 | 3.75 | 0.00 |
| Elasticsearch | 3.70 | 3.60 | -0.10 |

**Result:** PostgreSQL still clearly ahead. Extremely robust decision.

### Conclusion
The decision to select PostgreSQL+TimescaleDB is robust across reasonable weight variations. It maintains first-place ranking even with significant weight shifts favoring either cost or performance.
```

## Refinement Questions

Before finalizing your decision, answer these:

1. **Are criteria independent?** Check if any criteria overlap or are redundant
2. **Are weights truly reflective?** Did stakeholders align on importance?
3. **Is scoring evidence-based?** Can you cite reasons for each score?
4. **Were all options fairly scored?** Check for bias toward incumbent or familiar options
5. **Did options change since scoring?** Technology or requirements shifts warrant re-scoring
6. **Is the gap meaningful?** If top option only scores 0.5 points higher, decision less clear
7. **Are there deal-breakers?** Did you check threshold criteria before scoring?

## Best Practices

1. **Document everything:** Show your work so others understand the decision
2. **Include dissenting views:** Note where stakeholders disagreed on weights or scores
3. **Update periodically:** Revisit decision if context changes significantly
4. **Compare apples-to-apples:** Ensure all options scored on same rubric
5. **Avoid false precision:** 4.65 is not meaningfully different from 4.60
6. **Share transparently:** Stakeholders should understand why decision was made
7. **Test assumptions:** Use sensitivity analysis to challenge robustness
8. **Reserve judgment:** Close scores warrant deeper investigation, not automatic selection
