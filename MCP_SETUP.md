# MCP Server Setup Guide

tech-rd ships with 18 pre-configured MCP servers in `.mcp.json`. This guide covers authentication, verification, and troubleshooting for each.

## How MCP Servers Work in This Plugin

The `.mcp.json` file declares MCP servers that Claude can connect to for live data. These are HTTP-based remote servers; no local installation is required. Authentication is handled through your Claude desktop app's connected accounts or via environment variables.

The plugin is designed to work without any MCP servers connected. Commands and agents use the `~~category` connector system, which gracefully falls back to WebSearch and WebFetch when a specific MCP server is unavailable.

## Server-by-Server Setup

### Source Control

| Server | URL | Authentication |
|--------|-----|----------------|
| **GitHub** | `https://api.github.com/mcp` | Connect GitHub account in Claude settings |

Used by: `/oss-audit`, `/stack-detect`, `/landscape`, Tech Scout agent, Trend Analyst agent.

### Communication

| Server | URL | Authentication |
|--------|-----|----------------|
| **Slack** | `https://mcp.slack.com/mcp` | Connect Slack workspace in Claude settings |

Used by: Research Director for sharing reports to channels.

### Project Management

| Server | URL | Authentication |
|--------|-----|----------------|
| **Linear** | `https://mcp.linear.app/mcp` | Connect Linear account in Claude settings |
| **Atlassian** | `https://mcp.atlassian.com/v1/mcp` | Connect Atlassian account in Claude settings |

Used by: `/standards`, scheduling skill for tracking research tasks.

### Knowledge Base

| Server | URL | Authentication |
|--------|-----|----------------|
| **Notion** | `https://mcp.notion.com/mcp` | Connect Notion workspace in Claude settings |

Used by: notion-knowledge-base skill, data-export skill for saving research.

### AI/ML Platforms

| Server | URL | Authentication |
|--------|-----|----------------|
| **Hugging Face** | `https://huggingface.co/mcp?login&gradio=none` | Connect Hugging Face account in Claude settings |

Used by: `/research` (AI/ML topics), ai-ml-research skill.

### Research & Academic

| Server | URL | Authentication |
|--------|-----|----------------|
| **Consensus** | `https://mcp.consensus.app/mcp` | Connect Consensus account in Claude settings |
| **bioRxiv** | `https://hcls.mcp.claude.com/biorxiv/mcp` | No authentication required (public) |

Used by: `/research`, `/patent-scan`, biotech-healthtech skill, Evidence Validator agent.

### Web Search

| Server | URL | Authentication |
|--------|-----|----------------|
| **Tavily** | `https://mcp.tavily.com/mcp` | Connect Tavily account in Claude settings |

Used by: All commands (enhanced web search), Tech Scout agent.

### Financial Data

| Server | URL | Authentication |
|--------|-----|----------------|
| **FactSet** | `https://mcp.factset.com/content/v1` | Requires FactSet subscription; connect in Claude settings |
| **Quartr** | `https://mcp.quartr.com/mcp` | Connect Quartr account in Claude settings |

Used by: `/tech-dd`, fintech skill, competitive-intelligence skill.

### Analytics & Monitoring

| Server | URL | Authentication |
|--------|-----|----------------|
| **PostHog** | `https://mcp.posthog.com/mcp` | Connect PostHog account in Claude settings |
| **Datadog** | `https://mcp.datadoghq.com/mcp` | Connect Datadog account in Claude settings |
| **PagerDuty** | `https://mcp.pagerduty.com/mcp` | Connect PagerDuty account in Claude settings |

Used by: observability skill, devops-sre skill, cost-optimization skill.

### Cloud & Infrastructure

| Server | URL | Authentication |
|--------|-----|----------------|
| **AWS Marketplace** | `https://marketplace-mcp.us-east-1.api.aws/mcp` | Connect AWS account in Claude settings |
| **Cloudflare** | `https://bindings.mcp.cloudflare.com/mcp` | Connect Cloudflare account in Claude settings |

Used by: cloud-infrastructure skill, cost-optimization skill, `/build-vs-buy`.

### Design

| Server | URL | Authentication |
|--------|-----|----------------|
| **Figma** | `https://figma.com/mcp` | Connect Figma account in Claude settings |
| **shadcn** | `https://mcp.shadcn.com/mcp` | No authentication required (public) |

Used by: diagram-generation skill, output-formats skill (web output template).

## Verifying Connections

After connecting your accounts in Claude settings, test with a simple command:

```
/research test connection
```

The Research Director will report which MCP servers it can reach and which are unavailable. Unavailable servers are silently skipped; the plugin falls back to WebSearch/WebFetch.

## Troubleshooting

**"MCP server not responding"**
Most MCP servers require you to connect the corresponding account in Claude's settings (Settings > Connectors). The plugin does not manage authentication directly.

**"Server returned 401/403"**
Your connected account may have expired or lack the required permissions. Reconnect the account in Claude settings.

**"Server not found in .mcp.json"**
If you need to add a custom MCP server, add it to `.mcp.json` under `mcpServers` with `type: "http"` and the server URL. See CONTRIBUTING.md for details.

**Plugin works without any MCP servers**
This is by design. The `~~category` connector system means every command and skill can fall back to built-in Claude tools (WebSearch, WebFetch, Bash). MCP servers enhance results with live, structured data but are never required.

**FactSet returns empty results**
FactSet requires an active subscription. If you don't have one, the plugin will fall back to web search for financial data. Consider Quartr as a lighter alternative for earnings call data.

## Disabling Specific Servers

To disable a server you don't need, remove its entry from `.mcp.json`. This reduces connection overhead. The plugin will continue to work using fallback sources.
