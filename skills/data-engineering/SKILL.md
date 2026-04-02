---
name: Data Engineering Research
description: >
  Deep analysis of ETL/ELT architectures, streaming systems, lakehouse patterns, data governance, dbt, Spark, Kafka.
  Answer "data pipeline for", "ETL tool comparison", "streaming vs batch", "data platform" questions.
  Evaluate throughput, latency, cost at scale, schema evolution, and ecosystem completeness.
  Critical for data infrastructure design and modern analytics architecture.
---

# Data Engineering Research Domain

## Overview

Data engineering research synthesizes architectural patterns, tool ecosystems, and operational tradeoffs for moving, transforming, and serving data at scale. The field has fragmented into specialized sub-domains: batch ETL (Spark, dbt), real-time streaming (Kafka, Flink), and lakehouse architectures combining both.

Effective research here means understanding: which tools solve batch transformations optimally vs real-time ingest? How do schema evolution and data quality fit into architectural decisions? What are the hidden operational costs of each pattern?

## Key Research Dimensions

**Data Movement Patterns**
- Batch ETL: scheduled extraction, transformation, loading
- ELT: load raw, transform in-place (modern cloud paradigm)
- Streaming: continuous ingestion with sub-second latency
- Hybrid: batch backbone with real-time overlays
- Change data capture (CDC): capturing source system changes

**Storage & Lakehouse Architecture**
- Data lake: schema-on-read, Parquet/Iceberg/Delta Lake formats
- Data warehouse: structured, optimized for analytics queries
- Lakehouse: combining lake's schema flexibility with warehouse's performance
- Metadata layers: Apache Hudi, Apache Iceberg, Delta Lake format wars
- Iceberg advantages: ACID transactions, time-travel, hidden partitioning

**Processing Frameworks**
- Batch: Apache Spark (distributed), dbt (SQL-first), Airflow (orchestration)
- Streaming: Apache Kafka, Apache Flink, RabbitMQ, Kinesis
- Serverless: Snowflake, BigQuery, Redshift Spectrum (query, not process)
- Stateful processing: joining streams, windowing, aggregations
- Cost profiles: compute hours vs API calls vs managed service premiums

**Data Quality & Governance**
- Schema validation: Avro, Protobuf, JSON Schema
- Data quality frameworks: Great Expectations, dbt tests, custom validators
- Lineage tracking: understanding data flow and transformations
- PII handling: detection, masking, encryption
- Governance tools: Atlas, Collibra, enterprise data catalogs

**Performance & Scale**
- Throughput: records/sec that can be sustained
- Latency: P50/P99 time from source change to query-ready
- Cost: $/GB stored, $/query, $/compute-hour
- Query optimization: partitioning strategy, materialization decisions
- Scaling characteristics: linear or step-function changes?

## Data Sources & Query Methods

**Tool Benchmarking & Comparisons**
- Apache Spark benchmarking guides and TPC-DS results
- dbt performance documentation and real user benchmarks
- Airflow vs Prefect vs Dagster community discussions
- StackShare for tool adoption trends
- Query pattern: "ETL tool comparison", "dbt vs [alternative]"

**Architectural Patterns**
- Blogs from major data practitioners (Uber, Airbnb, Stripe, Netflix)
- dbt best practices documentation
- Apache Foundation project documentation
- Cloud provider patterns (Snowflake, BigQuery, Redshift documentation)
- Query pattern: "data lakehouse pattern", "streaming architecture"

**Performance & Operational Data**
- Community benchmarks (TPC-H, TPC-DS results)
- GitHub issues revealing real-world scaling challenges
- Operational metrics from data engineering communities
- Query pattern: "Spark performance tuning", "Kafka throughput"

**Ecosystem & Tooling**
- Apache Software Foundation project health (commits, community)
- GitHub stars and maintenance status
- Conference talks (Strata, DataWorks, Data Council)
- Job market (which tools are employers seeking)
- Query pattern: "data engineering stack 2024", "tool adoption trends"

**Cost Analysis**
- Provider pricing pages with calculators
- Real-world cost case studies
- Cloud data warehouse cost comparisons
- Query pattern: "cost comparison [platform]", "storage cost [format]"

## Analysis Frameworks

**Tool Selection Matrix** (for ETL/streaming)
- **Latency**: Batch (hours) vs streaming (ms) requirements
- **Complexity**: SQL-only (dbt) vs code-first (Spark) vs low-code
- **Ecosystem**: Available integrations, transforms, monitoring
- **Operations**: Team expertise, training burden, support available
- **Cost**: Compute charges, storage, API calls at scale

**Data Quality Strategy**
- **Schema validation**: Enforce at ingestion or fail fast?
- **Testing**: Unit (dbt tests), integration (end-to-end), production validation
- **Monitoring**: Anomaly detection on data freshness, volume, distributions
- **Remediation**: How quickly can you fix and replay bad data?
- **Governance**: Who approves schema changes? How are breaking changes handled?

**Lakehouse vs Data Warehouse Decision**
- **Schema flexibility**: Do you need to ingest before understanding?
- **Query performance**: Is standard SQL enough or need optimizations?
- **Cost sensitivity**: Warehouse optimized compute vs lake's storage savings?
- **Tool integration**: Can you query the lake? (Iceberg/Delta Lake enable this)
- **Governance maturity**: Does your team need structure imposed?

