---
name: programming-languages
description: >
  Compares programming language ecosystems including design philosophy, type systems,
  memory models, compiler architecture, and WASM capabilities. Covers Rust, Go, Swift,
  Kotlin, Zig, Python, TypeScript. Triggered by "Rust vs Go", "language comparison",
  "type system", "compiler optimization", "WASM". Evaluates performance, safety guarantees,
  learning curve, ecosystem maturity, job market demand.
---

## Overview

This skill provides comparative analysis of modern programming languages and their ecosystems. It guides teams in language selection based on performance requirements, safety guarantees, team expertise, and long-term ecosystem viability.

## Language Profiles

### Rust
- **Type System**: Ownership + borrowing, compile-time memory safety without garbage collection
- **Performance**: Native code, zero-cost abstractions, microsecond latencies
- **Ecosystem**: Cargo (package manager), growing production use (Linux kernel, AWS Lambda)
- **Strengths**: Memory safety, concurrency without data races, systems programming
- **Trade-offs**: Steep learning curve (borrow checker), longer compilation times
- **Job Market**: Rising demand, especially infrastructure/systems roles
- **WASM**: Excellent support via wasm-pack, popular for browser apps (Yew framework)

### Go
- **Type System**: Structural typing, simple interface model, built-in concurrency primitives (goroutines, channels)
- **Performance**: Fast compilation, single binary deployment, competitive runtime (GC latency ~1ms)
- **Ecosystem**: Strong in infrastructure (Kubernetes, Docker, Terraform), DevOps tooling
- **Strengths**: Simple syntax, rapid development, cloud-native focus
- **Trade-offs**: Limited generics (pre-1.18), verbose error handling, no inheritance
- **Job Market**: High demand in DevOps, cloud, infrastructure roles
- **Production**: Standard for microservices, CLIs, observability tools

### Swift
- **Type System**: Strong typing, generics, protocol-oriented design
- **Performance**: Native performance (similar to C++), optimized for Apple platforms
- **Ecosystem**: Apple frameworks (UIKit, SwiftUI), growing server-side adoption
- **Strengths**: iOS/macOS development, modern syntax, memory safety (ARC)
- **Trade-offs**: Primarily Apple ecosystem, limited Android/web presence
- **Job Market**: Strong for mobile development; limited infrastructure roles
- **Server-Side**: Swift for Server gaining traction (server frameworks emerging)

### Kotlin
- **Type System**: Full interop with Java, null safety built-in, coroutines for concurrency
- **Performance**: JVM-based, competitive with Java, lower startup latency than Go
- **Ecosystem**: Android development (official language since 2017), Java library compatibility
- **Strengths**: Java interop, concise syntax, mobile-first design
- **Trade-ops**: Tied to JVM, larger runtime footprint
- **Job Market**: High in Android/mobile; moderate in backend
- **Android**: Industry standard for modern Android apps

### Zig
- **Type System**: Comptime programming, optional type checking
- **Performance**: Compiles to machine code, no hidden allocation, C-like control
- **Ecosystem**: Still pre-1.0, growing but smaller community
- **Strengths**: Systems programming alternative to C/Rust, manual control, learning language
- **Trade-offs**: Immature ecosystem, smaller job market
- **Use Case**: C replacement, embedded systems, performance-critical code
- **Adoption**: GitHub, etc exploring as build-system language

### Python
- **Type System**: Duck typing with optional static type hints (mypy ecosystem)
- **Performance**: Interpreted, slower than compiled languages; async/await for concurrency
- **Ecosystem**: Largest package repository (PyPI), dominant in ML/data science
- **Strengths**: Rapid development, scientific computing (NumPy, PyTorch), vast libraries
- **Trade-offs**: Runtime performance limitations, GIL bottleneck in multi-threading
- **Job Market**: Very high demand across domains (ML, data, web, automation)
- **Web**: Django/FastAPI for backend; growing adoption in systems tools

### TypeScript
- **Type System**: Structural typing, generics, gradual typing
- **Performance**: Transpiles to JavaScript, V8 runtime (Node.js), performance parity with modern JS
- **Ecosystem**: Node.js + npm, same package ecosystem as JavaScript
- **Strengths**: Full-stack web development, rapid tooling ecosystem
- **Trade-offs**: Runtime errors still possible (types erased), dependency on JavaScript runtime
- **Job Market**: Highest demand for web/full-stack roles
- **Ecosystem Growth**: Framework maturity (Next.js, Nuxt), edge computing expansion

## Evaluation Dimensions

**Performance**: Latency (tail p99), throughput, memory footprint; language vs algorithm choice

