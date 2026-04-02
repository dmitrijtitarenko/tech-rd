---
name: Cloud Infrastructure Research
description: >
  Compare AWS, GCP, Azure, IaC tools, Kubernetes, serverless, and edge computing architectures.
  Address "cloud architecture for", "AWS vs GCP", "serverless for", "Kubernetes" decisions.
  Evaluate cost, scalability, vendor lock-in, managed services maturity, and region availability.
  Essential for infrastructure design, cost optimization, and multi-cloud strategy.
---

# Cloud Infrastructure Research Domain

## Overview

Cloud infrastructure research synthesizes technical capabilities, pricing models, and operational tradeoffs across cloud providers and deployment patterns. The cloud landscape fragments across three major providers (AWS, GCP, Azure), each with distinct service philosophies and hidden complexity.

Effective research here requires moving beyond feature checklists to understand: which managed services actually reduce operational burden vs creating new dependencies? How do pricing models align with your usage patterns? What are the real constraints of serverless, Kubernetes, and edge computing?

## Key Research Dimensions

**Provider Capabilities & Services**
- Compute: VM types, pricing tiers, auto-scaling behavior
- Networking: VPC/VNet design, ingress/egress costs, latency between regions
- Databases: managed SQL, NoSQL, data warehouse options
- Managed services: Kubernetes (EKS/GKE/AKS), serverless (Lambda/Cloud Functions/App Service)
- Data services: ETL, analytics, streaming, real-time processing
- AI/ML: model training infrastructure, inference serving, AutoML offerings

**Cost Structure & Optimization**
- Compute hour rates and reserved instance discounts
- Data transfer costs (inter-region, ingress/egress)
- Managed service overheads vs self-hosted
- Hidden costs: logging, monitoring, storage, API calls
- Commitment discounts and billing anomalies

**Operational Complexity**
- Service SLAs and reliability expectations
- Built-in logging, monitoring, and troubleshooting tools
- API rate limiting and quota management
- Scaling behavior under load (cold starts, rate limits)
- Multi-region failover and disaster recovery setup

**Vendor Lock-In & Portability**
- Proprietary APIs and services (unique features that lock you in)
- Data export mechanisms and interoperability
- Multi-cloud portability (Docker, Terraform, open standards)
- Exit costs and data retrieval timelines
- Switching effort for key workloads

**Regional Availability & Compliance**
- Geographic coverage for target markets
- Data residency and sovereignty requirements (GDPR, etc.)
- Latency profiles between regions
- Compliance certifications (FedRAMP, HIPAA, SOC2)

## Data Sources & Query Methods

**Pricing & Cost Analysis**
- Official pricing pages (AWS, GCP, Azure) with cost calculators
- CloudGarden and similar TCO comparison tools
- GitHub: realistic cost analyses for specific workloads
- ParkMyCloud, Flexera reports on cloud spend trends
- FinOps Foundation benchmarks and case studies
- Query pattern: "cloud cost comparison", "serverless pricing [use case]"

**Service Capability & Feature Comparison**
- Official provider documentation and feature matrices
- Real deployment case studies (AWS/GCP blogs, customer stories)
- Hacker News and r/devops discussions of operational tradeoffs
- GitHub Actions workflows revealing preferred approaches
- Query pattern: "managed Kubernetes comparison", "database options [provider]"

**Performance & Reliability**
- Provider status pages and incident history
- Community benchmarks (MLPerf for ML infrastructure)
- CloudPing latency measurements
- Third-party monitoring (StatusPage, Observability vendors)
- Query pattern: "AWS region latency", "GCP reliability [service]"

**Kubernetes & Infrastructure-as-Code**
- CNCF landscape for ecosystem maturity
- Terraform Registry for provider modules
- Operator Hub for Kubernetes-specific tooling
- GitHub for real infrastructure examples
- Query pattern: "Kubernetes operator [tool]", "Terraform [provider]"

**Industry Adoption & Lock-In**
- StackShare for technology adoption patterns
- GitHub integration analysis (which cloud has best DevOps tooling)
- Job market analysis (which cloud skills are in demand)
- Migration case studies and exit cost discussions
- Query pattern: "cloud adoption trends", "vendor lock-in [service]"

## Analysis Frameworks

**TCO (Total Cost of Ownership) Matrix**
Compute across 3-year horizon:
- Compute: rate/hour × hours/month × 12 × 3
- Storage: $/GB/month × stored_GBs × 36
- Data transfer: $/GB × GB_transferred × 12 × 3
- Managed services premium: difference vs self-hosted
- Hidden costs: logging, monitoring, support fees

**Serverless Suitability Assessment**
- **Concurrency requirements**: Can you handle cold starts during traffic spikes?
- **Duration patterns**: Latency-sensitive tasks (< 1sec) vs background jobs?
- **Statefulness**: Stateless (good fit) vs stateful (harder with serverless)?
- **Cost sensitivity**: Pay-per-invocation aligns with usage or creates surprises?
- **Operational complexity**: Reduced ops burden vs harder debugging/monitoring?

**Kubernetes Readiness Checklist**
- Team expertise: Can you manage distributed systems?
- Workload characteristics: Stateless microservices (ideal) vs monoliths/state?
- Scaling patterns: Frequent scaling (Kubernetes advantage) vs static scale?
- Multi-tenancy needs: Does Kubernetes namespace isolation suffice?
- Cost: Is overhead of Kubernetes cluster + management worth it? (minimum ~3 nodes)

