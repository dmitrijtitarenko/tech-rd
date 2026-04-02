# Contributing to tech-rd

Thank you for your interest in improving the tech-rd plugin. This guide covers everything you need to get started.

## Development Setup

1. Clone the repository:

```bash
git clone https://github.com/dtytarenko/tech-rd.git
cd tech-rd
```

2. Install Node dependencies (required for Mermaid diagram generation):

```bash
npm install
```

3. Install Python test dependencies:

```bash
pip install pytest pandas numpy scipy
```

4. Verify your setup:

```bash
pytest tests/ -v
```

All 117+ tests should pass before you begin working.

## Project Structure

```
tech-rd/
  .claude-plugin/plugin.json   # Plugin metadata (name, version, license)
  .mcp.json                    # 18 MCP server configurations
  marketplace-entry.json       # Marketplace listing metadata
  agents/                      # 5 orchestration agents (.md with YAML frontmatter)
  commands/                    # 12 slash commands (.md with YAML frontmatter)
  skills/                      # 37 skill directories, each with SKILL.md
  scripts/                     # 8 Python analysis scripts
  tests/                       # pytest test suite
  examples/                    # Sample outputs in all formats
```

## How to Add a New Skill

1. Create a directory under `skills/` with a kebab-case name:

```bash
mkdir skills/my-new-domain
```

2. Create `skills/my-new-domain/SKILL.md` with these required sections:

```markdown
# My New Domain

Description of what this skill covers.

## Key Research Dimensions

- Dimension 1
- Dimension 2

## Analysis Framework

How the agent should analyze findings.

## Output Templates

What deliverables this skill produces.

## Data Sources

| Connector | Purpose |
|-----------|---------|
| ~~web research | General web search |
| ~~source control | Repository analysis |
```

3. Add the skill name to the parametrized list in `tests/test_structure.py` under `TestSkillNames`.

4. Update `README.md` skill count and add the skill to the appropriate category table.

5. Update `marketplace-entry.json` component counts.

6. Run `pytest tests/ -v` to confirm all tests pass.

## How to Add a New Command

1. Create `commands/my-command.md` with YAML frontmatter:

```markdown
---
description: Short description of the command
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [argument]
---

# My Command

What this command does.

## Workflow

1. Step 1
2. Step 2

## Output Format

(Include the three-tier output block from existing commands.)

## Notes

- Important considerations
```

2. Update the command count in `tests/test_structure.py`, `README.md`, and `marketplace-entry.json`.

## How to Add a New MCP Server

1. Add the server entry to `.mcp.json` under `mcpServers`:

```json
"my-server": {
  "type": "http",
  "url": "https://mcp.example.com/mcp"
}
```

2. Document it in `README.md` in the MCP integrations table.

3. Add it to `CONNECTORS.md` under the appropriate `~~category`.

4. Document required environment variables in `MCP_SETUP.md`.

## Style Guide

All plugin content must follow the scientific style guide at `skills/output-formats/references/scientific-style-guide.md`. Key rules:

- No emojis anywhere in `.md`, `.json`, or `.py` files.
- No bullet-point lists in report body text; use tables and prose.
- All numeric claims must reference computed values (Python scripts), not estimates.
- Use `~~category` connector placeholders (not hardcoded tool names) in skill Data Sources sections.
- Agent frontmatter `tools:` must list only real Claude tools (WebSearch, WebFetch, Read, Write, Bash, Agent) plus `~~connector` placeholders.

## Running Tests

```bash
# Full suite
pytest tests/ -v

# Single module
pytest tests/test_structure.py -v

# Single test
pytest tests/test_structure.py::TestSkillNames::test_skill_directories_and_files -v
```

Tests validate:

- File structure (directories, counts, required files)
- Content quality (no emojis, valid JSON)
- MCP configuration (schema, URLs, server count)
- Script validity (imports, function definitions)
- Content completeness (required sections in skills, commands, agents)

## Pull Request Process

1. Create a feature branch from `main`.
2. Make your changes following the style guide.
3. Run `pytest tests/ -v` and confirm 0 failures.
4. Update `CHANGELOG.md` with your changes under an `[Unreleased]` section.
5. Open a PR with a clear title and description of what changed and why.

## Reporting Issues

Open an issue on GitHub with:

- What you expected to happen
- What actually happened
- Steps to reproduce
- Plugin version (from `plugin.json`)
