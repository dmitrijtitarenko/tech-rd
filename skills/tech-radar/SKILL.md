---
name: tech-radar
description: >
  Generates ThoughtWorks-style technology radars organizing tools and practices into four
  quadrants (Languages & Frameworks, Tools, Platforms, Techniques) and four rings (Adopt,
  Trial, Assess, Hold). Triggered by "tech radar", "technology assessment", "build tech radar".
  Produces interactive HTML/SVG radars with scoring framework based on adoption signals,
  maturity, community health, risk factors.
---

## Overview

This skill enables organizations to systematically evaluate and visualize their technology landscape. It creates radars that communicate technology strategy, guide teams toward recommended tools, and provide a framework for governance and decision-making across the organization.

## Radar Quadrants

### Languages & Frameworks
Evaluate programming languages, web frameworks (React/Vue/Angular), mobile frameworks (Flutter/RN), backend runtimes, etc.

**Assessment Criteria**:
- **Language maturity**: Production-ready, version stability, deprecation policy
- **Ecosystem health**: Package quality (npm, PyPI), dependency audit tools, security patching
- **Learning curve**: Community size (Stack Overflow questions), hiring availability
- **Performance**: Benchmarks, startup time, memory footprint for target use case
- **Long-term viability**: Funding, major company backing, adoption trends

**Scoring Example - Rust**:
- Adopt: Systems programming, performance-critical microservices, CLI tools
- Trial: General backend; increasing job market; proven in production
- Assess: WebAssembly; WASM ecosystem still maturing
- Hold: Rapid prototyping (steep learning curve); real-time constraints (borrow checker)

### Tools
Dependency managers (npm, Maven), DevOps tools (Terraform, Ansible), testing frameworks (Jest, pytest), monitoring/observability, CI/CD, containers.

**Assessment Criteria**:
- **Problem fit**: Does it solve your specific use case better than alternatives?
- **Operational complexity**: Setup time, configuration burden, ops skills required
- **Integration**: API, webhook, SDK for your tech stack
- **Community/Support**: Commercial support availability, community activity, documentation quality
- **Lock-in**: Data portability, standard formats, exit cost

**Scoring Example - Docker**:
- Adopt: Standard for containerization; mature ecosystem; easy onboarding
- Trial: Using custom registries/orchestration beyond Docker Compose
- Assess: New security scanning features; rootless mode
- Hold: VM-based deployments (legacy); single-host requirements

### Platforms
Cloud providers (AWS, GCP, Azure), Kubernetes, databases (Postgres, MongoDB), message queues (RabbitMQ, Kafka), serverless (Lambda), managed services.

**Assessment Criteria**:
- **Scalability**: QPS capacity, multi-region support, auto-scaling
- **Cost model**: Transparent pricing, burst handling, FinOps tools
- **Operational overhead**: Managed vs DIY, support SLAs
- **Vendor lock-in**: Data export mechanisms, API compatibility
- **Compliance**: Certifications (SOC2, HIPAA), data residency, encryption

**Scoring Example - Kubernetes**:
- Adopt: Microservices orchestration; stateless applications; team familiar with ops
- Trial: Advanced networking (Istio service mesh); multi-cluster management
- Assess: Edge Kubernetes (K3s); serverless Kubernetes (Knative)
- Hold: Single monolithic application; small team without DevOps capacity

### Techniques
Practices and methodologies: API design (REST, GraphQL, gRPC), testing strategies (TDD, property-based), architectural patterns (microservices, event-driven), security practices (zero-trust, supply chain security).

**Assessment Criteria**:
- **Team readiness**: Skill requirements, training investment
- **Problem domain fit**: Is this technique applicable to your problems?
- **Measurable benefits**: Reduced bugs, faster time-to-market, better scalability
- **Risk**: Organizational adoption friction, tool/framework dependency

**Scoring Example - Infrastructure as Code (Terraform)**:
- Adopt: Cloud infrastructure; multi-environment management; team has DevOps expertise
- Trial: Cross-provider strategy (AWS + GCP); drift detection tools
- Assess: Policy-as-code (Sentinel); advanced state management
- Hold: Ad-hoc provisioning (manual AWS console clicks); small, static infrastructure

## Ring Definitions

**ADOPT**: Use this technology by default
- Proven in production; team trained; strong community; minimal risk
- Examples: Python, TypeScript, PostgreSQL, Docker, AWS S3

**TRIAL**: Suitable for use on internal projects
- Demonstrated value; acceptable risk; justification required to "Adopt"
- Examples: Rust for new microservices, GraphQL for new APIs, Kubernetes for scaling

**ASSESS**: Evaluate in POC/limited scope
- Promising but unproven in organization; learning investment; not recommended for critical systems
- Examples: emerging languages (Zig), experimental platforms (Deno), new tools (Pydantic v2 migration)

**HOLD**: Deprioritized; reduce usage over time
- Replaced by better tools; legacy technology; organizational migration path defined
- Examples: Monolithic architecture without migration strategy, outdated security practices, deprecated frameworks

## Scoring Framework

