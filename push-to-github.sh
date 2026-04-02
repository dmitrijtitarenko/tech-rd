#!/usr/bin/env bash
# push-to-github.sh — Run locally to create repo and push
# Usage: cd tech-rd-final && bash push-to-github.sh
#
# Prerequisites:
#   1. GitHub CLI installed: brew install gh
#   2. Authenticated: gh auth login
#   3. Delete the assets/ folder first: rm -rf assets/

set -euo pipefail

echo "=== tech-rd: Create GitHub repo and push ==="

# Clean up items that shouldn't be committed
rm -rf assets/ node_modules/ __pycache__ .pytest_cache/ package-lock.json 2>/dev/null || true
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name ".DS_Store" -delete 2>/dev/null || true

# Remove the .git directory if it was initialized in the sandbox
rm -rf .git 2>/dev/null || true

# Initialize fresh
git init -b main
git add -A

# Verify nothing unwanted is staged
echo ""
echo "=== Staged files ==="
git status --short | head -30
echo "... ($(git status --short | wc -l) files total)"
echo ""

# Commit
git commit -m "Initial release: tech-rd v0.1.0

Full-spectrum technology R&D intelligence plugin for Claude.
- 37 specialized skills across 31 domain verticals
- 12 research commands (research, compare, tech-radar, landscape, etc.)
- 5 orchestrated agents (Research Director, Tech Scout, Trend Analyst, Deep Researcher, Evidence Validator)
- 18 MCP server integrations
- 9 professional output templates (3-tier: Markdown, LaTeX/PDF, Interactive Web)
- 8 Python analysis scripts
- 137 automated tests across 6 test modules
- Tool-agnostic ~~ connector system for graceful MCP fallback"

# Create GitHub repo (public, with description)
gh repo create dmitrijtitarenko/tech-rd \
  --public \
  --description "Full-spectrum technology R&D intelligence plugin for Claude — 37 skills, 12 commands, 5 agents, 18 MCP integrations" \
  --source=. \
  --remote=origin

# Push
git push -u origin main

echo ""
echo "=== Done ==="
echo "Repo: https://github.com/dmitrijtitarenko/tech-rd"
echo ""
echo "Next steps:"
echo "  1. Go to https://github.com/dmitrijtitarenko/tech-rd/settings and add topics"
echo "  2. Enable GitHub Actions in the Actions tab if not auto-enabled"
echo "  3. Submit to marketplace / hackathon"
