# Tech Radar Template

A technology radar is a visual representation of your organization's technology landscape. It categorizes technologies across four quadrants and four maturity rings, helping teams understand what to adopt, evaluate, retain, or retire.

## Structure

### Quadrants

1. **Languages & Frameworks** - Programming languages, web frameworks, mobile frameworks, runtime environments
2. **Tools** - Development tools, automation, monitoring, analytics, testing, deployment
3. **Platforms** - Cloud platforms, databases, infrastructure, container orchestration, messaging systems
4. **Techniques** - Methodologies, practices, patterns, architectural approaches, processes

### Rings (Maturity Levels)

1. **Adopt** - Ready for production use. Proven, mature, recommended as your default choice.
2. **Trial** - Worth exploring in non-critical projects. Good but still needs validation in your context.
3. **Assess** - Monitor and understand. Interesting but not yet proven enough for investment.
4. **Hold** - Minimize or discontinue. Legacy or problematic; phase out or maintain carefully.

## Entry Format

Each technology entry includes:

```
Technology Name | Quadrant | Ring | Movement | Rationale
```

**Movement indicators:**
- `new` - First appearance on radar
- `unchanged` - Same position as previous radar
- `moved-in` - Moved to higher maturity ring
- `moved-out` - Moved to lower maturity ring

## Example Entries

```markdown
| Technology | Quadrant | Ring | Movement | Rationale |
|------------|----------|------|----------|-----------|
| Python | Languages & Frameworks | Adopt | unchanged | Standard language for backend services. Mature ecosystem, strong community. |
| Rust | Languages & Frameworks | Trial | moved-in | Evaluating for performance-critical services. Strong safety guarantees. Smaller team experience needed. |
| TypeScript | Languages & Frameworks | Adopt | unchanged | Frontend standard. Improves code quality and maintainability across teams. |
| Go | Languages & Frameworks | Assess | new | Lightweight, concurrent programs. Monitoring for cloud infrastructure tools adoption. |
| Kubernetes | Platforms | Adopt | moved-in | Production container orchestration. Now enterprise standard after 18 months of scaling. |
| PostgreSQL | Platforms | Adopt | unchanged | Primary transactional database. Reliable, feature-rich, great community support. |
| DuckDB | Platforms | Trial | new | In-process OLAP database. Testing for analytics and reporting workloads. |
| GraphQL | Techniques | Trial | unchanged | Evaluating for API layer. Some teams successful, others finding it complex. Build internal expertise. |
| Observability | Techniques | Adopt | moved-in | Moved from monitoring. Traces, metrics, logs essential for distributed systems. |
| Monolithic Architecture | Techniques | Hold | moved-out | Legacy constraint. Actively migrating to microservices. Limited new development. |
```

## Markdown Table Format

```markdown
# Tech Radar - [Quarter/Date]

## Languages & Frameworks

| Technology | Ring | Movement | Rationale |
|------------|------|----------|-----------|
| Python | Adopt | unchanged | Standard backend language, mature ecosystem, strong community |
| TypeScript | Adopt | unchanged | Frontend standard, improves code quality |
| Rust | Trial | moved-in | Performance-critical services, safety guarantees |
| Go | Assess | new | Cloud infrastructure tools, lightweight deployment |
| Java | Trial | moved-out | Legacy systems, minimal new development |

## Tools

| Technology | Ring | Movement | Rationale |
|------------|------|----------|-----------|
| GitHub Actions | Adopt | unchanged | CI/CD standard, tight integration with repository |
| Docker | Adopt | unchanged | Container standard, widespread adoption |
| Prometheus | Adopt | unchanged | Metrics collection and alerting |
| Datadog | Trial | new | Comprehensive observability, evaluating cost vs value |
| Jenkins | Hold | unchanged | Legacy system, migration to GitHub Actions underway |

## Platforms

| Technology | Ring | Movement | Rationale |
|------------|------|----------|-----------|
| AWS | Adopt | unchanged | Primary cloud provider, multi-service strategy |
| PostgreSQL | Adopt | unchanged | Primary transactional database |
| Redis | Adopt | unchanged | Caching and session management |
| Kubernetes | Adopt | moved-in | Production standard after successful 18-month rollout |
| MongoDB | Assess | unchanged | Document storage, limited use cases justified |

## Techniques

| Technology | Ring | Movement | Rationale |
|------------|------|----------|-----------|
| Observability | Adopt | moved-in | Traces, metrics, logs essential for distributed systems |
| Infrastructure as Code | Adopt | moved-in | Standard practice for all deployments |
| GitOps | Trial | new | Declarative infrastructure management, early success |
| Microservices | Trial | unchanged | Active migration from monolithic architecture |
| API-First Design | Adopt | unchanged | Standard for all service development |

```

## HTML/SVG Radar Visualization

For visual representation, use this inline SVG radar structure:

