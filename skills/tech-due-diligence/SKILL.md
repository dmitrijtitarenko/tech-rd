---
name: tech-due-diligence
description: >
  Performs M&A technical assessment including tech stack analysis, code quality signals,
  tech debt indicators, team assessment, scalability evaluation, security posture, IP/patent
  review. Triggered by "M&A tech assessment", "technical due diligence", "acquisition review".
  Outputs due diligence report with risk matrix and valuation impact analysis.
---

## Overview

This skill guides technical leaders through comprehensive assessment of target companies during M&A processes. It identifies technical strengths, risks, integration challenges, and hidden costs that impact deal valuation and post-merger integration success.

## Assessment Dimensions

### Technology Stack Analysis

**Architecture Review**:
- **Monolith vs microservices**: Monolith = simpler to understand but harder to scale; microservices = ops overhead but modularity
- **Database strategy**: Single DB vs polyglot persistence; normalization vs de-normalization tradeoffs
- **Async/event-driven**: Kafka/RabbitMQ indicates maturity; HTTP polling = scalability concern
- **Real-time capabilities**: WebSockets, server-push indicate higher technical sophistication

**Infrastructure**:
- **Cloud maturity**: On-premise = legacy risk; cloud-native (Kubernetes) = modern; hybrid = complexity
- **IaC adoption**: Terraform/CloudFormation = reproducible infrastructure; manual = operational debt
- **Multi-region/availability**: Single datacenter = downtime risk; multi-region = geographic resilience
- **Security infrastructure**: TLS, VPN, secrets management vs in-code credentials

**Tech Debt Indicators**:
- **Outdated dependencies**: Major version gaps (Node.js 12 vs 18) = security risk
- **Deprecated frameworks**: Django 1.x, Struts, old Java versions = legacy code
- **Legacy database schema**: Unmigrated to modern schema (no UUIDs, no soft deletes) = operational friction
- **Performance debt**: Unindexed queries, N+1 problems, blocking operations

### Code Quality Assessment

**Metrics**:
- **Test coverage**: <50% = risky; >80% = good; >95% = excellent
- **Code style/lint**: Consistent formatting, automated linting = discipline
- **Documentation**: README completeness, architecture docs, API docs
- **Code review discipline**: All code reviewed vs ad-hoc merges?
- **Refactoring pace**: Continuous improvement vs accumulating technical debt

**Red Flags**:
- Single developer owns critical services (bus factor = 1)
- No version control discipline (merge commits without code review)
- Copy-paste code patterns (DRY violations)
- Comments explaining "why" vs "what" (suggests poor design)

**Source of Truth**:
- GitHub/GitLab analysis: language distribution, commit patterns, contributor activity
- Code quality tools: SonarQube, CodeFactor scores
- SLOC (source lines of code): Large codebases (1M+ lines) = maintenance burden
- Cyclomatic complexity: Functions averaging >10 = hard to test/maintain

### Tech Debt Quantification

**Cost of Debt**:
- **Development velocity impact**: Refactoring slowing down feature work? 10-20% productivity loss typical
- **Operational overhead**: Paying extra for over-provisioned infrastructure due to inefficiency?
- **Bug rate correlation**: Tech debt correlates with defect density
- **Team morale**: Frustration with "legacy code"; hiring risk for talented engineers

**Debt Prioritization**:
- **Critical**: Impacts revenue (performance, availability)
- **High**: Impacts team velocity (hard to change, brittle)
- **Medium**: Nice to fix (documentation, refactoring)
- **Low**: Cosmetic (code style, comments)

**Remediation Cost Estimate**:
- Replatforming microservices: 6-12 engineer-months per service
- Database migration: 3-6 months (data volume dependent)
- Framework upgrade (Django 1 → 4): 2-4 months
- Performance optimization: 1-2 months

### Team Assessment

**Quality Indicators**:
- **Seniority distribution**: 70% senior (good) vs 70% junior (training burden)
- **Tenure**: Average 2+ years = institutional knowledge; <1 year = high churn
- **Hiring velocity**: Growing rapidly = confidence; flat = mature
- **Key person risk**: CEO, CTO, head engineer; what if they leave?

**Engineering Culture**:
- **On-call burden**: 24/7 rotation with 1 person (burnout) vs large rotation (sustainable)
- **Post-mortems**: Blameless culture = learning; blame culture = cover-ups
- **Promotion paths**: Career development = retention
- **Diversity & inclusion**: Underrepresented groups suggest culture issues

