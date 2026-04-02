---
name: architecture-patterns
description: >
  System design patterns including microservices, event-driven architecture, CQRS
  (Command Query Responsibility Segregation), hexagonal architecture, anti-patterns,
  migration strategies (strangler fig, parallel run, blue-green). Triggered by "system design",
  "architecture pattern", "monolith to microservices", "CQRS", "event-driven". Outputs architecture
  recommendation with trade-off analysis and implementation roadmap.
---

## Overview

This skill guides architectural decisions from greenfield design to legacy modernization. It covers patterns that address scalability, maintainability, testability, and organizational alignment challenges.

## System Design Patterns

### Monolithic Architecture
- **Structure**: Single codebase, single deployment unit, shared database
- **Strengths**: Simple to develop initially; single transaction; no network latency
- **Weaknesses**: Hard to scale (must scale entire app); deployment risk (one bug affects all); team coupling
- **Scaling**: Horizontal scaling requires stateless design; database becomes bottleneck
- **Organizational fit**: Small teams (<20 engineers) starting out
- **Example**: Early-stage startups, single-product companies

**Anti-patterns in Monoliths**:
- God classes (1000+ line methods)
- Circular dependencies (module A depends on B, B depends on A)
- Shared mutable state (global variables, singleton singletons)
- Mixed concerns (business logic + infrastructure code)

### Microservices Architecture
- **Structure**: Multiple services, separate codebases, service-to-service communication (HTTP/gRPC)
- **Strengths**: Independent scaling; team autonomy; fault isolation; technology diversity
- **Weaknesses**: Distributed systems complexity (eventual consistency, network latency); operational overhead; debugging difficulty
- **Organizational fit**: Large teams (50+ engineers), multiple products, high scaling demands
- **Example**: Netflix, Uber, Spotify, PayPal

**Trade-offs**:
- **Scaling**: Service X gets 10K QPS; scale it independently (cost efficient)
- **Failure**: Service A outage doesn't bring down B (fault isolation)
- **Development**: Teams can use different languages (Go for high-throughput, Python for ML)
- **Operational**: Each service needs observability, monitoring, testing, deployment pipeline

**Implementation Patterns**:
- **API Gateway**: Single entry point; routing, rate limiting, auth centralized
- **Service Discovery**: Kubernetes DNS, Consul, Eureka for dynamic service location
- **Load Balancing**: Within service (multiple replicas) and across regions
- **Circuit Breaker**: Prevent cascading failures (timeout, fallback)

### Event-Driven Architecture
- **Structure**: Services communicate via events (published to message broker)
- **Strengths**: Decoupled; asynchronous; scalable to high throughput
- **Weaknesses**: Eventual consistency complexity; distributed tracing harder; testing complexity
- **Use Cases**: High-throughput systems (Kafka 1M msgs/sec), real-time analytics, log aggregation
- **Example**: Financial trading, IoT data pipelines, real-time notifications

**Event Flow**:
1. Service A (e.g., order creation) publishes "OrderCreated" event
2. Broker (Kafka, RabbitMQ) persists event
3. Services B, C, D consume event asynchronously
4. B updates inventory; C triggers payment; D sends notification
5. All happen independently; no blocking on A

**Anti-patterns**:
- **Synchronous RPC over events**: Publishing events but treating them as synchronous (defeats purpose)
- **Event explosion**: Hundreds of event types with unclear boundaries
- **Ordering assumptions**: Assuming events processed in order (breaks with async)
- **Event versioning**: Publishing events without backwards-compatible schema

### CQRS (Command Query Responsibility Segregation)
- **Principle**: Separate read and write models
- **Structure**:
  - **Command side**: Validates, updates write model (source of truth)
  - **Query side**: Read-optimized view; eventually consistent
  - **Event stream**: Command → event → Query side update
- **Strengths**: Optimize reads/writes independently; complex queries fast; audit trail via events
- **Weaknesses**: Consistency complexity; duplicate data; learning curve
- **Use Cases**: High-traffic systems with complex queries, event sourcing, audit requirements
- **Example**: Event stores (EventStoreDB), audit systems

