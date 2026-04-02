---
name: observability
description: >
  Comprehensive observability strategy covering OpenTelemetry, distributed tracing, logging,
  metrics, APM (Application Performance Monitoring), and tools (Jaeger, Honeycomb, Grafana,
  eBPF). Triggered by "observability", "distributed tracing", "OpenTelemetry", "APM",
  "logging strategy", "metrics architecture". Evaluates data volume cost, query performance,
  correlation capability, agent overhead, and ecosystem maturity.
---

## Overview

This skill guides teams through observability architecture design, from instrumentation strategy to data pipeline optimization. It covers the three pillars (metrics, logs, traces) and their integration via OpenTelemetry, helping teams understand system behavior in production at scale.

## Core Concepts

### Three Pillars of Observability

**Metrics**: Aggregated, time-series data
- **Types**: Counters (total requests), gauges (CPU %), histograms (latency distribution), summaries
- **Dimensionality**: Labels (tags) enable slicing: error_rate{service="api", region="us-east"}
- **Retention**: 15-30 days typical (cost-driven); downsampling to 1-year archives
- **Query Language**: Prometheus PromQL, Grafana Loki LogQL
- **Cardinality Risk**: High-dimensional labels (e.g., user_id) explode metric storage

**Logs**: Structured events with context
- **Format**: JSON preferred (structured); legacy syslog/free-text harder to query
- **Volume**: Typically 50-100x metrics (storage cost); sampling strategies required at scale
- **Tools**: ELK (Elasticsearch-Kibana), Loki (Grafana), Splunk, Datadog
- **Challenge**: Correlation (matching logs to traces/metrics by trace_id)
- **Retention**: 24h-7d hot storage; archive to S3/GCS for compliance (cheaper)

**Traces**: Request-path visualization
- **Distributed Tracing**: Trace ID propagated across services, spans represent work units
- **Sampling**: 100% sampling = $$; 1-10% adaptive sampling balances cost/visibility
- **Use Case**: Understanding latency in microservices (which service is slow?)
- **Tools**: Jaeger, Zipkin, Tempo, Honeycomb, Datadog
- **Challenge**: Data explosion (10K requests/sec × 500B/trace = 5TB/day); sampling critical

## OpenTelemetry

### Standard & Ecosystem
- **Origin**: Merge of OpenCensus (Google) + OpenTracing (CNCF) in 2019
- **Status**: CNCF Incubating (2021), approaching 1.0 stable
- **Architecture**: Instrument → Collection → Export
- **Languages**: Python, Node.js, Go, Java, .NET, PHP, Ruby; SDKs mature

### Instrumentation Strategy

**Auto-Instrumentation**:
- Zero-code approach (Java agent, Python decorator injection)
- Catches standard libraries (HTTP clients, databases, message queues)
- Trade-off: Coverage vs control; may miss business logic

**Manual Instrumentation**:
- Explicit span creation for business metrics ("processing_order", "db_query_duration")
- Better signal-to-noise ratio but requires developer effort
- Best practice: Combine auto + manual for critical paths

### OpenTelemetry Collector
- **Pattern**: Separate sidecar/agent collecting, processing, exporting telemetry
- **Benefits**: Decouples app from backend; local buffering reduces network trips
- **Components**:
  - **Receivers**: OTLP (native), Prometheus, Jaeger, Syslog, etc.
  - **Processors**: Batch (efficiency), sampling (cost control), filtering (privacy)
  - **Exporters**: Jaeger, Prometheus, Datadog, Honeycomb, Grafana Loki
- **Deployment**: DaemonSet per node (Kubernetes), sidecar per pod (resource-heavy), centralized agent

### Cost Optimization via OpenTelemetry
- **Sampling**: Intelligent sampling (high-error traces = 100%, normal = 1%)
- **Filtering**: Drop low-value logs (e.g., health check logs)
- **Aggregation**: Pre-aggregate metrics at collector (reduce cardinality)
- **Retention Policies**: Hot (7d) + warm (30d) + cold archive (1y)

## Observability Tools