### Scalability Assessment

**Current Scale**:
- **QPS (queries per second)**: 100 QPS = small; 10K QPS = mid; 100K+ QPS = enterprise scale
- **Data volume**: <1TB = small; 10-100TB = large; >1PB = massive
- **Concurrent users**: <10K = small; 100K-1M = large
- **Growth trajectory**: 2x/year = sustainable; 10x/year = infrastructure churn

**Scalability Capacity**:
- **Bottleneck analysis**: Where does the system break?
  - Database (single primary, read replicas insufficient)
  - API gateway (single point of failure)
  - Cache layer (Redis eviction, memory saturation)
  - Message queue (throughput limit)
- **Headroom**: If 10K QPS today, can handle 30K QPS without redesign? (3x headroom = good)
- **Multi-region readiness**: Is system ready to expand to new regions?

**Risk Assessment**:
- Black swan scenarios: What if traffic 10x in 1 week? (viral growth, PR)
- Seasonal spikes: Can system handle 3x during peak season?
- Geographic expansion: Can you quickly add regions without redesign?

### Security Posture

**Application Security**:
- **OWASP compliance**: SQL injection, XSS, CSRF mitigations present?
- **Authentication**: OAuth2, JWT, MFA implemented?
- **Authorization**: Role-based access control, principle of least privilege?
- **Encryption**: TLS 1.3+, encryption at rest, key management

**Infrastructure Security**:
- **Network segmentation**: DMZ, internal networks, VPC isolation?
- **Secrets management**: HashiCorp Vault, AWS Secrets Manager vs .env files (bad)
- **Access controls**: IAM policies, SSH key rotation, bastion hosts
- **Monitoring/logging**: Intrusion detection, audit logs, SIEM integration?

**Compliance**:
- **Standards**: SOC2, ISO 27001, HIPAA, PCI-DSS certifications?
- **Data residency**: GDPR compliance, data localization requirements?
- **Vendor risk**: Third-party security assessments, SLAs?

**Vulnerability Management**:
- **Patch cadence**: How fast do security updates roll out?
- **CVE response**: Do they track and patch known vulnerabilities?
- **Penetration testing**: Regular external/internal pen tests?
- **Bug bounty program**: Incentivizing security researchers?

### IP & Patent Analysis

**Intellectual Property**:
- **Proprietary algorithms**: What unique tech does target own?
- **Patent portfolio**: Any defensive patents? (Cost to acquire: $5K-50K per patent)
- **Open-source usage**: Licensing compliance (GPL, AGPL risks)?
- **Trade secrets**: Proprietary data, ML models, datasets

**Patent Risk Assessment**:
- **Infringement risk**: Does target infringe third-party patents?
- **Freedom to operate**: Can acquiring company continue product without license fees?
- **Patent quality**: Utility patents (strong) vs business method patents (weak)?

**Licensing**:
- **GPL compliance**: If using GPL code, must open-source your changes
- **AGPL risk**: If SaaS, must open-source or get license
- **Commercial licenses**: Any vendors demanding license fees post-acquisition?

## Due Diligence Report Structure

**Executive Summary** (2 pages):
- Overall risk assessment (Green/Yellow/Red)
- 3 key risks, 3 opportunities
- Valuation impact (-/+ %)

**Technical Findings** (10-15 pages):
- Architecture overview with diagrams
- Tech debt quantification and remediation roadmap
- Scalability assessment and growth capacity
- Security posture vs industry standards
- Team capability and key person risks

**Risk Matrix**:

| Risk | Likelihood | Impact | Mitigation |
|------|---|---|---|
| Single database point of failure | High | Critical | Multi-region replication required (2-3M cost) |
| Key CTO departure | Medium | High | Retention package; knowledge transfer plan |
| GPL compliance violation | Medium | Critical | Audit codebase; license audit tool |
| Performance bottleneck at 10K QPS | Low | High | Caching layer, database optimization (1-2M) |

**Integration Roadmap**:
- 0-3 months: Knowledge transfer, quick wins
- 3-6 months: Tech debt remediation (priority items)
- 6-12 months: Larger infrastructure migrations
- 12+ months: Full platform consolidation

**Valuation Adjustments**:
- Tech debt reduction: -$X million (cost to fix)
- Security remediation: -$Y million (risk if breached)
- Team retention risk: -$Z million (key person dependency)
- IP value: +$N million (proprietary algorithms, patents)

