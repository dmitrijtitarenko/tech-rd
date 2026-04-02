---
name: api-ecosystem
description: >
  Comprehensive analysis of API design paradigms including REST, GraphQL, gRPC, AsyncAPI,
  OpenAPI 3.1, API gateways, API marketplaces, and API security. Triggered by "API design",
  "GraphQL vs REST", "gRPC", "API gateway", "OpenAPI". Evaluates developer experience,
  performance, tooling quality, standards compliance, versioning strategy, and ecosystem maturity.
---

## Overview

This skill guides teams through API architecture decisions, from protocol selection to ecosystem governance. It covers the full API lifecycle: design, documentation, gateway infrastructure, security, versioning, and marketplace strategies.

## API Paradigms

### REST (Representational State Transfer)
- **Principle**: Resource-oriented, HTTP verbs (GET, POST, PUT, DELETE), stateless, cacheable
- **Standard**: HTTP/1.1, HTTP/2 support; OpenAPI 3.0+ documentation
- **Strengths**: Simplicity, browser-testable, excellent caching (CDN, HTTP layer), ubiquitous
- **Trade-offs**: Over/under-fetching (multiple requests or excess data), verbose payloads
- **Performance**: HTTP overhead acceptable for most use cases; multiplexing (HTTP/2) reduces latency
- **Adoption**: Dominant for public APIs, legacy systems
- **Versioning**: URL path (/v1/, /v2/) or header-based; content negotiation

### GraphQL
- **Principle**: Query language for APIs, client specifies exact data needs, strongly typed schema
- **Strengths**: No over/under-fetching, single request for related data, excellent DX (IDE support, introspection)
- **Trade-offs**: Query complexity (server cost), caching complexity (not HTTP-native), N+1 query risk
- **Performance**: Lower latency vs REST (fewer requests); server-side query cost unpredictable
- **Scaling**: Dataloaders prevent N+1; complexity analysis required for public APIs
- **Adoption**: Growing in high-traffic applications (GitHub, Shopify, Twitter), internal APIs
- **Versioning**: Additive-only (new fields/types); deprecation warnings in schema
- **Tooling**: Apollo Server, GraphQL Yoga, introspection, federation for microservices

### gRPC
- **Principle**: RPC framework using Protocol Buffers, HTTP/2, binary protocol
- **Strengths**: High performance (binary encoding, multiplexing), low latency, streaming support (duplex, server-push)
- **Trade-offs**: Complex browser support (gRPC-web shim), steeper DevEx (protobuf definitions)
- **Performance**: 10-100x faster than REST for high-throughput, microsecond latencies possible
- **Use Cases**: Microservices, real-time systems, high-frequency data pipelines, IoT
- **Adoption**: Kubernetes (etcd), Google Cloud, CNCF ecosystem, Envoy proxy native support
- **Maturity**: Production-grade; gRPC-web bridges HTTP limitation; gRPC-json bridge for REST clients

### AsyncAPI
- **Principle**: Message-driven APIs, pub-sub / event streaming (Kafka, RabbitMQ, WebSockets)
- **Standard**: Similar to OpenAPI but for asynchronous patterns, protocol-agnostic
- **Strengths**: Event sourcing, real-time communication, decoupled services
- **Trade-offs**: Eventual consistency, harder to debug, message ordering complexity
- **Adoption**: Event-driven architectures, streaming platforms (Kafka); growing ecosystem
- **Tooling**: AsyncAPI Studio (visual editor), code generation, lifecycle management

### OpenAPI 3.1
- **Standard**: RESTful API specification (formerly Swagger), YAML/JSON
- **Features**: Request/response schemas, authentication schemes, examples, webhooks
- **Tooling**: Swagger UI (interactive docs), code generation (OpenAPI Generator, Swagger Codegen)
- **Maturity**: Industry standard; wide tooling support; works with REST primarily
- **Automation**: API linting (Spectral), contract testing, documentation auto-generation

## API Infrastructure

### API Gateways
- **Functions**: Authentication, rate limiting, request routing, response transformation, logging
- **Products**: Kong, AWS API Gateway, Google Cloud Endpoints, Azure API Management, Tyk
- **Patterns**:
  - **Authentication Hub**: OAuth2, JWT validation, API key management
  - **Rate Limiting**: Per-user, per-IP, per-API quotas; sliding window algorithms
  - **Routing**: Versioning (path, header, subdomain), canary deployments
  - **Transformation**: Request/response rewriting, header injection, body transformation
- **Deployment**: Managed (cloud provider) vs self-hosted (Kong, Traefik)
- **Scaling**: Horizontal scalability critical; stateless design required
- **Cost**: Per-request pricing (AWS) vs fixed (self-hosted); request volume sensitivity

### API Versioning Strategies
- **URL Path**: /v1/, /v2/ (explicit, browser-friendly)
- **Header-Based**: Accept: application/vnd.company.v2+json (RESTful purist)
- **Subdomain**: api-v2.company.com (clean, CDN-cacheable)
- **Query Parameter**: ?api_version=2 (least common, poor cacheability)
- **Additive Evolution** (GraphQL): New fields/types; deprecation warnings