### Metrics: Prometheus/Grafana
- **Prometheus**: Pull-based scraping, time-series DB, 15s-5m resolution
- **Strengths**: Simple, no external dependency (self-contained binary), PromQL powerful
- **Scaling**: Single-node Prometheus ~1M metrics; sharding/remote-storage for 10M+
- **Grafana**: Visualization, dashboarding, alerting (via Alertmanager)
- **Limitations**: Not built for high-cardinality (unique values per label)

### Distributed Tracing

**Jaeger**:
- CNCF graduated project
- Collectors (receive spans) + Cassandra/Elasticsearch storage + UI
- Self-hosted complexity; scaling requires distributed backend
- Sampling built-in; Collector-to-backend buffering
- Free and open-source; growing production adoption

**Honeycomb**:
- SaaS platform, no ops burden
- **Strength**: High-cardinality trace exploration (query arbitrary fields)
- **Pricing**: Per GB ingested (~$0.50-$1.50/GB); 30-90 day retention
- **UX**: Drill-down interface, field autocompletion, query builder
- **Trade-off**: Vendor lock-in; cost sensitive to traffic volume

**Grafana Tempo**:
- CNCF incubating; log + trace correlation
- Object storage backend (S3, GCS) = cheap long-term storage
- Growing ecosystem; integrates with Prometheus/Loki
- Sampling required for cost efficiency

### Logging: Loki / ELK

**Grafana Loki**:
- Indexing strategy: Log stream labels only (not full-text), reduces storage 10-100x
- **Trade-off**: Less query flexibility than Elasticsearch
- **Cost**: ~$10-100/month for 100GB/day (on-prem hardware)
- **Advantage**: Runs on commodity hardware; integrates with Prometheus/Tempo

**ELK (Elasticsearch-Kibana)**:
- **Strength**: Full-text search, flexible mapping, mature ecosystem
- **Cost**: Storage-heavy; 5-10TB/day workloads = $10K+/month
- **Scaling**: 3-node cluster minimum production; data rebalancing during growth
- **Advantage**: Existing tooling, SIEM integrations, compliance features

**Splunk**:
- Enterprise-grade with SIEM features
- Premium pricing (~$5-15/GB/month); common cost complaint
- Strong for compliance (audit trails, regulatory)

### APM (Application Performance Monitoring)

**Datadog APM**:
- SaaS; integrates metrics, logs, traces, profiling
- **Strength**: Unified platform; automatic service discovery
- **Cost**: Spans + infrastructure metrics; complex pricing model
- **Market Leader**: 50%+ adoption in enterprise

**New Relic**:
- SaaS; good UI, large-scale production experience
- **Strength**: Pro-active alerting, anomaly detection
- **Cost**: Per GB ingested or per host; similar Datadog pricing

**Elastic APM**:
- Self-hosted option; integrates with ELK stack
- Lower cost than Datadog/New Relic at scale
- Smaller market share; ecosystem smaller

### eBPF for Observability

- **What**: Kernel instrumentation without modifying application code
- **Tools**: Pixie (auto-metrics), Grafana Phlare (profiling), Cilium (networking)
- **Strength**: Causal observability (system calls, TCP flows, CPU usage) without agent overhead
- **Use Case**: Detecting performance bottlenecks (syscall latency, disk I/O), network issues
- **Limitation**: Kernel version dependent (Linux 4.9+); complexity for developers

## Evaluation Dimensions

**Data Volume Cost**: Traces > Logs >> Metrics; sampling critical
- Realistic budget: $500-5000/month for 100M requests/day

**Query Performance**: How fast can insights be derived?
- Real-time alerts: Metrics + lightweight log sampling
- Root cause analysis: Traces + logs correlated by trace_id (Datadog strength)

**Cardinality Management**: Risk of unbounded label explosion
- Safe: service, environment, region, endpoint
- Risky: user_id, request_id (unbounded unique values)

**Agent Overhead**: CPU/memory impact on application
- Auto-instrumentation agents: 1-5% overhead
- Manual instrumentation: <1% overhead
- Sampling strategies reduce ingestion (half agent overhead)

**Ecosystem Maturity**: Tool stability, community, vendor support
- Prometheus/Grafana: Excellent (CNCF graduated)
- OpenTelemetry: Good (approaching 1.0)
- Jaeger: Good (CNCF graduated)
- Honeycomb: Good (SaaS quality)

## When to Use This Skill