**Adoption Signals** (40%):
- How many teams use this tech successfully?
- Trend: growing adoption (+10 teams) vs declining (-5 teams)
- Job market demand (salary premium, hiring ease)

**Maturity** (30%):
- Version stability (1.0+ vs 0.x)
- Release cadence (monthly stable releases = good; erratic = caution)
- Known bugs / security vulnerabilities (mature = minimal; new = higher)
- API stability (breaking changes signal immaturity)

**Community Health** (20%):
- GitHub stars, contributor diversity, bus factor (depends on 1-2 people = risky)
- Q&A activity (Stack Overflow, official forums, Discord)
- Ecosystem size (npm packages, library integrations)
- Funding / company backing stability

**Risk Factors** (10%):
- **Vendor lock-in**: Proprietary vs open-source; exit cost
- **Performance**: Does it meet your latency/throughput SLAs?
- **Security**: Known vulnerabilities, security update cadence
- **Scalability**: Have production cases proven it scales to your size?

## Implementation Example

ThoughtWorks maintains build-your-own-radar open-source tool:
https://github.com/thoughtworks/build-your-own-radar

**Output Format**: Interactive SVG with:
- Click-to-reveal descriptions for each quadrant item
- Color-coding: Green (new), gray (from last radar), red (moved down)
- Ring visual encoding: closer to center = stronger recommendation

## When to Use This Skill

- **Creating technology strategy** for organization (publish quarterly/semi-annually)
- **Communicating tech direction** to non-technical stakeholders
- **Governance**: defining what tools/languages teams "should" use vs "should not"
- **Incident analysis**: "should we have held that technology instead of adopting?"
- **Hiring & recruiting**: what's the tech stack, which tools do we value?
- **Vendor evaluation**: which platform to standardize (Kubernetes vs Nomad vs Docker Swarm)?

## Output Examples

- Interactive HTML/SVG radar (quadrant-based visual)
- CSV data format (tool name, quadrant, ring, change from last radar, reason)
- Narrative report (10-20 page PDF): story of each key technology, migration paths
- Process documentation: how often to update, who decides, escalation paths

## Computational Workflows

### Pre-built Analysis Scripts

**tech_adoption_scorer.py**: Scores technologies across Adopt/Trial/Assess/Hold rings. Inputs: adoption signals (team count using), maturity (version 1.0+), community health (GitHub stars, contributor count), risk factors. Outputs: ring recommendation with confidence score and justification.

**radar_data_generator.py**: Parses CSV (technology, quadrant, ring, reason) and generates SVG/HTML radar visualization. Outputs: interactive radar (click-to-expand descriptions), change indicators (moved up/down from last radar), color-coded by status.

**technology_trend_analyzer.py**: Pulls GitHub star trends, job posting volume, funding data for tracked technologies. Compares: adoption velocity (stars/month), hiring demand, VC interest. Outputs: technology momentum score, recommendation for radar positioning.

**governance_readiness_assessor.py**: Maps current tool usage across teams vs. radar recommendations. Inputs: tool inventory (per team), tech radar governance model. Outputs: policy compliance score, teams out-of-policy, recommendations to align adoption.

### Dynamic Computation Examples

1. **Ring Positioning Recommendation Engine**: Input: technology maturity (version), community health (contributors, commit frequency), org adoption (teams using), business risk (vendor stability). Compute: ring positioning (Adopt/Trial/Assess/Hold) with factors-weighted scoring.

2. **Technology Transition Impact Model**: Given technology moving from Trial to Hold, estimate: team retraining time, migration effort, timeline to deprecate. Outputs: migration roadmap phases, resource allocation, risk of technical debt if not transitioned.

3. **Strategic Technology Assessment**: Input: emerging technology (e.g., Zig, WebAssembly, AI agents), org context (team skills, problem domain). Score: strategic fit (solving our problems?), learning curve (hiring/training cost), ecosystem maturity (will it survive?). Output: recommendation (Assess now vs wait and see).

### Output Artifacts

- **Interactive Technology Radar SVG**: Quadrant-based visual (Languages, Tools, Platforms, Techniques) with ring rings (Adopt/Trial/Assess/Hold), clickable for descriptions
- **Radar Positioning Justification Report**: For each technology: rationale for ring, change from last radar, migration path if applicable, responsible teams/owners
- **Governance Compliance Dashboard**: Technologies used vs. approved; teams out-of-alignment; deprecation progress on "Hold" items
- **Quarterly Radar Evolution Chart**: Tracking how technologies move across rings over time, trend analysis of adoption velocity

---

**Supercharged By**: GitHub API (project trends, adoption via starred repos), Stack Overflow data (sentiment analysis), job posting data (hiring demand), tech news RSS feeds (emerging trends), internal tool usage analytics

## Data Sources

| Connector | Purpose |
|-----------|---------|
| ~~web research | ThoughtWorks radar, industry analyst reports, conference trends |
| ~~source control | GitHub trending, npm download stats, crate/gem/pip metrics |
| ~~analytics | Developer survey data, job posting trends, community signals |
