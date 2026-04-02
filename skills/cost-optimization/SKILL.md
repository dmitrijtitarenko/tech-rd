---
name: cost-optimization
description: >
  Cloud cost analysis, build-vs-buy TCO (Total Cost of Ownership), infrastructure right-sizing,
  FinOps practices, license optimization, and cost modeling. Triggered by "cloud cost",
  "cost optimization", "TCO analysis", "build vs buy", "FinOps", "cost reduction".
  Outputs cost analysis with breakeven charts, recommendations, and ROI projections.
---

## Overview

This skill helps organizations identify cost optimization opportunities across cloud infrastructure, software licensing, and build-vs-buy decisions. It provides frameworks for cost visibility, forecasting, and reduction strategies.

## Cloud Cost Analysis

### Cost Drivers & Visibility

**Typical Cloud Cost Breakdown** (AWS/GCP/Azure):
- **Compute** (50-60%): EC2, Lambda, Fargate pricing
  - On-demand vs reserved instances vs spot instances (up to 90% savings)
  - Instance right-sizing (oversized instances = money left on table)
- **Storage** (15-20%): S3, EBS, backup storage
  - Data transfer egress expensive (regional transfer vs internet = 10-100x)
  - Lifecycle policies (cold storage cheaper: Glacier $0.004/GB vs S3 $0.023/GB)
- **Database** (10-15%): RDS, DynamoDB, managed services
  - Multi-AZ replication doubles cost
  - Provisioned vs on-demand capacity; reserved capacity discounts
- **Networking** (5-10%): Data transfer, VPN, CDN
  - Egress often overlooked; can exceed compute costs
  - CDN (CloudFront) reduces origin traffic (cost + performance win)
- **Managed Services** (5-10%): SaaS, third-party APIs, observability
  - SaaS licensing models (per-seat, per-transaction, per-GB) compound
  - Observability (DataDog, New Relic) often 10-20% of compute cost

### Cost Visibility Framework

