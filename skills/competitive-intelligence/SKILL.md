---
name: competitive-intelligence
description: >
  Identifies and analyzes competitor technology stacks, feature comparisons, and market
  positioning. Triggered by "competitor tech stack", "competitive analysis", "who uses",
  "market positioning", "feature comparison". Uses tech stack detection (BuiltWith-style
  web header analysis, JS fingerprinting), job postings, GitHub activity, funding data.
  Outputs competitive matrix and positioning map.
---

## Overview

This skill enables organizations to understand competitive technology strategies, feature offerings, and market positioning. It provides insights into what technologies successful competitors use, what features matter to customers, and how to position against alternatives.

## Tech Stack Detection Methods

### Web Fingerprinting

**HTTP Header Analysis**:
- Server header: "Server: Apache/2.4.41", "Server: nginx/1.18.0"
- X-Powered-By: reveals language/framework ("X-Powered-By: Express")
- Cache-Control, X-Cache-By: CDN detection (Akamai, Cloudflare, Fastly)
- Deprecation headers, API versioning headers reveal backend API design

**HTML/Meta Tags**:
- `<meta name="generator" content="Hugo">` reveals site generators
- Analytics libraries (Google Analytics, Mixpanel script tags)
- A/B testing platforms (Optimizely, VWO)
- Advertising platforms (Google Ad Manager, Criteo pixels)

**JavaScript Analysis**:
- Library detection (React, Vue, Angular in webpack bundles)
- Frontend tooling fingerprint (Webpack, Vite, Parcel)
- Third-party service integrations (Stripe, Twilio, SendGrid API calls)
- CSS framework (Bootstrap, Tailwind classes)

**API Reconnaissance**:
- GraphQL endpoint discovery (introspection query)
- REST API endpoint mapping (JavaScript fetch/XMLHttpRequest calls)
- Rate limit headers: frequency, quota (shows API maturity)
- OpenAPI/Swagger documentation endpoints

### Job Posting Analysis

**Tech Stack Signals**:
- Job postings list required/preferred technologies
- Ratio of Java vs Go hiring = backend strategy
- Frontend framework mentions in job descriptions
- Infrastructure keywords (Kubernetes, Docker, AWS) = cloud maturity

**Hiring Intensity**:
- Volume of job openings in specific domains (hiring for "ML engineers" = ML focus)
- Salary ranges revealed in postings (market competitiveness assessment)
- Geographic distribution (remote vs specific offices = expansion plans)

**Process Signals**:
- "5+ years Kubernetes experience" = mature DevOps vs greenfield projects

### GitHub Activity Intelligence

**Repository Analysis**:
- Language distribution (go, rust, python commits) reveals tech focus
- Starred projects (bookmarks) indicate technologies team evaluates
- Organization activity (commits/merges) = engineering velocity
- Dependency usage (go.mod, requirements.txt, package.json) = tech ecosystem

**Community Signals**:
- Open-source projects released = technology strategy transparency
- Contribution patterns (active maintenance = good signal)
- Issue response time = team capacity assessment

### Funding & Financial Data

**Signals**:
- Funding rounds indicate growth velocity (Series A= early scale, Series D = mature)
- Investor list (Benchmark, a16z) = strategic partnerships, investor expertise
- IPO announcements = large-scale infrastructure investment needs
- Acquisition targets indicate strategic tech direction
- Patent filings = R&D focus areas

## Competitive Intelligence Framework

### Feature Comparison Matrix

**Columns**: Your product, Competitor A, Competitor B, Competitor C

**Rows**: Feature categories:
- **Core functionality**: What problems does each solve?
- **Scalability**: Max QPS, data volume, multi-region
- **Integrations**: 100+ third-party apps vs 5?
- **Pricing**: Per-seat, per-transaction, freemium?
- **UI/UX**: Modern React-based UI vs legacy Backbone?
- **Compliance**: HIPAA, SOC2, GDPR ready?
- **Support**: 24/7 enterprise support vs community-only?

**Output**: Green (strong), yellow (parity), red (gap)

### Market Positioning Map

**2D plot**:
- **X-axis**: Price (low cost vs premium)
- **Y-axis**: Feature richness (simple vs full-featured)

**Plotting**:
- "Affordable simplicity" quadrant (Stripe: simple payment, low cost)
- "Premium platform" quadrant (Salesforce: comprehensive CRM, high cost)
- "Freemium leader" quadrant (Slack: free tier drives adoption)

**Insights**:
- Gaps = market opportunities
- Crowded quadrant = commoditizing feature set
- Premium positioning = hard to compete on features; compete on support/specialization

## Intelligence Sources & Techniques

### Primary Research
- Website walkthrough: UI/UX assessment, performance, mobile experience
- Pricing page: pricing model, packaging, discount structure
- Help/Docs: completeness, up-to-date, customer pain points
- Customer testimonials: use cases, company sizes, industries served

