---
name: DevOps & SRE Research
description: >
  CI/CD pipelines, platform engineering, reliability patterns, DORA metrics, GitOps, and infrastructure automation.
  Address "CI/CD pipeline for", "deployment strategy", "reliability SLO", "DORA metrics", "platform engineering" questions.
  Evaluate MTTR, deployment frequency, change failure rate, lead time, and team scaling patterns.
  Critical for building reliable systems and measuring engineering effectiveness.
---

# DevOps & SRE Research Domain

## Overview

DevOps and SRE research bridges infrastructure automation, reliability engineering, and organizational metrics. This domain has matured from "DevOps is a mindset" to concrete measurement frameworks: DORA metrics quantify engineering effectiveness, SLO/SLI/SLA establish reliability expectations, and platform engineering tools standardize deployment patterns.

Effective research here means understanding: how do CI/CD architectures enable velocity without sacrificing reliability? What SLO targets actually align with user experience? How does platform engineering scale autonomy across distributed teams?

## Key Research Dimensions

**CI/CD Architecture & Tooling**
- Build systems: Jenkins, GitHub Actions, GitLab CI, CircleCI, Buildkite
- Testing automation: unit, integration, E2E, performance, security scanning
- Artifact management: container registries, binary repositories, versioning
- Deployment strategies: blue-green, canary, rolling, feature flags
- Rollback and recovery procedures
- Build performance: cache strategies, parallelization, artifact reuse

**Infrastructure as Code (IaC)**
- Declarative tools: Terraform, Pulumi, CloudFormation, ARM templates
- Configuration management: Ansible, Chef, Puppet (though IaC preferred)
- GitOps: Flux, ArgoCD, keeping state in Git as source of truth
- Environment parity: dev/staging/prod consistency
- State management: local, remote, secrets encryption

**Reliability Engineering**
- Service Level Objectives (SLOs): what availability/latency is acceptable?
- Service Level Indicators (SLIs): what metrics define SLO achievement?
- Error budgets: how much downtime can you afford this quarter?
- Incident response: detection, escalation, postmortem processes
- Chaos engineering: testing failure scenarios
- Capacity planning: growth modeling, resource forecasting

**Platform Engineering & DX**
- Internal developer platforms: what abstractions reduce cognitive load?
- Self-service capabilities: how much can teams provision independently?
- Standardization: golden paths that constrain choices to reduce options
- Observability: centralized logging, metrics, tracing infrastructure
- On-call experience: alert fatigue, runbook quality, escalation clarity

**DORA Metrics**
- **Deployment Frequency**: how often do you deploy? (Daily ideal, weekly acceptable, monthly indicates friction)
- **Lead Time for Changes**: from commit to production. (Hours ideal, days acceptable, weeks indicates process bottleneck)
- **Mean Time to Recovery (MTTR)**: how fast can you recover from incidents? (Minutes to hours ideal)
- **Change Failure Rate**: % of deployments causing incidents. (0-15% ideal, > 30% indicates poor testing)

## Data Sources & Query Methods

**DORA Metrics & Industry Benchmarks**
- DORA/Four Keys annual reports on engineering effectiveness
- State of DevOps reports with industry benchmarks
- Accelerate book (Forsgren, Humble, Kim) for DORA framework
- Cloud provider surveys (AWS, Google Cloud State of DevOps)
- Query pattern: "DORA metrics benchmark", "deployment frequency"

**CI/CD Tool Comparisons**
- GitHub, GitLab, JetBrains reports on tool adoption
- Open source tool comparisons (Jenkins, Tekton, Drone)
- Cloud provider native tools evaluation
- Stack Overflow surveys on tool preference
- Query pattern: "CI/CD tool comparison 2024", "GitHub Actions vs GitLab CI"

**Platform Engineering Patterns**
- Internal Developer Platform (IDP) frameworks and maturity models
- Platform Engineering community research
- Case studies from tech companies (Spotify, Airbnb, Stripe)
- StackShare for tool adoption in platform stacks
- Query pattern: "internal developer platform", "platform engineering"

**SRE & Reliability**
- Google SRE book and practices
- PagerDuty, Opsgenie reports on on-call practices
- Site reliability blogs from major tech companies
- Incident.io and PostMortem research
- Query pattern: "SLO setting", "incident response", "MTTR"

**Observability & Monitoring**
- CNCF observability landscape and tool maturity
- Observability vendor reports (Datadog, New Relic, Splunk)
- Open source tool health (Prometheus, Grafana, ELK stack)
- Query pattern: "observability tool comparison", "logging solution"

## Analysis Frameworks

**CI/CD Pipeline Design Assessment**
- **Feedback loop**: How fast do developers learn of failures? (seconds to minutes ideal)
- **Test coverage**: What % of code is tested? (> 80% coverage reasonable)
- **Build time**: P50 and P99 build durations (5-10 min acceptable, >30min painful)
- **Artifact management**: Can you quickly identify what built?
- **Deployment safety**: Can you easily identify which change broke prod?

**SLO Setting Framework**
- **User impact**: What failures matter most to users?
- **Availability**: What uptime SLO aligns with user expectations? (99.9% = 9 hours/year downtime)
- **Latency**: What P99 response time is acceptable? (varies by use case: 10ms vs 1sec)
- **Durability**: Can you lose data? (how long can replication lag?)
- **Error budget**: Given SLO, how many incidents can you afford?

**Deployment Strategy Selection**
- **Risk tolerance**: Blast radius of a bad deploy (all users vs gradual rollout)
- **Blast radius**: Can you quickly affect all users or gradual rollout?
- **Rollback capability**: How fast can you revert a broken deploy?
- **Testing confidence**: Can you test enough to ensure deploy safety?
- **Metrics**: Do you have real-time signals to detect failures?