## When to Use This Skill

- **Pre-LOI assessment**: Before signing letter of intent
- **Post-LOI detailed diligence**: Deep technical dive before closing
- **Integration planning**: Technical roadmap post-acquisition
- **Valuation support**: Providing data for deal negotiation
- **Risk identification**: What could derail the acquisition?
- **Competitor acquisition**: Understanding competitor technology strategy
- **Talent assessment**: Is the engineering team world-class or average?

## Output Examples

- Executive summary with risk dashboard (green/yellow/red)
- Detailed technical assessment report (architecture, code quality, tech debt)
- Risk matrix with mitigation strategies and cost estimates
- Integration roadmap (0-12 months, quarterly milestones)
- Valuation adjustment table (financial impact of tech findings)
- Org chart with key person risk assessment

## Computational Workflows

### Pre-built Analysis Scripts

**code_quality_analyzer.py**: Clones target repository, analyzes: test coverage (pytest, Jest coverage reports), cyclomatic complexity, SLOC distribution, dependency freshness (outdated packages), security scanning (Snyk, vulnerable dependencies). Outputs: quality score (1-100), risk heat map by module, technical debt estimate (person-months to remediate).

**tech_debt_quantifier.py**: Maps code quality metrics to remediation cost. Input: complexity score, test coverage gap, deprecation count, security issues. Output: cost estimate (engineers × months), phased remediation timeline, ROI of addressing critical debt vs. deferring, valuation impact (-$X million).

**scalability_assessment_model.py**: Analyzes: current scale (QPS, concurrent users, data volume), bottleneck identification (database, cache, gateway), headroom calculation (3x growth without redesign?). Outputs: scalability maturity score, growth forecast (2 years), replatforming cost if growth targets exceeded.

**team_capability_scorer.py**: Uses LinkedIn API (team size, tenure, skill distribution), GitHub analysis (commit patterns, code review quality). Inputs: org size, seniority distribution, turnover rate. Outputs: team strength score, key person risk matrix, integration cost if acquiring talent attrition.

### Dynamic Computation Examples

1. **Tech Debt Valuation Impact Model**: Input: identified tech debt items (monolith, outdated frameworks, poor test coverage). Compute: productivity impact (% slower feature development), risk cost (incidents, customer churn), remediation timeline. Output: valuation adjustment (-$N million), integration cost, payback timeline if addressed post-acquisition.

2. **Security Risk Scorecard & Breach Cost Projection**: Assess: OWASP compliance gaps, encryption coverage, compliance certifications (SOC2, HIPAA). Compute: breach likelihood given gaps, potential liability (customer data exposed), regulatory fines. Output: security posture score, risk-adjusted valuation impact.

3. **IP & Patent Freedom-to-Operate Analysis**: Search patent databases for competitor patents in acquisition target's space. Assess: infringement risk, licensing cost if conflict exists. Output: FTO risk score (green/yellow/red), licensing negotiation strategy, valuation adjustment for patent liability.

### Output Artifacts

- **Executive Summary Dashboard**: Overall risk assessment (Green/Yellow/Red), 3 key risks with financial impact, 3 opportunities, valuation adjustment recommendation
- **Technical Assessment Report**: Architecture overview, code quality score with module-level breakdown, tech debt quantification and remediation roadmap, scalability assessment
- **Risk Matrix**: Detailed risks (single DB failure, key CTO departure, GPL compliance violation) with likelihood, impact, mitigation cost, financial impact
- **Integration Roadmap Gantt**: 0-3 month (knowledge transfer), 3-6 month (critical tech debt), 6-12 month (infrastructure migration), 12+ month (full consolidation)
- **Valuation Impact Summary Table**: Tech debt reduction (-$X), security remediation (-$Y), team retention (-$Z), IP value (+$N), net adjustment

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub codebase analysis, contributor history, code quality metrics
- **~~financial data**: Financial performance data, funding history, revenue trends for valuation
- **~~web research**: Public company information, press releases, technical blog posts
- **~~project tracker**: Current roadmap items, velocity metrics, team capacity signals

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: GitHub API (codebase analysis, contributor history), CVE databases (security risk assessment), patent databases (USPTO, Google Patents), financial data sources (revenue/growth trends for valuation), employee data (LinkedIn for team assessment), cloud APIs (infrastructure cost analysis)