### Secondary Research
- Press releases: product launches, partnerships, acquisitions
- Investor updates / shareholder reports: growth metrics, strategic direction
- Tech blogs: engineering decisions, architecture posts
- Podcast/conference talks: founder vision, roadmap hints

### Quantitative Data
- Website traffic (SimilarWeb, Alexa): market traction
- App store rankings (iOS/Android): growth trajectory
- Social media followers: community engagement
- Employee count (LinkedIn): team size, growth hiring

## Analysis Outputs

### Competitive Snapshot Report
- Feature gap analysis (we're weak in X; competitor Y is strong)
- Pricing comparison (our pricing 2x higher; feature parity justifiable?)
- Tech debt assessment (competitor using legacy vs modern stack)
- Go-to-market strategy (how are they growing faster?)

### Threat Assessment
- Which competitors are growing fastest?
- Feature gaps = vulnerability (competitor wins in these areas)
- Customer migration risk (switching cost = satisfaction predictor)

### Opportunity Analysis
- Underserved market segments (competitor doesn't serve X industry)
- Technology advantages (we're using newer tech = better reliability/scalability)
- Feature ideas (not offered by any competitor = blue ocean?)

## When to Use This Skill

- **Product roadmap planning**: What features matter to customers vs what competitors offer
- **Pricing strategy**: Competitive pricing benchmarking, bundling strategy
- **Tech stack decisions**: How do successful competitors engineer their systems?
- **Sales strategy**: How to position against specific competitors (strength/weakness)
- **M&A analysis**: Acquiring competitor for tech/talent/customers?
- **Hiring**: Which competitor's engineering practices should we emulate?
- **Market entry**: Is this market crowded (difficult to win) or open (opportunity)?

## Output Examples

- Feature comparison spreadsheet (matrix format, scoring)
- Competitive positioning map (2D scatter, quadrant analysis)
- Tech stack intelligence report (competitor architectures, technology choices)
- Threat assessment (which competitors pose biggest risk, why)
- Opportunity analysis (feature gaps, underserved segments, market white space)
- Job posting analysis (hiring trends indicating strategic direction)

## Computational Workflows

### Pre-built Analysis Scripts

**tech_stack_detector.py**: Fingerprints competitor websites using HTTP headers, meta tags, JavaScript analysis. Detects: server software, frontend framework, CDN, analytics platform, payment processor. Outputs: tech stack JSON, confidence scores per detection.

**feature_matrix_scorer.py**: Builds feature comparison matrix (your product vs. competitors A, B, C). Inputs: feature list with weights (importance 1-10). Outputs: gap analysis heatmap (green/yellow/red), feature parity score, gaps that matter most to customers.

**job_posting_analyzer.py**: Queries Indeed, LinkedIn for competitor job postings. Tracks: hiring volume trend, required technologies, salary range, experience requirements. Outputs: tech strategy signals (which areas are growing), hiring velocity, compensation benchmark.

**market_positioning_mapper.py**: Creates 2D scatter plot (price vs feature richness, or other dimensions). Plots: your product, competitors. Inputs: pricing, feature count (or custom dimension). Outputs: positioning strategy recommendation (underserved quadrant?).

### Dynamic Computation Examples

1. **Competitive Tech Stack Analysis**: Given competitor domain, extract full tech stack (frontend, backend, infrastructure, third-party services). Map: architecture patterns (serverless vs k8s), language choices, cloud provider commitment. Compare: modernization level, tech debt indicators.

2. **Feature Demand Prediction**: Input: customer testimonials, use cases mentioned by competitors. Extract: frequently mentioned features, feature priority patterns, unmet needs (no competitor mentions = opportunity). Output: feature roadmap recommendation, customer segment focus.

3. **Hiring Intensity vs Product Roadmap Correlation**: Analyze competitor job postings over time. Spike in "ML Engineer" hires → likely AI feature development. Correlate: hiring trends with recent product announcements → reveals upcoming focus areas.

### Output Artifacts

- **Competitive Tech Stack Report**: Detailed tech breakdown per competitor (frontend, backend, hosting, third-party services), modernization assessment
- **Feature Comparison Matrix**: Feature by feature (rows) vs your company and competitors (columns), gap analysis heat map, priority scoring
- **Market Positioning Map**: 2D scatter (price vs feature richness, or innovation vs cost) showing your product and competitors, market opportunities highlighted
- **Competitive Threat Assessment**: Which competitors pose biggest risk (why), feature gaps you need to address, market segments competitors winning/losing, hiring trends indicating strategic shifts

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub API for competitor technology stack analysis, language distribution, dependency tracking
- **~~web research**: Competitor website fingerprinting, job posting analysis, funding announcements
- **~~financial data**: Crunchbase funding data, acquisition announcements, revenue signals
- **~~product analytics**: Similarweb traffic trends, app store rankings, user growth signals

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: BuiltWith API (commercial tech stack detection), GitHub API (repository language/activity analysis), LinkedIn API (employee growth trends), Crunchbase (funding/investment data), job posting aggregators (Indeed API, Glassdoor scraping), website analytics (Similarweb, Alexa)