**Platform Engineering Maturity Assessment**
- **Golden paths**: Do teams follow standard deployment patterns?
- **Self-service**: Can teams provision without bottlenecking on DevOps?
- **Observability**: Is observability built-in or bolted on?
- **Onboarding**: How fast can new team members deploy code?
- **Scaling**: As teams grow, do individual teams slow down?

**DORA Improvement Strategy**
- **Current state**: Measure deployment frequency, lead time, MTTR, change failure rate
- **Bottleneck identification**: Where is friction slowing teams down?
- **Quick wins**: Which changes improve metrics without large investment?
- **Dependency mapping**: What changes require coordination across teams?
- **Investment ROI**: Does improving deployment frequency help business?

## Output Format Templates

### CI/CD Pipeline Design
```
Organization: [company, team size]
Current Pipeline: [tools, deployment frequency]
Pain Points: [slow builds, test flakiness, manual steps]

Recommended Architecture: [build/test/deploy stages]
Tool Stack: [CI/CD, artifact registry, deployment tool]
Performance Targets: [build time, deployment frequency]
Security Integration: [scanning, secrets management, RBAC]
Cost Estimate: [compute, storage, API calls]
Implementation Timeline: [phases, team effort]
```

### SLO Definition & Error Budget
```
Service: [name, critical user flows]
Availability SLO: [e.g., 99.95%]
Latency SLO: [P99 response time]

Error Budget: [hours/month of acceptable downtime]
Monitoring SLIs: [metrics proving SLO achievement]
Alerting: [thresholds that trigger escalation]
Incident Response: [process, stakeholder notification]
Review Cadence: [monthly/quarterly SLO review]
```

### Platform Engineering Roadmap
```
Current State: [existing tooling, process friction]
Target State: [desired DX improvements]

Phase 1: [quick wins, team education]
Phase 2: [infrastructure investment]
Phase 3: [org-wide adoption, scale]

Success Metrics: [DORA improvements, team feedback]
Resource Requirements: [platform engineers, budget]
Dependencies: [upstream infrastructure changes]
```

### Deployment Strategy Comparison
```
Service: [application, risk profile]
Deployment Strategy Options: [blue-green, canary, rolling]

Strategy A: [traffic split, duration, rollback capability]
Strategy B: [traffic split, duration, rollback capability]
Strategy C: [traffic split, duration, rollback capability]

Recommendation: [which strategy wins and why]
Monitoring: [which metrics indicate failure]
Rollback Procedure: [how fast can you revert?]
```

## Key Metrics to Always Collect

For DevOps/SRE decisions, track:
1. **DORA metrics**: Deployment frequency, lead time, MTTR, change failure rate
2. **Reliability**: Availability %, SLO attainment, incident frequency
3. **Performance**: Build time P50/P99, deploy time, recovery time
4. **Quality**: Test coverage %, change failure rate, incident severity distribution
5. **Developer experience**: Mean time to first deployment, build flakiness rate
6. **Cost**: Compute costs, tooling costs, incident response costs

## Computational Workflows

**Pre-built Analysis Scripts**
- `dora_metrics_analyzer.py` — Compute deployment frequency, lead time, MTTR, change failure rate from deployment logs using pandas
- `slo_attainment_calculator.py` — Track availability/latency SLO compliance against error budget using numpy windowing
- `incident_impact_simulator.py` — Model cascade failure and MTTR distributions with scipy for reliability improvements
- `cost_of_downtime_projector.py` — Calculate business impact of outages by duration and time-of-day using Monte Carlo

**Dynamic Computation Examples**
- When setting SLOs, compute error budget allocation across services using statistical proportional allocation
- When evaluating deployment strategies, simulate blast radius and rollback impact across traffic distributions
- When calculating platform engineering ROI, run sensitivity analysis on time savings vs infrastructure costs

**Output Artifacts**
- DORA metrics dashboards (line charts: deployment frequency, lead time trends over time)
- Error budget burndown charts (stacked area: incident impact vs available budget)
- MTTR distribution histogram with confidence intervals and median
- Mermaid state diagram showing incident response flow and escalation paths
- LaTeX formula: Error_Budget (hours) = (1 - SLO) * 730 hours/month; e.g., 99.95% SLA = 2.16 hours/month budget

## References

Load from `references/` directory:
- `dora-metrics-guide.md` — measurement, benchmarking, improvement strategies
- `slo-setting-practices.md` — defining SLOs that align with business
- `ci-cd-pipeline-patterns.md` — architecture decisions and best practices
- `incident-response-procedures.md` — on-call runbooks and postmortem templates
- `platform-engineering-patterns.md` — building internal developer platforms
- `deployment-strategy-guide.md` — blue-green vs canary vs rolling decisions

## Common Pitfalls to Avoid

- **Metric theater**: DORA metrics look good if you deploy broken code frequently
- **Deployment vs delivery**: Fast deployments don't matter if you can't deploy reliably
- **Alert fatigue**: Alerting on everything creates noise; focus on actionable signals
- **SLO mismatch**: 99.99% SLO when 99% aligns with business costs 10x more
- **Platform complexity**: "Platform engineering" that adds friction instead of reducing it
- **Rollback failure**: Testing happy path while rollback fails under pressure
- **Error budget confusion**: Error budget spent on incidents doesn't mean you can deploy more riskily

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~monitoring**: Observability platforms for DORA metric collection, real-time incident tracking
- **~~source control**: Git history for lead time calculation, deployment frequency analysis
- **~~cloud**: Cloud provider APIs for infrastructure changes, deployment pipeline integration

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