- **Designing observability strategy** from scratch (pillars, tools, cost model)
- **Migration planning**: monolith metrics + logs → distributed tracing + OpenTelemetry
- **Cost optimization**: sampling strategies, retention policies, data pipeline efficiency
- **Bottleneck detection**: latency analysis in microservices via distributed traces
- **Compliance**: audit logging, data residency, GDPR data deletion
- **Incident response**: how to structure logs/traces for faster troubleshooting
- **Tool evaluation**: Prometheus vs New Relic vs Honeycomb vs Datadog TCO analysis
- **Cardinality management**: alerting on metric explosion (time-series monitoring)

## Output Examples

- Observability architecture diagram (instrumentation, collection, storage, visualization)
- OpenTelemetry implementation roadmap (auto-instrumentation phases, manual span addition)
- Sampling strategy (rules for adaptive sampling, cardinality limits)
- Retention & cost model (hot/warm/cold tiers, data size projections)
- Tool comparison matrix (cost, query performance, cardinality, learning curve)
- Incident response playbook (how logs/traces/metrics correlate for troubleshooting)

## Computational Workflows

### Pre-built Analysis Scripts

**telemetry_cost_projector.py**: Estimates observability cost at scale. Inputs: requests/day, trace sampling percentage, metrics cardinality, log volume (GB/day). Outputs: monthly cost by tool (Datadog, Honeycomb, Grafana stack), data retention tiers, optimization recommendations to stay within budget.

**sampling_strategy_optimizer.py**: Calculates optimal sampling rates for cost control. Given: error rate, latency percentile requirements (need to track p99 latencies), budget ceiling. Outputs: adaptive sampling rules (100% for errors, N% for success), cardinality limits by dimension, cost savings projection.

**cardinality_analyzer.py**: Scans metrics and logs for high-cardinality labels (user_id, request_id). Inputs: label patterns, unique value distribution. Outputs: storage explosion risk, recommended label removal/aggregation, estimated savings (GB/month).

**trace_correlation_validator.py**: Tests trace/log/metric correlation via trace_id. Inputs: sample of logs and traces. Validates: trace_id presence, timestamp alignment, service boundary crossing detection. Outputs: correlation completeness score, missing instrumentation points.

### Dynamic Computation Examples

1. **Observability Stack Cost vs Coverage Trade-off**: Input: system size (microservices count, QPS), coverage targets (% of requests traced). Compare: Prometheus/Grafana/Jaeger stack (self-hosted) vs managed (Datadog, Honeycomb). Output: 3-year TCO, complexity score, support burden estimate.

2. **Incident Root Cause Analysis Simulation**: Input: error spike event, latency baseline. Simulate tracing path (service A → B → C) to identify bottleneck. Compute: time-to-detection (alerting lag), time-to-diagnosis (query+analysis), time-to-fix (deployment). Recommend observability improvements.

3. **Agent Overhead & Sampling Impact**: Input: auto-instrumentation agent overhead (1-5%), sampling rate (1%), cardinality reduction (aggressive filtering). Compute: combined impact on application latency, data volume reduction, cost savings, visibility loss trade-offs.

### Output Artifacts

- **Observability Architecture Diagram**: Instrumentation strategy (auto vs manual), collection pattern (sidecar, daemonset, centralized), export targets, storage tiers (hot/warm/cold)
- **Cost Projection Model**: Monthly spend by platform and retention tier, data volume forecast at 1M/10M/100M requests/day
- **Sampling & Cardinality Strategy Table**: Sampling rules per service/error-type, high-cardinality label list with proposed remediation
- **Correlation & Debugging Playbook**: How to trace from metric alert to logs to traces, instrumentation gaps identified, time-to-diagnosis improvement roadmap

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~monitoring**: Observability platforms like Datadog, Honeycomb, Grafana for metrics/traces/logs
- **~~cloud**: Cloud infrastructure APIs for instrumentation, cost tracking, regional deployment
- **~~source control**: OpenTelemetry implementations, instrumentation libraries, configuration patterns

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: Cloud infrastructure (Kubernetes) for DaemonSet collector deployment; log aggregation (Fluentd, Logstash) for log collection; APM integrations (auto-discovery of services); alerting platforms (PagerDuty) for incident correlation