**Implementation**:
```
Command: AddInventory(item_id, quantity)
  → Validation on write model
  → Event: InventoryIncremented(item_id, quantity, timestamp)
  → Published to subscribers

Query side updates:
  Read model: inventory_item { id, quantity, updated_at }
  → Used for "get inventory" queries (fast, denormalized)
```

### Hexagonal Architecture (Ports & Adapters)
- **Principle**: Isolate business logic from infrastructure
- **Structure**:
  - **Core**: Business logic (domain model, use cases)
  - **Ports**: Interfaces (contracts) the core exposes
  - **Adapters**: Implementations for specific technologies (REST, gRPC, database, email)
- **Strengths**: Testable (mock adapters); technology agnostic; decoupled dependencies
- **Weaknesses**: More abstractions; learning curve; initial complexity
- **Example**: Pluggable architecture (swap PostgreSQL for MongoDB without changing business logic)

### Strangler Fig Pattern (Migration)
- **Principle**: Incrementally replace legacy system without big-bang rewrite
- **Process**:
  1. New service alongside legacy (both running)
  2. Gradually route traffic to new service (5% → 50% → 100%)
  3. Legacy decommissioned only after new proven stable
- **Strengths**: Reversible; low risk; can rollback; phased team transition
- **Disadvantages**: Temporary duplicated code; dual maintenance; slower than big-bang
- **Timeline**: 6-18 months typical for medium monolith
- **Example**: Shopify's gradual Ruby on Rails → service-oriented evolution

### Blue-Green Deployment Pattern
- **Principle**: Two identical production environments; switch traffic instantly
- **Blue environment**: Current production
- **Green environment**: New version being tested
- **Switch**: Load balancer routes 100% traffic to Green (instant; zero-downtime)
- **Rollback**: Route back to Blue if issues detected
- **Strengths**: Zero downtime; instant rollback; full environment testing
- **Weaknesses**: Requires 2x infrastructure; database migration complexity (if schema changes)
- **Cost**: 2x compute; offset by reduced downtime risk

### Canary Deployment Pattern
- **Principle**: Route small % of traffic to new version; monitor; expand if healthy
- **Process**:
  1. Deploy new version to 5% of servers
  2. Monitor metrics (error rate, latency); compare to baseline
  3. If healthy: expand to 25% → 50% → 100%
  4. If unhealthy: rollback the 5% immediately
- **Strengths**: Risk mitigation; real-world testing; gradual rollout
- **Disadvantages**: Slower than blue-green; complex monitoring required
- **Example**: Netflix canary analysis; continuous deployment pipelines

## Anti-Patterns to Avoid

| Anti-Pattern | Symptom | Remedy |
|---|---|---|
| Distributed monolith | Microservices with shared database | Service-per-DB; async communication |
| God service | One microservice doing everything | Domain-driven design; split by domain |
| Chatty services | Service A calls B calls C (3 hops) | Event-driven; async APIs |
| Eventual consistency everywhere | Lack of strong consistency requirements | Use distributed transactions where critical (SAGA pattern) |
| Technology sprawl | 10 languages, 15 frameworks | Define tech radar; governance |

## Common Architecture Patterns by Use Case

### High-Traffic Web Application
```
→ API Gateway (rate limit, auth)
→ Microservices (order, payment, inventory) + CQRS read models
→ Event stream (Kafka) for async processing
→ Cache layer (Redis) for fast reads
→ CDN (Cloudflare) for static assets
```

### Real-Time Analytics
```
→ Event source (IoT devices, application logs)
→ Message broker (Kafka, Kinesis) for high throughput
→ Stream processing (Flink, Spark) for aggregations
→ Time-series DB (InfluxDB) for metrics storage
→ Visualization (Grafana) for dashboards
```

### E-Commerce Platform
```
→ Product catalog (read-heavy) with caching
→ Shopping cart (session-based, Redis)
→ Order service with transaction guarantees (SAGA pattern)
→ Payment integration (external API with circuit breaker)
→ Notification service (async, event-driven)
→ Inventory (eventual consistency across regions)
```

## When to Use This Skill