**Level 0** (Blind): No cost tracking; surprise bills
**Level 1** (Basic): Total monthly bill; no breakdown by service/team
**Level 2** (Detailed): Cost per service, per environment (prod/staging)
**Level 3** (Ownership): Cost allocated to teams/products; accountability
**Level 4** (Optimization): Automated cost reduction via alerts, chargeback, optimization
**Level 5** (Financial**: Cost amortized against business metrics ($ per customer, $ per transaction)

**Tools**:
- AWS Cost Explorer, GCP Billing, Azure Cost Management (built-in)
- Third-party: CloudHealth, Vantage, CloudZero, Apptio (detailed analytics)
- Open-source: KubeCost (Kubernetes-specific), OpenCost

### Right-Sizing Strategies

**Compute Right-Sizing**:
1. **Analyze historical usage**: CPU/memory utilization over 30 days
2. **Identify oversized**: Instances running <20% utilized
3. **Consolidate**: Multiple small instances → medium instance (fewer AWS fees)
4. **Right-sized timeline**: Gradual transition to prevent performance issues

**Example Savings**:
```
Current: 10x m5.xlarge (32 GB RAM each, 20% utilized)
Issue: Paying for 320 GB total, using 64 GB

Optimized: 3x m5.2xlarge (64 GB each, 60% utilized)
Savings: $2000 → $1200 monthly (40% reduction)
```

**Reserved Instances (RIs)**:
- 1-year commitment: 25-40% discount vs on-demand
- 3-year commitment: 50-70% discount vs on-demand
- Finance model: Predictable workloads (database, web servers)
- Risk: Overestimating capacity = unused RIs (use capacity planning)

**Spot Instances**:
- Up to 90% discount vs on-demand (AWS surplus capacity)
- Interruption risk: Can be reclaimed with 2-minute notice
- Use case: Batch jobs, non-critical workloads, with auto-recovery
- Savings: Typical 40-60% on compute cost with proper handling

**Lambda Cost Optimization**:
- Pay per invocation + duration + memory
- Right-size memory (higher memory = faster CPU = less duration cost)
- Example: 256 MB × 30s = same cost as 512 MB × 15s (latter faster)
- Optimize: Profile code for execution speed; reduce cold starts via provisioned concurrency

### Storage Cost Optimization

**Lifecycle Policies**:
```
Day 0-30: S3 Standard ($0.023/GB, hot access)
Day 31-90: S3 Intelligent-Tiering (auto-tiered)
Day 91-365: S3 Glacier ($0.004/GB, 3-5 hour retrieval)
365+: Glacier Deep Archive ($0.00099/GB, 12-hour retrieval)

Example: 1 TB data over 2 years
Standard: 730 days × $0.023 = $16.79 → $0 (after archive)
Intelligent-tier: $8-12 (auto-optimized)
Manual lifecycle: $2-3 (if cold storage acceptable)
```

**Data Transfer Optimization**:
- Egress to internet: ~$0.09/GB (expensive)
- Egress within region: Free
- CloudFront CDN: $0.085/GB (slightly cheaper + faster)
- S3 Transfer Acceleration: $0.04/GB (high-speed upload)
- Strategy: Keep data in region; use CDN for public assets

**Database Storage**:
- RDS: Expensive storage IO ($0.20/million requests)
- Aurora: Better IO efficiency; pay for storage + compute
- DynamoDB on-demand: $1.25/million write units (expensive at scale)
- DynamoDB provisioned: $1.25/million write units (reserved much cheaper)

## Build vs Buy (TCO Analysis)

### Framework

**Build**: Custom development, internal operations
- **Costs**: Engineering salaries, infrastructure, operations (24/7 support)
- **Timeline**: 6-24 months to feature parity
- **Risk**: Technical debt, key person dependencies, opportunity cost

**Buy**: SaaS vendor, managed service
- **Costs**: Subscription (per-seat, per-GB, per-transaction), implementation, migration
- **Timeline**: 1-3 months to deployment
- **Risk**: Vendor lock-in, price increases, feature mismatch

**TCO Comparison Framework**:

| Year | Build (Internal) | Buy (SaaS) | Notes |
|------|---|---|---|
| Year 1 | Dev: $500K + Infra: $200K = $700K | SaaS: $150K/year + Implementation: $50K = $200K | Buy wins initially |
| Year 2 | Ops: $300K + Maintenance: $100K = $400K | SaaS: $150K + Training: $20K = $170K | Buy still cheaper |
| Year 3 | Ops: $300K + Features: $200K = $500K | SaaS: $200K (price increase) | Breakeven approaching |
| 5-year TCO | $500K + $400K + $500K + $500K + $500K = $2.4M | $200K + $170K + $200K + $220K + $240K = $1.03M | Buy: $1.37M cheaper |

**Decision Factors**:
- **Customization ceiling**: Does SaaS meet 80%+ of requirements? (Rule of 80)
- **Vendor strength**: Is vendor stable? (startup vs established?)
- **Lock-in risk**: Can you migrate away if unsatisfied?
- **Competitive advantage**: Is this core (build) or commodity (buy)?

**Examples**:
- **Build**: Recommendation engine (core competitive advantage; Amazon, Netflix)
- **Buy**: Email service (commodity; use SendGrid/Mailgun)
- **Hybrid**: Observability (core but tools mature; use Datadog + custom dashboards)

## FinOps Practices

### Organizational Structure
- **Cloud Center of Excellence (CoE)**: Cross-functional (engineering, finance, operations)
- **Shared responsibility**: Engineers own optimization; finance owns budget/governance
- **Accountability**: Chargeback to teams/departments; creates cost awareness

### Optimization Process (Monthly Cycles)
1. **Measure**: Cost per team, per service, per environment
2. **Analyze**: Waste identification (idle resources, overprovisioning)
3. **Recommend**: Specific optimizations (right-size, reserved instances, shut down)
4. **Implement**: Engineering action on recommendations
5. **Verify**: Measure improvement next month

### Cost Optimization Quick Wins (Low Effort, High Impact)
- Delete unattached EBS volumes ($100/month per TB)
- Terminate unused EC2 instances (development/test left running)
- Enable S3 lifecycle policies (move old data to Glacier)
- Use Reserved Instances for stable workloads (25-70% savings)
- Enable CloudFront for assets (5-10% data transfer savings)
- Use Spot instances for batch jobs (60% savings)

**Expected savings**: 10-30% without capacity reduction; larger with redesign

## License Optimization

### Software License Types

**Perpetual Licenses**: Pay once, own forever (diminishing cost-of-ownership)
- Higher upfront cost ($10K-100K+)
- Ownership model; no recurring payments
- Upgrades often sold separately
- Example: Enterprise database licenses (Oracle, SQL Server)

**Subscription Licenses**: Pay monthly/yearly (predictable cost)
- Lower upfront ($100-1000/month)
- Always latest version included
- Cancellable but recurring cost
- Example: SaaS (Slack, Jira Cloud, Salesforce)

**Per-Seat vs Per-User**:
- Per-seat: License tied to specific person (team size fixed cost)
- Per-user: Shared license pool; users on-demand (flexible sizing)
- Example: Slack is per-seat; Datadog is per-host or per-event

**License Audit**:
1. Catalog all software licenses (spreadsheet)
2. Compare actual usage to license count
3. Identify under-utilized (more licenses than users)
4. Negotiate volume discounts or downsize licenses

**Typical Savings**: 15-30% via consolidation, volume discounts, or license reassignment

## Cost Forecasting & Anomaly Detection

### Forecasting Methods

**Trend-based**: Historical growth × projection
- Example: 20% monthly growth → forecast 12 months ahead
- Risk: Assumes growth continues; doesn't account for seasonal changes

**Capacity-based**: Map business metrics to cost
- Metric: 1M transactions/month = $10K cloud cost
- Forecast: 2M transactions = $20K expected cost
- Allows CFO to tie cost to business ($ per transaction)

**Scenario analysis**: What-if modeling
- Scenario A: Maintain current workload = $50K/month
- Scenario B: 2x traffic + 2x team size = $150K/month
- Identify break-even point for pricing/monetization

### Anomaly Detection
- Alert on 20%+ month-over-month increase (investigate before accepting)
- Automated alerts for unused resources
- Example: CloudTrail logs identify orphaned resources being deleted nightly

## When to Use This Skill

- **Cloud cost audit**: "Why is the bill so high?" → detailed breakdown and recommendations
- **Budget planning**: Finance forecasting for next fiscal year
- **Right-sizing project**: Optimizing existing infrastructure
- **TCO analysis**: Build internal tool vs use SaaS vendor
- **License optimization**: Software audit and renegotiation
- **Post-incident analysis**: Did incident spike costs? (runaway auto-scaling?)
- **Scaling strategy**: How much will infrastructure cost at 10x scale?

## Output Examples

- Cost analysis report (current spending breakdown; waste identification; recommendations)
- Optimization roadmap (quick wins vs medium-term vs long-term projects)
- Right-sizing recommendations with estimated monthly savings
- Reserved instance analysis (break-even timeline; commitment strategy)
- TCO comparison (build vs buy; financial projections 5-year horizon)
- FinOps operating model (governance, chargeback, optimization process)
- Anomaly alert configuration (automated cost spike detection)

## Computational Workflows

### Pre-built Analysis Scripts

**cloud_cost_simulator.py**: Models multi-cloud TCO across AWS, GCP, Azure. Inputs: compute type (on-demand/reserved/spot ratio), storage (volume, lifecycle tiers), data transfer (egress volume), managed services (RDS, Datadog). Outputs: monthly cost projection by service, savings with Reserved Instance commitment, spot instance interruption impact.

**resource_rightsizing.py**: Analyzes CPU/memory utilization from CloudWatch. Inputs: instance type, utilization over 30 days (p50, p95, p99). Identifies: oversized instances (<20% utilized), undersized (running at 95% capacity). Outputs: right-size recommendation with cost delta ($), conversion timeline, performance risk assessment.

**reserved_instance_breakeven_calculator.py**: Compares on-demand vs 1-year vs 3-year Reserved Instance pricing. Inputs: instance type, utilization assumption, growth rate. Outputs: break-even point (when RI becomes cheaper), cost savings projection, commitment risk (stranded capacity if traffic drops).

**build_vs_buy_tco_modeler.py**: Compares custom build (engineer salaries, infrastructure) vs SaaS. Inputs: feature complexity, team size, 5-year timeline with inflation. Outputs: year-by-year cost comparison, break-even point, customization ceiling (will SaaS meet 80% of needs?), risk adjustment (vendor lock-in, price increases).

### Dynamic Computation Examples

1. **Cloud Cost Optimization Roadmap**: Input: current AWS bill ($100K/month), utilization patterns, growth forecast. Identify: quick wins (unattached volumes, unused instances), medium-term (RI purchases, storage lifecycle), long-term (architecture redesign). Output: phased savings roadmap, $500K/year opportunity quantified.

2. **FinOps Chargeback Model**: Input: team allocations, service consumption (compute, storage, network). Compute: cost per team, cost per service, unit cost ($/per request, $/per user). Output: monthly chargeback report, team accountability scorecard, cost variance analysis (spending vs budget).

3. **Lambda Optimization Analysis**: Input: Lambda invocation count, duration, memory setting (current vs optimal). Model: cost per invocation, cold start overhead. Compute: optimal memory (balance: CPU → duration reduction vs memory cost). Output: cost savings projection, performance improvement (latency), payoff timeline.

### Output Artifacts

- **Cloud Cost Analysis Report**: Current spending breakdown (compute 50%, storage 20%, network 10%, managed services 20%), waste identification, top 10 cost drivers
- **Cost Optimization Roadmap**: Quick wins (weeks), medium-term (1-3 months), long-term (3-12 months) with estimated monthly savings per phase, resource requirements
- **Right-Sizing Recommendations**: Instance-by-instance analysis (current vs recommended sizing), estimated monthly savings ($), performance risk, conversion timeline
- **TCO Comparison Model**: Build vs buy financial projection (5-year), year-by-year cost, break-even analysis, risk factors (vendor increase, customization gap), recommendation with confidence

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~cloud**: Real-time cloud cost APIs, pricing data, resource consumption metrics
- **~~financial data**: Pricing data, business metrics for ROI analysis, unit economics
- **~~monitoring**: Infrastructure utilization data, performance metrics, capacity planning signals

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: Cloud provider APIs (AWS Cost Explorer, GCP Billing API), FinOps tools (CloudHealth, Vantage, CloudZero), business metrics (revenue, transaction count for cost-per-unit analysis), financial modeling tools (Excel, Tableau)
