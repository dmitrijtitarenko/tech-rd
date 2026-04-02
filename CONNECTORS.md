# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~source control` might mean GitHub, GitLab, or Bitbucket — any source control system with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Source control | `~~source control` | GitHub | GitLab, Bitbucket |
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Project tracker | `~~project tracker` | Linear, Atlassian (Jira) | Asana, ClickUp, Shortcut |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| AI/ML platform | `~~ml platform` | Hugging Face | Weights & Biases, MLflow |
| Academic research | `~~research` | Consensus, bioRxiv | Semantic Scholar, PubMed |
| Web research | `~~web research` | Tavily | Perplexity, Exa |
| Cloud provider | `~~cloud` | AWS Marketplace, Cloudflare | GCP, Azure |
| Monitoring | `~~monitoring` | Datadog, PagerDuty | New Relic, Grafana, Splunk |
| Financial data | `~~financial data` | FactSet, Quartr | Bloomberg, PitchBook |
| Product analytics | `~~product analytics` | PostHog | Amplitude, Mixpanel |
| Design system | `~~design system` | shadcn, Figma | Storybook, Zeroheight |
