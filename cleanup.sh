#!/usr/bin/env bash
# cleanup.sh — Run locally to remove build artifacts, caches, and bloat
# Usage: cd tech-rd-final && bash cleanup.sh

set -euo pipefail

echo "=== tech-rd plugin cleanup ==="

# Remove node_modules (543 MB)
if [ -d "node_modules" ]; then
  echo "Removing node_modules/..."
  rm -rf node_modules
else
  echo "node_modules/ not found (already clean)"
fi

# Remove Python caches
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true
if [ -d ".pytest_cache" ]; then
  rm -rf .pytest_cache
fi

# Remove LaTeX build artifacts
find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.synctex.gz" \) -delete 2>/dev/null || true

# Remove macOS metadata
find . -type f -name ".DS_Store" -delete 2>/dev/null || true

# Remove DIAGRAM_COMPILATION_REPORT.md if present
if [ -f "DIAGRAM_COMPILATION_REPORT.md" ]; then
  echo "Removing DIAGRAM_COMPILATION_REPORT.md..."
  rm -f DIAGRAM_COMPILATION_REPORT.md
fi

# Remove root-level research_data.json duplicate (should be in examples/)
if [ -f "research_data.json" ]; then
  echo "Removing root research_data.json (duplicate of examples/research_data.json)..."
  rm -f research_data.json
fi

echo ""
echo "Done. Run 'du -sh .' to verify size reduction."
echo "Expected clean size: ~2-3 MB"
