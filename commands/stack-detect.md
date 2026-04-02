---
description: Technology stack detection for websites
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [url]
---

# Stack Detect Command

Detect technology stack of websites and products.

## Workflow

1. **Parse Input URL**
   - Validate and normalize URL
   - Ensure proper protocol handling (http/https)
   - Identify domain and subdomain structure

2. **Frontend Technology Detection**
   - Analyze HTTP headers for technology hints
   - Examine HTML source for framework signatures:
     - React: __NEXT_DATA__, _React_props, etc.
     - Vue: v-app, v-bind, vue-loader attributes
     - Angular: ng-app, ng-controller, etc.
     - Svelte: svelte signatures
   - Check CSS framework identifiers (Tailwind, Bootstrap, etc.)
   - Analyze bundle hashes for bundler detection (Webpack, Vite, etc.)
   - Review Network requests for framework libraries

3. **Backend Technology Detection**
   - Server headers: X-Powered-By, Server headers
   - Response headers for framework signatures
   - Cookie names and structures
   - Response patterns (performance headers, caching)
   - Technology indicators:
     - Python: django, flask, fastapi patterns
     - Node.js: express, next.js, nestjs patterns
     - Java: spring, tomcat patterns
     - Ruby: rails patterns
     - Go: typical Go server patterns

4. **Infrastructure Detection**
   - CDN/Content Delivery: Cloudflare, Akamai, CloudFront hints
   - Hosting Provider: DNS providers, IP geolocation
   - DNS records: Cloud provider hints, service indicators
   - SSL certificate information (issuer, organization)
   - Regional endpoint distribution

5. **Services & APIs Detection**
   - Third-party service integrations via HTTP requests
   - Analytics platforms (Google Analytics, Mixpanel, etc.)
   - Tracking pixels and data services
   - Payment processors (Stripe, Square, etc.)
   - Email services (SendGrid, Mailchimp, etc.)
   - Search services (Algolia, Elasticsearch, etc.)
   - CMS systems (Contentful, Sanity, etc.)

6. **Database Technology Hints**
   - Response patterns suggesting database type
   - API endpoints revealing database technology
   - Error messages with database signatures
   - When available: ~~web-research (deep crawl), ~~ui-components (for web output generation)

7. **Monitoring & Observability**
   - APM tools (DataDog, New Relic, etc.)
   - Error tracking (Sentry, Rollbar, etc.)
   - Logging services (LogRocket, etc.)
   - Monitoring tools signatures

8. **Output: Stack Report**
   - URL and detection date
   - Frontend Stack:
     - Framework (e.g., React 18)
     - Build tool (e.g., Webpack)
     - CSS framework (e.g., Tailwind CSS)
     - UI libraries identified
   - Backend Stack:
     - Language and framework
     - API type (REST, GraphQL, etc.)
   - Infrastructure:
     - Hosting provider
     - CDN/Performance layer
     - Geographic distribution
   - Services Detected:
     - Analytics platforms
     - Third-party integrations
     - Payment processors
   - Confidence Levels: Mark each detection with High/Medium/Low confidence
   - Additional Observations:
     - Performance characteristics
     - Architectural patterns observed
     - Notable technology choices

9. **Technology Extraction Rules**
   - Use multiple detection strategies (redundancy)
   - Prefer server headers over other signals
   - Flag conflicting signals
   - Note when detection is ambiguous

10. **Confidence Assessment**
    - High: Clear signature or authoritative header
    - Medium: Multiple corroborating signals
    - Low: Single signal or inference

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Some frameworks intentionally hide their identity
- Third-party services may change without stack updates
- Detections are snapshots (technology changes over time)
- Cannot detect all technologies (especially closed-source stacks)
- Some detections are probabilistic rather than certain