### API Security
- **Authentication**: OAuth2 (3-legged), API keys (simple), JWT (stateless), mTLS (service-to-service)
- **Authorization**: Scopes (OAuth), roles (RBAC), attributes (ABAC), resource-based (Amazon S3-style)
- **Rate Limiting**: Prevent abuse, DDoS protection, fair resource sharing
- **Input Validation**: Schema validation, SQL injection prevention, XSS defense
- **Data Protection**: Encryption in transit (TLS 1.3), at rest; GDPR/CCPA data handling
- **API Governance**: Audit logging, threat detection (suspicious patterns), WAF integration
- **Secret Management**: Rotation, vault integration (HashiCorp, AWS Secrets Manager)

### API Marketplaces & Developer Experience
- **Internal Marketplaces**: API discovery, lifecycle management, monetization (chargeback)
- **Public Marketplaces**: RapidAPI, Programmable Web integration, monetization at scale
- **Developer Portal**: Documentation (Swagger UI), SDKs, sandbox environments, community
- **Analytics**: Usage patterns, cost tracking, performance monitoring per consumer
- **Feedback Loop**: Breaking change notifications, versioning strategy, deprecation timeline

## Decision Framework

| Dimension | REST | GraphQL | gRPC | AsyncAPI |
|-----------|------|---------|------|----------|
| Latency | ~100ms | ~50ms | ~1-10ms | Event-driven |
| Browser Native | Excellent | Web only | gRPC-web | WebSocket/SSE |
| DevEx | Good | Excellent | Moderate | Good |
| Caching | HTTP native | Complex | Weak | N/A |
| Learning Curve | Shallow | Moderate | Steep | Moderate |
| Mobile Friendly | Yes | Yes (overhead) | Yes | Conditional |
| Real-time | Polling | Subscriptions | Server-push | Native |

## When to Use This Skill

- **Choosing primary API paradigm** (REST, GraphQL, gRPC) for new service
- **Gateway selection & deployment**: authentication, rate limiting, routing strategy
- **Versioning strategy**: managing breaking changes, deprecation timelines
- **Security audit**: authentication, authorization, secret management, compliance
- **Developer experience optimization**: documentation, tooling, SDK quality
- **Performance optimization**: latency reduction, throughput scaling
- **API marketplace evaluation**: internal/external API monetization, discovery
- **Real-time communication**: WebSocket vs Server-Sent Events vs gRPC vs message queues

## Output Examples

- API design review (paradigm selection, schema validation, security checklist)
- Gateway architecture diagram (routing rules, rate limiting, auth flows)
- API versioning roadmap (timeline, deprecation policy, migration guide)
- Security posture assessment (auth, rate limiting, data protection)
- Developer portal specification (SDK, documentation, sandbox, analytics)
- Microservices communication matrix (REST for public, gRPC for internal)

## Computational Workflows

### Pre-built Analysis Scripts

**api_paradigm_benchmarker.py**: Compares REST vs GraphQL vs gRPC latency and payload size. Inputs: query complexity (fields requested), network RTT, payload size. Outputs: end-to-end latency distribution, bandwidth consumed, optimal paradigm recommendation by use case.

**rate_limit_calculator.py**: Models rate limiting strategy (token bucket vs sliding window). Inputs: QPS, burst capacity, backend resources. Outputs: rate limit parameters (requests/second, burst multiplier) to maximize fairness and prevent abuse without starving legitimate users.

**api_versioning_migration_planner.py**: Tracks API version adoption across clients. Inputs: current client distribution, deprecation timeline. Outputs: estimated migration cost (support burden, dual-code maintenance), deprecation notification strategy, rollback risk assessment.

**openapi_compliance_validator.py**: Validates OpenAPI 3.1 specs against schema, tests code generation, checks security definitions. Outputs: compliance score, documentation completeness, missing authentication/rate limiting specifications.

### Dynamic Computation Examples

1. **Latency vs Feature Richness Trade-off**: Input: required features (filtering, sorting, pagination), target p99 latency (50ms vs 100ms). Compute: payload size per API paradigm, request count reduction via federation. Recommend: REST for simplicity, GraphQL for complex queries, gRPC for microsервices.

2. **API Gateway Throughput Model**: Input: QPS target, request size, authentication method. Compute: gateway resource requirement (CPU, memory), request processing overhead by pattern (auth, routing, transformation), cost/million requests across cloud providers.

3. **SDK Generation ROI**: Input: API endpoint count, supported languages (Python, Node, Go). Estimate: SDK development time via code generation vs hand-written, maintenance burden, developer experience improvement, adoption forecast.

### Output Artifacts

- **API Design Recommendation Matrix**: Feature completeness (filtering, real-time, complex queries), latency characteristics (p50, p95, p99), caching strategy by paradigm (REST, GraphQL, gRPC)
- **Versioning Strategy Roadmap**: Current API versions, client adoption distribution, deprecation timeline, support burden estimate
- **Gateway Architecture Diagram**: Entry point, rate limiting strategy (per-user, per-IP, per-endpoint), routing rules, transformation pipeline
- **Security Posture Assessment Table**: Authentication methods implemented, rate limiting coverage, input validation, OWASP compliance checklist

---

**Supercharged By**: API monitoring (Datadog, New Relic) for performance analytics; security scanning (Snyk, Checkmarx) for vulnerability detection; API mocking services (Prism, Mockoon) for testing; code generation tooling for SDK automation

## Data Sources

| Connector | Purpose |
|-----------|---------|
| ~~web research | API documentation, developer portals, industry reports |
| ~~source control | GitHub API repositories, SDK libraries, OpenAPI specs |
| ~~analytics | API usage metrics, adoption trends, rate limit data |