**Streaming Readiness Assessment**
- **Throughput requirements**: Can Kafka/Kinesis keep up?
- **State management**: Do you need windowed aggregations or joins?
- **Latency sensitivity**: Minutes (Kafka + Spark micro-batches) vs sub-second (Flink)?
- **Failure recovery**: Can you afford to lose in-flight messages?
- **Complexity cost**: Is streaming complexity justified for use case?

**Cost Optimization Framework**
- **Compute**: Reserved instances, batch scheduling, right-sizing
- **Storage**: Data lifecycle (hot/warm/cold), format selection, deduplication
- **Queries**: Materialized views, caching, query optimization
- **Data transfer**: Regional affinity, compression, API rate limits
- **Hidden costs**: Monitoring, logging, metadata service fees

## Output Format Templates

### Data Pipeline Architecture Decision
```
Use Case: [analytics/ML/operational/etc.]
Data Volume: [GB/day, records/sec]
Latency SLA: [batch hours, streaming minutes, real-time seconds]

Recommended Architecture: [batch/streaming/hybrid]
Tool Stack: [orchestrator, processing, storage, serving]
Estimated Cost: [$/month at target scale]
Scaling Capacity: [max volume before redesign]
Data Quality Approach: [validation strategy]
```

### ETL Tool Comparison
```
Tools Compared: [dbt, Spark, Airflow, etc.]
Use Case: [specific workload]

Tool A: [pros/cons, cost, ops burden]
Tool B: [pros/cons, cost, ops burden]
Tool C: [pros/cons, cost, ops burden]

Recommendation: [which tool wins and why]
Migration Path: [if changing from current tool]
```

### Lakehouse Implementation Guide
```
Current State: [existing data platform]
Target Lakehouse: [Iceberg/Delta/Hudi decision]

Schema Design: [partition strategy, format]
Ingestion Strategy: [batch/streaming/CDC]
Query Layer: [which tools query the lake?]
Data Quality: [testing, monitoring, remediation]
Migration Plan: [timeline, tools, staffing]
```

### Streaming System Design
```
Data Source: [type, volume, latency]
Requirements: [throughput, latency, exactly-once?]

Recommended System: [Kafka/Flink/etc.]
Topology: [producers, transformations, sinks]
State Management: [if needed]
Failure Handling: [recovery strategy]
Monitoring: [metrics to alert on]
Capacity: [max throughput, burst handling]
```

## Key Metrics to Always Collect

For data engineering decisions, track:
1. **Performance**: Throughput (records/sec), latency P50/P99, query time
2. **Cost**: $/GB stored, $/query, $/compute-hour, total monthly
3. **Reliability**: Data freshness, SLA uptime, recovery time from failures
4. **Data quality**: Validation rules, test pass rate, production incidents
5. **Scalability**: Data volume growth rate, query growth, processing time trend
6. **Operational burden**: Team size, on-call overhead, incident frequency

## Computational Workflows

**Pre-built Analysis Scripts**
- `pipeline_cost_analyzer.py` — Compute per-GB and per-query costs across batch/streaming/lakehouse approaches using pandas
- `throughput_latency_simulator.py` — Model data freshness vs compute cost tradeoff with numpy across architecture patterns
- `schema_evolution_impact_calculator.py` — Estimate cost of schema changes across Iceberg/Delta/Hudi with row count projections
- `storage_optimization_recommender.py` — Analyze storage format efficiency (Parquet compression ratios) and partitioning strategy impact

**Dynamic Computation Examples**
- When selecting ETL tool, compute total cost of ownership across dbt/Spark/Airflow for target data volume and latency SLA
- When designing lakehouse, run cost comparison across format choices (Iceberg vs Delta Lake) with growth scenarios
- When optimizing storage, calculate expected cost savings from partitioning strategy and compression using real data distributions

**Output Artifacts**
- Cost comparison matrix (rows: tools/architectures, columns: compute/storage/operations costs at different scales)
- Latency vs cost tradeoff scatter plot (axes: data freshness vs monthly cost, sized by data volume)
- Storage format efficiency bar chart (compression ratio and query speed comparison)
- Mermaid flowchart showing pipeline architecture selection (batch/streaming/hybrid decision tree)
- LaTeX formula: Total_Cost = (compute_hours * rate/hour * months) + (storage_GB * rate/GB/month) + (queries * rate/query)

## References

Load from `references/` directory:
- `etl-tool-landscape-2024.md` — detailed tool comparisons and feature matrices
- `spark-optimization-guide.md` — performance tuning and cost reduction
- `dbt-best-practices.md` — project structure, testing, deployment
- `streaming-patterns.md` — Kafka/Flink architectures and failure modes
- `lakehouse-format-comparison.md` — Iceberg vs Delta Lake technical details
- `cost-optimization-strategies.md` — reducing data platform spend

## Common Pitfalls to Avoid

- **Tool hype**: Kafka for everything feels good until you manage 10 clusters
- **Over-streaming**: Batch with hourly SLA costs less to operate than sub-second streaming
- **Schema assumptions**: "We'll just fix schema later" becomes technical debt quickly
- **Scaling blindness**: Tool works fine at 1GB/day until 10x growth hits month 6
- **Cost underestimation**: Managed services cheaper than self-hosted until you have 5 clusters
- **Data quality theater**: Tests that don't catch real problems; alert on actual anomalies
- **Governance gap**: Without data ownership, nobody maintains data quality

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub repositories with ETL/streaming implementations, infrastructure patterns
- **~~cloud**: Cloud data warehouse pricing, API access, managed service availability
- **~~monitoring**: Real-time data quality monitoring, pipeline performance tracking
- **~~web research**: Tool benchmarks, architecture patterns, cost comparisons

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