- **Greenfield architecture**: Designing new system from scratch
- **Monolith migration**: Planning strangler fig transition
- **Scaling bottleneck**: System hitting limits; need architectural redesign
- **Organizational restructuring**: Teams growing; need new org/architecture alignment
- **Technology evaluation**: Should we use event-driven? CQRS? Microservices?
- **Post-mortems**: Architectural issues contributed to incident; need redesign
- **Code review**: Design patterns for consistency and quality

## Output Examples

- Architecture diagram (services, databases, event streams, deployment topology)
- Pattern recommendation with trade-off analysis (pros/cons per pattern)
- Implementation roadmap (phases, timeline, team allocation)
- Organizational structure alignment (teams per service, ownership model)
- Technology stack specification (languages, frameworks, datastores per service)
- Migration strategy (if applicable): strangler fig timeline, phase gates

## Computational Workflows

### Pre-built Analysis Scripts

**architecture_pattern_recommender.py**: Maps system requirements (QPS target, team size, consistency model) to patterns (monolith, microservices, event-driven, CQRS). Inputs: scale, latency SLAs, team structure, change velocity. Outputs: recommended pattern with trade-off analysis, implementation complexity score, team capability gaps.

**migration_cost_estimator.py**: Models strangler fig pattern cost. Input: monolith size (SLOC, complexity), target pattern, team size. Outputs: extraction timeline per microservice (weeks estimate), parallel run cost (dual infrastructure), risk assessment (rollback scenarios), 3-year TCO comparison.

**bottleneck_identifier.py**: Takes system metrics (QPS, latency, error rate). Simulates: database bottleneck (query load), cache bottleneck (hit rate), gateway bottleneck (connection pooling). Outputs: primary bottleneck, scaling recommendation (vertical vs horizontal), cost of scaling, headroom calculation.

**consistency_model_trade_off_analyzer.py**: Compares strong consistency vs eventual consistency for business operations (payments, inventory, orders). Inputs: consistency requirement, latency tolerance, conflict rate. Outputs: pattern trade-offs (SAGA vs 2PC), complexity vs reliability, cost estimate (extra monitoring, conflict resolution).

### Dynamic Computation Examples

1. **Monolith-to-Microservices Migration Roadmap**: Input: current monolith (1M SLOC, 50-engineer team), target scale (100K QPS). Compute: domain boundaries for service extraction, migration sequence (start with high-change domains), parallel run duration. Output: 18-month timeline with phase gates, team allocation, risk checkpoints.

2. **Event-Driven Architecture ROI Calculator**: Input: current throughput (10K req/sec), processing latency (200ms), event latency target (50ms). Model: event streaming (Kafka), async processing, eventual consistency cost (conflict resolution). Output: implementation cost (infrastructure, code refactoring), payback period (when throughput improvement ROI breaks even).

3. **Canary Deployment Risk Simulator**: Input: deployment frequency (daily), feature complexity (high-risk vs low-risk), error detection latency (5 min). Simulate: % deployments catching bugs in canary phase, rollback speed. Output: recommended canary percentage (5% vs 25%), monitoring requirements, incident response time.

### Output Artifacts

- **Architecture Recommendation**: Pattern selection (monolith, microservices, event-driven, CQRS, hybrid) with trade-off analysis, organizational alignment, technology stack selection
- **Migration Roadmap Gantt Chart**: Phase timeline (0-3 months domain extraction, 3-6 months parallel run, 6-12 months deprecation), team allocation, key deliverables, risk gates
- **Bottleneck Analysis Report**: Current bottleneck identified with data (DB p99 latency, cache hit ratio, gateway QPS), scaling options (vertical vs horizontal), cost estimates, headroom projection
- **Deployment Strategy Specification**: Blue-green vs canary vs rolling, monitoring checklist, rollback triggers, incident response playbook, deployment frequency recommendation

---

**Supercharged By**: System design tools (C4 models, ArchiMate), infrastructure code (Terraform for deployment), container orchestration (Kubernetes for operations), observability platforms (distributed tracing for debugging), chaos engineering for resilience testing

## Data Sources

| Connector | Purpose |
|-----------|---------|
| ~~web research | Architecture blogs, conference talks, pattern catalogs |
| ~~source control | Reference implementations, architecture decision records |
| ~~research | Academic papers on distributed systems, software architecture |
