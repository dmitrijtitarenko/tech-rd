---
name: database-technologies
description: >
  Evaluates and compares database systems across relational (Postgres, MySQL), NewSQL
  (CockroachDB, Vitess), vector databases (Pinecone, Weaviate, Milvus, Qdrant, pgvector),
  graph databases (Neo4j), time-series (InfluxDB, TimescaleDB), and document stores.
  Use this when choosing a database "for your workload", assessing "vector database" needs,
  "scaling database" solutions, or comparing "NewSQL vs traditional" options.
---

## Overview

This skill provides expert-level guidance on database selection and architecture, covering the full spectrum of modern database technologies. It helps teams make informed decisions about data persistence layers by evaluating performance characteristics, consistency models, scalability patterns, and operational overhead.

## Key Domains

### Relational Databases
- **PostgreSQL**: Advanced features (JSON, array types, extensions like pgvector for embeddings)
- **MySQL**: Performance optimizations, replication strategies, cloud variants (Aurora, PlanetScale)
- Trade-offs: mature ecosystems, ACID guarantees, standardized SQL

### NewSQL Databases
- **CockroachDB**: Distributed ACID transactions, geo-distribution, horizontal scaling
- **Vitess**: MySQL middleware for sharding, meta-routing, online schema changes
- **TiDB**: HTAP (hybrid transactional-analytical), multi-replica consistency
- When to consider: global applications, distributed transactions at scale

### Vector Databases
- **Pinecone**: Fully managed, serverless, metadata filtering
- **Weaviate**: Self-hosted flexibility, hybrid search (vector + semantic)
- **Milvus**: Open-source, high-throughput, CRUD operations
- **Qdrant**: Edge deployment, payload filtering, snapshot/backup
- **pgvector**: PostgreSQL extension, native SQL integration
- Use case trigger: "embedding storage", "semantic search", "RAG applications"

### Graph Databases
- **Neo4j**: Dominant player, ACID transactions, relationship querying at scale
- Pattern: Complex relationship traversals (recommendation engines, knowledge graphs)
- Scaling: Enterprise (cluster) vs community editions

### Time-Series Databases
- **InfluxDB**: Tag-based indexing, retention policies, downsampling
- **TimescaleDB**: PostgreSQL extension, query performance at scale
- **VictoriaMetrics**: Long-term storage efficiency, cardinality handling
- Trigger phrases: "metrics", "event streams", "time-based queries"

### Document Databases
- **MongoDB**: Schema flexibility, aggregation pipeline, sharding
- **Firestore/Firebase**: Real-time sync, mobile-friendly, managed
- Pattern: Semi-structured data, rapid iteration

## Decision Framework

**Query Performance**: Specialized databases (vector, time-series) outperform general-purpose for their domain

**Scalability**: Horizontal (sharding) vs vertical; managed services reduce operational overhead

**Consistency Models**: ACID (relational, NewSQL) vs eventual (NoSQL document stores)

**Managed vs Self-Hosted**: Managed options (Pinecone, Firestore) reduce operations; self-hosted (Milvus, Weaviate) offer control

**Cost**: Storage, compute, ingestion rates; FinOps analysis critical for high-volume workloads

**Integration**: Data movement pipelines, ETL tooling, native connector support

## When to Use This Skill

- **Choosing primary data store** for new systems
- **Migrating from legacy** database architectures
- **Scaling existing databases** to 10M+ QPS or multi-region
- **Adding specialized stores** (vector, time-series) to existing stack
- **Compliance analysis**: data residency, encryption, audit trails
- **Cost optimization**: right-sizing instances, storage tiers, retention policies

## Output Examples

- Database selection matrix (performance, cost, scalability comparison)
- Migration roadmap (data re-platforming, testing strategy)
- Scalability architecture with sharding/replication patterns
- Cost-to-throughput analysis by database type

## Computational Workflows

### Pre-built Analysis Scripts

**query_benchmark.py**: Parses pgbench or YCSB benchmark result files, extracts throughput, latency percentiles (p50, p95, p99), and generates comparison table across database configurations.

**index_performance.py**: Simulates B-tree vs LSM (Log-Structured Merge) trade-offs. Takes workload parameters (write ratio, read ratio, key distribution) and outputs: insert throughput, query latency, space amplification trade-off analysis.

**replication_lag_analyzer.py**: Models replication latency in multi-primary (CockroachDB, MySQL Group Replication) and primary-replica scenarios. Inputs: network RTT, transaction volume, schema size. Outputs: consistency window, failover impact matrix.

**vector_embedding_loader.py**: Loads embeddings, tests insert performance into Pinecone/Weaviate/Milvus via REST APIs, measures latency distribution, and outputs cost-per-million-vectors projection.

### Dynamic Computation Examples

1. **NewSQL Scaling Calculator**: Given transaction volume and data size, compute sharding strategy (hash-based vs range-based). Calculate hot-shard risk, rebalancing cost, and optimal shard count for target latency (p99 <100ms).

2. **Vector Database Cost Simulator**: Input: monthly embedding count, search QPS, storage retention. Output: TCO comparison table (Pinecone managed vs self-hosted Milvus). Consider: API calls, compute, storage tiers.

3. **Migration Impact Model**: For legacy-to-modern migration, estimate downtime windows, data validation overhead (checksums, sampling), and dual-write period (days needed for consistency verification).

### Output Artifacts

- **Database Selection Matrix**: Feature comparison (ACID, horizontal scale, query language, cost model) ranked by your workload priority weights
- **Performance Trade-off Chart**: Latency vs throughput scatter plot showing Postgres, CockroachDB, DynamoDB, Cassandra positioned by your access patterns
- **Replication Topology Diagram**: Primary-replica, multi-primary, or hybrid models with failure scenarios annotated
- **Cost Projection Table**: $/month by database type at 1M, 10M, 100M rows with realistic query patterns

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub repositories with database implementations, benchmarks, schema examples
- **~~cloud**: Managed database services, pricing information, performance characteristics
- **~~web research**: Real-world benchmark results, performance comparisons, best practices

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: Cloud infrastructure connectors (AWS, GCP, Azure) for managed database pricing; data engineering platforms (Databricks, Fivetran) for pipeline integration