**Memory Safety**: Compile-time (Rust), runtime GC (Go, Java), manual (C/Zig)

**Concurrency Model**: Green threads (Go goroutines), async/await (Rust, Python), traditional threads

**Learning Curve**: Steep (Rust, C++) → moderate (Go) → shallow (Python, JavaScript)

**Ecosystem Maturity**: Standardized libraries, package quality, production track record

**Compilation Model**: Ahead-of-time (Rust, Go) vs interpreted (Python) vs JIT (Java)

**Type System Power**: Rust's ownership > Go's interfaces > Python's duck typing

**Job Market Demand**: TypeScript/Python (broadest) → Go/Swift → Rust (growing) → Zig (emerging)

## WASM Considerations

| Language | WASM Support | Use Case | Maturity |
|----------|---|---|---|
| Rust | Excellent (wasm-pack) | Browser apps, edge compute | Production |
| Go | Good (TinyGo) | Embedded WASM | Experimental |
| Swift | Emerging | Cross-platform native | Early |
| TypeScript | Native | JavaScript in browser already | N/A |
| Python | Experimental (PyScript, Pyodide) | Data science in browser | Emerging |

## When to Use This Skill

- **Choosing primary language** for new system/team
- **Polyglot architecture decisions**: when to introduce multiple languages
- **Performance-critical system**: Rust vs Go vs C++ trade-off analysis
- **Ecosystem evaluation**: library maturity, dependency risk assessment
- **Migration strategy**: legacy language → modern language roadmap
- **Team skill assessment**: hiring demand, training investment
- **WASM feasibility**: browser/edge deployment of existing code

## Output Examples

- Language selection matrix (performance, safety, ecosystem, learning curve)
- Ecosystem health report (dependency quality, maintenance, security)
- Job market analysis (salary trends, hiring demand by language)
- Migration playbook (incremental adoption, interop strategies)
- WASM feasibility assessment for legacy codebases

## Computational Workflows

### Pre-built Analysis Scripts

**language_ecosystem_scorer.py**: Analyzes GitHub language distribution, npm/PyPI package quality (security audit score via Snyk), dependency freshness. Outputs: ecosystem health score (1-10), risk factors (outdated dependencies, unmaintained packages), long-term viability assessment.

**performance_benchmark_parser.py**: Parses benchmark results (TechEmpower, StackBlitz) for Rust, Go, TypeScript, Python across throughput and latency. Generates comparison charts (request/sec, latency percentiles) by framework and runtime.

**job_market_analyzer.py**: Queries job boards (Indeed API, LinkedIn) for "Rust engineer", "Go developer" postings. Tracks: salary trends over time, hiring volume, required experience, geographic hotspots. Outputs: market demand forecast, shortage indicators.

**wasm_feasibility_assessor.py**: Takes existing codebase (language, dependencies) and assesses WASM compatibility. Inputs: code complexity, library dependencies, performance requirements. Outputs: WASM viability score, refactoring effort estimate, use case alignment (browser, edge, serverless).

### Dynamic Computation Examples

1. **Language Adoption ROI Calculator**: Given team size, language choice, typical project duration. Compute: productivity impact (lines/day), learning curve cost, hiring ease, long-term maintenance burden. Compare 5-year TCO across language choices.

2. **Type System Safety vs Productivity Trade-off**: Input workload (real-time systems, CRUD web app, ML pipeline). Score each language on: type safety (compile-time guarantees), development velocity (lines/feature/day), runtime safety. Output: recommendation with confidence score.

3. **WASM Compilation & Performance Analyzer**: Input Rust/Go source, output WASM bundle size, startup time, runtime performance vs native. Identify optimization hotspots (heavy computation sections best suited for WASM).

### Output Artifacts

- **Language Selection Matrix**: Feature comparison (type system, concurrency model, ecosystem maturity, hiring availability) scored by your priority weights
- **Job Market Demand Chart**: Salary trends and hiring volume over 3 years for Rust, Go, TypeScript, Python
- **Ecosystem Health Dashboard**: Package quality scores, security vulnerability trends, community activity levels
- **WASM Readiness Report**: Compilation feasibility, bundle size projection, performance bounds, recommended refactoring priorities

---

**Supercharged By**: GitHub API (project trends, adoption patterns); Stack Overflow data (developer sentiment); GitHub Jobs/LinkedIn (market demand); language repository commit history (community health)

## Data Sources

| Connector | Purpose |
|-----------|---------|
| ~~web research | Language surveys (Stack Overflow, JetBrains), benchmark suites |
| ~~source control | Language repos, compiler projects, package registry stats |
| ~~research | PL research papers, language specification documents |
