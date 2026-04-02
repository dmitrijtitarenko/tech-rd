---
name: Notion Knowledge Base
description: >
  Optional per-user Notion workspace for storing and organizing research outputs.
  Only created when user explicitly wants it. Designs database structure based on
  user preferences. Triggered by "save to Notion", "create knowledge base",
  "organize my research", "Notion setup".
---

# Notion Knowledge Base

## Setup and Activation

This skill is entirely optional. Notion integration is only created when user explicitly requests it.

Initial setup process:
1. Ask user about organizational preferences before creating anything
2. Determine desired database structure and property schema
3. Configure templates for different research output types
4. Set up relationships between related topics

## Database Structure

Core properties for all research entries:

- **Title**: Research topic or technology name
- **Domain**: Category (AI/ML, Infrastructure, Security, etc.)
- **Date**: When research was conducted
- **Confidence**: High, Medium, Low (based on research depth)
- **Status**: Draft, In Progress, Complete, Archived
- **Tags**: Auto-generated from content and user labels
- **Output Format**: Type of deliverable (Deep Report, Comparison, Tech Radar, Scorecard, etc.)
- **Sources**: Links to research materials used
- **Summary**: Quick overview of findings

## Page Templates

Pre-configured templates for common output formats:

- **Deep Research Report**: Executive summary, context, detailed findings, recommendations
- **Technology Comparison**: Side-by-side comparison matrix with weighted criteria
- **Tech Radar Entry**: Technology name, ring status, movement direction, rationale
- **Competitive Brief**: Product overview, positioning, strengths, weaknesses, threat assessment
- **Scorecard**: Evaluation criteria with scores, weights, justification for each rating
- **Trend Analysis**: Timeline, adoption curve, market signals, future projection

## Relations and Links

Connect related research topics:

- "Vector Databases" relates to "AI/ML Research"
- "RAG Frameworks" relates to both "Generative AI" and "Vector Databases"
- "LLM Cost Optimization" relates to "Model Efficiency"

Enable bidirectional relations so navigating between topics is frictionless.

## Auto-Generated Tags

Tags extracted from research content during save process:

- Technologies mentioned
- Problem domains
- Industry verticals
- Maturity stages
- User-defined categories

## One-Command Save

Any research output saved to Notion with single command. Claude handles:
- Format conversion to template structure
- Property assignment
- Relation inference
- Duplicate detection

## Tool Implementation

Uses Notion MCP tools:
- `notion-create-database`: Initial KB setup
- `notion-create-pages`: Add research entries
- `notion-update-page`: Modify existing entries
- `notion-search`: Query knowledge base
