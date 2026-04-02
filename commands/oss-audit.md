---
description: Open source project health audit
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [repo-url or package-name]
---

# OSS Audit Command

Comprehensive health audit of open source projects.

## Workflow

1. **Identify Target**
   - Parse repository URL (GitHub, GitLab, etc.) or package name
   - Resolve to canonical repository location
   - Validate project exists and is actively maintained

2. **Bus Factor Analysis**
   - Count active maintainers with commit authority
   - Analyze commit distribution (how concentrated?)
   - Check if project has documented succession plan
   - Risk Rating: Green (3+ maintainers), Yellow (1-2), Red (single maintainer)

3. **Release Cadence Evaluation**
   - Analyze release history (frequency, regularity)
   - Check time between versions
   - Assess if releases include breaking changes with deprecation period
   - Risk Pattern: Green (regular releases), Yellow (irregular), Red (stalled)

4. **Issue Response Analysis**
   - Sample recent issues: resolution time
   - Check for stale/unanswered issues
   - Assess bug fix priority and speed
   - Community responsiveness level

5. **Security Posture Assessment**
   - Search for reported vulnerabilities (CVE, security advisories)
   - Check if project has security policy and disclosure process
   - Review dependency vulnerability scanning
   - Audit history: major incidents, response times
   - Risk: Green (proactive), Yellow (reactive), Red (negligent)

6. **License Analysis**
   - Identify primary license
   - Flag GPL/proprietary if relevant to your use case
   - Check for license compatibility with dependencies
   - Assess commercial restrictions

7. **Dependency Health**
   - Count total dependencies
   - Identify outdated or unmaintained dependencies
   - Check for circular dependencies or version conflicts
   - Risk assessment: dependency chain fragility

8. **Contributor Diversity**
   - Analyze contributor list (company affiliation, independence)
   - Check for single-company projects (higher acquisition/abandonment risk)
   - Assess new contributor onboarding
   - Community health: vibrant or cliquish?

9. **Output: Health Scorecard**
   - Overall health rating (1-10 or Green/Yellow/Red)
   - Detailed score breakdown by metric:
     - Bus Factor: [color]
     - Release Cadence: [color]
     - Issue Response: [color]
     - Security Posture: [color]
     - License: [status]
     - Dependency Health: [color]
     - Contributor Diversity: [color]
   - Risk Summary: Production readiness assessment
   - Recommendations for integration or monitoring

10. **Special Considerations**
    - For enterprise use: commercial support availability
    - For critical systems: evaluate backup alternatives
    - For emerging projects: understand growth stage and stability trajectory

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Use GitHub API insights when available (~~source-control)
- Look for red flags: abandoned issues, security negligence, excessive breaking changes
- Consider project age and maturity stage in assessment
- Note projects acquired or transitioning to new maintainers