```html
<svg viewBox="0 0 400 400" width="400" height="400" style="border: 1px solid #ccc">
  <!-- Background circles (rings) -->
  <circle cx="200" cy="200" r="30" fill="none" stroke="#ddd" stroke-width="1" />
  <circle cx="200" cy="200" r="60" fill="none" stroke="#ddd" stroke-width="1" />
  <circle cx="200" cy="200" r="90" fill="none" stroke="#ddd" stroke-width="1" />
  <circle cx="200" cy="200" r="120" fill="none" stroke="#ddd" stroke-width="1" />

  <!-- Quadrant dividers -->
  <line x1="200" y1="80" x2="200" y2="320" stroke="#ddd" stroke-width="1" />
  <line x1="80" y1="200" x2="320" y2="200" stroke="#ddd" stroke-width="1" />

  <!-- Ring labels -->
  <text x="200" y="95" text-anchor="middle" font-size="10" fill="#666">ADOPT</text>
  <text x="200" y="155" text-anchor="middle" font-size="10" fill="#666">TRIAL</text>
  <text x="200" y="215" text-anchor="middle" font-size="10" fill="#666">ASSESS</text>
  <text x="200" y="280" text-anchor="middle" font-size="10" fill="#666">HOLD</text>

  <!-- Quadrant labels -->
  <text x="120" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">
    LANGUAGES &amp; FRAMEWORKS
  </text>
  <text x="280" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">
    TOOLS
  </text>
  <text x="120" y="330" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">
    TECHNIQUES
  </text>
  <text x="280" y="330" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">
    PLATFORMS
  </text>

  <!-- Example entries (adjust coordinates as needed) -->
  <!-- Adopt ring entries (0-30px radius from center) -->
  <circle cx="200" cy="175" r="4" fill="#0a9" opacity="0.8" />
  <text x="210" y="180" font-size="9" fill="#000">Python</text>

  <circle cx="225" cy="165" r="4" fill="#0a9" opacity="0.8" />
  <text x="235" y="170" font-size="9" fill="#000">TypeScript</text>

  <!-- Trial ring entries (30-60px radius from center) -->
  <circle cx="230" cy="130" r="4" fill="#fa0" opacity="0.8" />
  <text x="240" y="135" font-size="9" fill="#000">Rust</text>

  <circle cx="260" cy="220" r="4" fill="#fa0" opacity="0.8" />
  <text x="270" y="225" font-size="9" fill="#000">Kubernetes</text>

  <!-- Assess ring entries (60-90px radius from center) -->
  <circle cx="200" cy="110" r="4" fill="#05f" opacity="0.8" />
  <text x="210" y="115" font-size="9" fill="#000">Go</text>

  <!-- Hold ring entries (90-120px radius from center) -->
  <circle cx="200" cy="80" r="4" fill="#f05" opacity="0.8" />
  <text x="210" y="85" font-size="9" fill="#000">Java</text>

  <!-- Legend -->
  <g transform="translate(320, 0)">
    <text x="0" y="15" font-size="9" font-weight="bold" fill="#333">Legend</text>
    <circle cx="5" cy="25" r="3" fill="#0a9" opacity="0.8" />
    <text x="12" y="28" font-size="8" fill="#333">Adopt</text>

    <circle cx="5" cy="40" r="3" fill="#fa0" opacity="0.8" />
    <text x="12" y="43" font-size="8" fill="#333">Trial</text>

    <circle cx="5" cy="55" r="3" fill="#05f" opacity="0.8" />
    <text x="12" y="58" font-size="8" fill="#333">Assess</text>

    <circle cx="5" cy="70" r="3" fill="#f05" opacity="0.8" />
    <text x="12" y="73" font-size="8" fill="#333">Hold</text>
  </g>
</svg>
```

## Best Practices

1. **Update regularly:** Quarterly or semi-annually to reflect organizational technology decisions
2. **Collaborative:** Create with input from tech leadership, architects, and team leads
3. **Justifiable:** Every entry should have clear rationale tied to business or technical goals
4. **Contextualized:** What's in "Adopt" for one organization may be "Assess" for another
5. **Action-oriented:** Use movements and placements to drive concrete decisions (training, migration, etc.)
6. **Transparent:** Share reasons for changes so teams understand technology strategy

## Movement Patterns to Watch

- **Moved-in:** Technology improving in your context. Consider increased investment or training.
- **Moved-out:** Technology losing relevance or performance. Plan migration or retirement.
- **Unchanged:** Stable. Validate that this is intentional, not neglect.
- **New entries:** Monitor adoption and team capability gaps.

## Questions to Ask When Creating

1. Do we have production experience with this technology?
2. What would adoption require (training, hiring, infrastructure)?
3. Does this fit our architecture and business strategy?
4. What are the risks and how would we mitigate them?
5. Are there competing technologies we should compare?
6. What's the opportunity cost of not adopting this?
7. How long will this technology remain relevant for our use case?