**Multi-Cloud Portability Assessment**
- Core workload portability: If I rebuild, how much code changes?
- Data portability: Can I export and re-import data in reasonable time/cost?
- Tool standardization: Docker + Kubernetes + Terraform minimize lock-in
- Managed service dependency: Each proprietary service increases lock-in cost
- Escape hatch: Is it feasible to move in emergency? (not just theoretically)

**Region & Compliance Strategy**
- Data residency: Where must data legally exist?
- Provider coverage: Can you serve all target geographies?
- Redundancy: Do you need multi-region failover?
- Latency budget: Can you tolerate region-to-region hops?
- Compliance complexity: Does region choice affect compliance burden?

## Output Format Templates

### Cloud Architecture Recommendation
```
Workload: [application type, scale]
Recommended Provider: [AWS/GCP/Azure]
Architecture: [compute, storage, networking approach]

Cost Estimate: [monthly at target scale]
Comparison: [vs alternatives, cost sensitivity analysis]
Scaling Capacity: [max workload size before redesign]
Lock-in Risk: [vendor-specific services used, switching difficulty]
Operational Burden: [team size, monitoring, updates]
```

### Serverless vs Container Decision
```
Use Case: [specific workload]
Recommended Approach: [serverless/Kubernetes/VMs]
Rationale: [cost, latency, operations tradeoffs]

Cold Start Impact: [P99 latency if applicable]
Scaling Behavior: [how does it handle traffic spikes?]
Cost Analysis: [monthly estimate for expected traffic]
Operational Requirements: [team skills, monitoring]
Migration Path: [if requirements change later]
```

### Cost Optimization Analysis
```
Current Setup: [description of infrastructure]
Current Spend: [$X/month]
Optimization Opportunities: [specific changes]

Quick Wins: [0-1 week effort, X% savings]
Medium Term: [1-3 month effort, X% savings]
Long Term: [architectural changes, X% savings]
Implementation Priority: [which to do first]
```

### Multi-Cloud Strategy Document
```
Core Workloads: [applications, data flow]
Provider Selection: [primary and secondary]
Portability Approach: [Docker/K8s/Terraform]

Lock-In Assessment: [which services bind you to provider]
Switching Costs: [effort and time to migrate]
Disaster Recovery: [failover procedure, RTO/RPO]
Monitoring & Ops: [centralized observability strategy]
```

## Key Metrics to Always Collect

For any cloud decision, quantify:
1. **Cost**: Compute, storage, data transfer, managed service premiums
2. **Performance**: Latency P50/P99, throughput capacity, cold start time
3. **Reliability**: Service SLA, historical uptime, incident frequency
4. **Scalability**: Min/max instance counts, burst capacity, rate limits
5. **Operational overhead**: Tools needed, team size, monitoring complexity
6. **Vendor lock-in**: Proprietary services used, data exit procedures

## Computational Workflows

**Pre-built Analysis Scripts**
- `tco_calculator.py` — Compute 3-year total cost of ownership across AWS/GCP/Azure using pandas with compute/storage/transfer cost models
- `serverless_cost_projector.py` — Model Lambda/Cloud Functions costs across invocation frequency distributions using scipy
- `multi_region_latency_simulator.py` — Predict regional latency distributions and data transfer costs with numpy arrays
- `scaling_capacity_analyzer.py` — Forecast infrastructure scaling curves to identify when redesign needed using curve_fit

**Dynamic Computation Examples**
- When comparing cloud providers, run TCO calculation across multiple usage scenarios (50%, 100%, 200% of projected volume)
- When evaluating serverless, simulate monthly cost across invocation distributions to identify cost surprises
- When planning multi-region, compute cumulative latency and bandwidth costs for different data flow patterns

**Output Artifacts**
- TCO comparison tables (rows: providers, columns: compute/storage/transfer/managed service costs)
- Cost sensitivity tornado chart (showing which cost drivers matter most)
- Scaling capacity heatmap (axes: request volume vs instance count, color: total cost)
- Mermaid swimlane diagram showing architecture decision points (serverless vs containers vs VMs)
- LaTeX formula: TCO = (compute_rate * hours/month * 36) + (storage * GB * 36) + (egress * transfer_GB * 12 * 3)

## References

Load from `references/` directory:
- `cloud-pricing-2024.md` — detailed cost comparisons and hidden fees
- `serverless-performance-analysis.md` — cold start patterns and optimization
- `kubernetes-operational-guide.md` — cluster setup, scaling, updates
- `multi-cloud-patterns.md` — workload distribution and failover strategies
- `data-transfer-optimization.md` — egress costs and architectural implications

## Common Pitfalls to Avoid

- **Price list confusion**: Published rates ≠ your actual bill (discounts, free tier, underutilization)
- **Cold start surprise**: Serverless feels instant until 10x traffic spike reveals 5-second latency
- **Kubernetes complexity**: "Just use K8s" when workload doesn't need it wastes ops time
- **Data transfer shock**: Inter-region replication costs hidden until production traffic hits
- **Managed service premium**: Fully managed databases cost 2-3x self-hosted; factor in ops overhead
- **Compliance overconfidence**: FedRAMP certification doesn't guarantee your app is compliant

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~cloud**: Direct access to AWS, GCP, Azure pricing APIs and service documentation
- **~~monitoring**: Observability tools for cost tracking, performance analysis, capacity planning
- **~~source control**: Infrastructure-as-code repositories showing real Terraform and CloudFormation patterns
- **~~web research**: Real-time pricing updates, region availability status, provider blog announcements

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
