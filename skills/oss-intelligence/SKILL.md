---
name: oss-intelligence
description: >
  Assesses open-source project health using metrics: bus factor, release cadence, contributor
  diversity, license risk, security posture, fork trends, sponsor/funding status, maintainer
  burnout signals. Triggered by "OSS health", "open-source assessment", "dependency risk",
  "maintainer burnout". Outputs health scorecard (green/yellow/red) with risk analysis.
---

## Overview

This skill evaluates the health and sustainability of open-source projects your organization depends on. It identifies risks (unmaintained projects, single-point-of-failure developers, security vulnerabilities) and opportunities (well-maintained alternatives, healthy ecosystems).

## Health Assessment Dimensions

### Bus Factor (Concentration Risk)

**Definition**: How many key developers would need to leave before the project stalls?

**Metrics**:
- **Commit concentration**: Top developer contributes >50% = high risk
- **Review concentration**: Single reviewer approves >80% of PRs = bottleneck
- **Active maintainers**: 1 maintainer = critical risk; 3-5 = healthy
- **Truck factor**: If top N contributors disappeared, project survives?

**Scoring**:
- Green: 5+ active maintainers, <30% concentration on any one person
- Yellow: 2-4 maintainers, 30-50% concentration
- Red: 1 maintainer or >70% concentration (high risk project)

**Remediation**:
- Contribute back to maintainer hiring, code review
- Fork if critical; adopt alternative if available
- Negotiate commercial support (example: Canonical for Ubuntu)

### Release Cadence & Version Stability

**Metrics**:
- **Release frequency**: Monthly stable releases = healthy; >1 year without release = stale
- **Version bumping**: Semantic versioning (MAJOR.MINOR.PATCH) = predictable
- **Pre-release policy**: Beta/RC versions before stable = quality gate
- **Deprecation timeline**: 2+ releases warning before removal = considerate

**Scoring**:
- Green: Monthly releases, clear versioning, 6-month deprecation notice
- Yellow: Quarterly releases, inconsistent versioning
- Red: >6 months between releases, BREAKING CHANGES without notice

**Risk**: Long gaps between releases = security vulnerabilities accumulate

### Contributor Diversity

**Metrics**:
- **Company representation**: Single company dominates (Red Hat Linux) vs independent (Kubernetes)
- **Top 10% contribution**: <50% = diverse; >80% = dominated
- **New contributors per year**: Trend indicates project health
- **Onboarding friction**: Contributing guidelines, CONTRIBUTING.md = good signal
- **Comment/code ratio**: Collaborative review vs drive-by commits

**Scoring**:
- Green: Multiple companies, 5+ new contributors/year, clear onboarding
- Yellow: Dominated by 2-3 companies, 2-5 new contributors/year
- Red: Single company, declining contributor base, no CONTRIBUTING docs

**Risk**: Over-dependence on single sponsor (company pivot = project dies)

### Security Posture

**Metrics**:
- **CVE response time**: How fast are security issues fixed? (example: Kubernetes usually <30 days)
- **Vulnerability disclosure policy**: Responsible disclosure (embargo period) vs public immediately?
- **Supply chain security**: Signed commits, signed releases, provenance?
- **Dependency audit**: Uses tools (Dependabot, Snyk) to track transitive dependency vulnerabilities?
- **SLSA framework**: Compliance with Software Package Security

**Scoring**:
- Green: <30 day CVE response, signed releases, dependency scanning, clear security policy
- Yellow: 30-90 day response, some security automation
- Red: >90 days or no clear security process, unsigned releases

**Risk**: Using project with 0-day vulnerabilities or slow patching = customer risk

### License Compliance Risk

**Metrics**:
- **License type**: MIT/Apache 2.0 (permissive) vs GPL (copyleft)
- **License compatibility**: Can you use alongside your stack?
  - MIT + Apache 2.0 = compatible
  - Apache 2.0 + GPL v3 = problematic (patent clause conflict)
  - AGPL = restrictive (source code disclosure required if SaaS)
- **License tracking**: SPDX format standardization

**Risk Scoring**:
- Green: MIT/Apache 2.0/BSD licenses
- Yellow: GPL v2 (understand copyleft requirements)
- Red: AGPL (if SaaS), proprietary/unknown license

**Remediation**: Legal review before adopting AGPL/GPL; use license compliance tools (FOSSA, Black Duck)

### Maintenance Status & Activity

**Metrics**:
- **Latest commit age**: <1 month = active; >6 months = stale; >1 year = dead
- **Issue/PR resolution time**: <1 week = responsive; >1 month = slow
- **Issue/PR backlog**: Growing vs shrinking
- **Stale issue/PR automation**: Archiving old issues = good practice

**Scoring**:
- Green: Active commits, <1 week issue response, <100 open issues
- Yellow: Commits quarterly, 1-4 week response, 100-500 open issues
- Red: No commits >6 months, >1 month response, 500+ open issues

**Risk**: Using unmaintained project = accumulating tech debt, unpatched vulnerabilities

### Fork & Ecosystem Health

**Metrics**:
- **Fork count**: Many forks = possible community fragmentation (example: OpenStack forks)
- **Popular forks**: Do forks have more activity than upstream? (sign of maintainer issues)
- **Upstream integration**: Do forks merge back improvements or diverge?
- **Ecosystem**: Are there compatible projects (replacements)?

**Scoring**:
- Green: <10 significant forks, minimal activity divergence
- Yellow: 10-50 forks, some with their own communities
- Red: 50+ forks, significant activity in alternative forks, upstream fragmenting

**Risk**: Choosing wrong fork = backwards incompatibility later

### Funding & Sustainability

**Metrics**:
- **Funding model**: Fully funded (Linux Foundation, Mozilla) vs unfunded
- **Sponsorship**: GitHub Sponsors, Open Collective support level
- **Commercial backing**: Company employs maintainers (example: JetBrains + Kotlin)
- **Funding source diversity**: Single funder vs multiple sponsors

**Scoring**:
- Green: Well-funded, diverse sponsors, dedicated maintainers
- Yellow: Some sponsorship, part-time maintainers
- Red: No funding, unpaid volunteers only, burnout signals

**Risk**: Unfunded projects risk maintainer burnout → project abandonment

### Maintainer Burnout Signals

**Red Flags**:
- **Communication**: Slow issue responses, frustrated tone in comments
- **Issues/PRs ignored**: Backlog growing, stale tags accumulating
- **Burnout language**: "I don't have time", "anyone take over?", disappearance
- **Forced vacation**: Maintainer suddenly inactive (good = real break; bad = disappeared)
- **Solo maintainer fatigue**: One person handling 1000+ issues

**Risk Mitigation**:
- Contribute back or sponsor (funds help hiring help)
- Use alternatives if critical signs detected
- Prepare internal fork if project is critical

## Health Scorecard Template

| Dimension | Score | Risk | Recommendation |
|-----------|-------|------|---|
| Bus Factor | Yellow | Single maintainer | Consider fork; contribute to project |
| Release Cadence | Green | None | Stable releases quarterly |
| Contributor Diversity | Green | None | Healthy ecosystem |
| Security | Yellow | CVEs take 45+ days | Monitor CVE announcements; test patches quickly |
| License | Green | None | MIT-compatible |
| Maintenance | Yellow | 20% issue resolution rate | Backlog growing; consider alternative |
| Fork/Ecosystem | Green | None | Upstream remains canonical |
| Funding | Red | Unfunded, unpaid volunteers | High burnout risk; consider alternative or fork |

## When to Use This Skill

- **Dependency evaluation**: Should we use this library? Is it maintained?
- **Build vs use decision**: Is OSS alternative healthy enough for production use?
- **Risk assessment**: Which of our 500 dependencies is at risk of abandonment?
- **Vendor selection**: Choosing between multiple open-source options
- **Acquisition analysis**: Acquiring company with custom forks; consolidate or maintain forks?
- **Sustainability planning**: Ensuring long-term reliability of critical dependencies
- **Sponsorship decisions**: Which projects does our org depend on; should we fund?

## Output Examples

- OSS health scorecard (traffic light: green/yellow/red per dimension)
- Risk register (critical dependencies with health scores, action items)
- Alternative recommendation (if primary choice is risky, suggest healthier options)
- Funding strategy (which projects to sponsor; ROI of sponsorship)
- Fork decision matrix (should we fork, contribute upstream, or switch alternatives?)

## Computational Workflows

### Pre-built Analysis Scripts

**bus_factor_calculator.py**: Analyzes GitHub repository commit distribution, code review patterns. Inputs: repository URL, time window (last 12 months). Outputs: top N contributors (% of commits), review concentration, truck factor estimate, risk score (red if >70% concentration on 1 person).

**release_cadence_tracker.py**: Mines GitHub releases API, git tags, PyPI/npm version history. Inputs: package name, source repository. Outputs: release frequency (releases/year), version bump patterns (semantic versioning check), time-to-patch for security fixes, deprecation timeline analysis.

**security_posture_analyzer.py**: Checks: CVE disclosure policy (GitHub security advisory), signed commits/releases, dependency scanning tools (Dependabot, Snyk), SLSA framework compliance. Outputs: security maturity score (1-5), vulnerability response time baseline, remediation recommendations.

**license_compliance_checker.py**: Parses LICENSE files, SPDX identifiers, dependency trees. Identifies: GPL/AGPL risks, license compatibility conflicts (Apache 2.0 + GPL issue?). Outputs: license risk matrix (green/yellow/red), legal review requirements, remediation path (relicensing, replacement library).

### Dynamic Computation Examples

1. **Dependency Risk Scorecard**: Input: list of 100+ dependencies (package.json, requirements.txt, Cargo.toml). For each: assess bus factor, release cadence, security posture. Output: risk scorecard (high-risk dependencies highlighted), alternatives list (healthier similar projects), remediation roadmap.

2. **Maintainer Burnout Risk Assessment**: Analyze: commit frequency decline, issue response time lengthening, contributor burnout language in issues. Compute: burnout risk score, sustainability prediction (will this project be maintained 2 years from now?), sponsorship recommendation.

3. **Fork vs Upstream Decision Engine**: Given critical project showing signs of abandonment, evaluate: fork risk (dev burden), alternative project options, contributing back to upstream. Output: decision matrix (fork/contribute/switch), cost/benefit analysis, timeline estimate.

### Output Artifacts

- **OSS Health Scorecard**: Traffic light per dimension (Bus Factor, Release Cadence, Contributor Diversity, Security, License, Maintenance Status, Funding) with risk assessment and recommendations
- **Dependency Risk Register**: All critical dependencies ranked by health score, action items (fork decision, alternative options, contribution plan), prioritized by usage importance
- **Security Vulnerability Timeline**: CVE history for top dependencies, response times, patch availability lag, upgrade urgency recommendations
- **Funding & Sustainability Analysis**: Funding sources, sponsorship options, ROI of funding (maintainer capacity increase, release frequency impact), contribution strategy

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub API for commit history, contributor analysis, repository health metrics
- **~~web research**: Open Collective funding data, maintainer sentiment analysis, project announcements

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: GitHub API (commit history, contributor analysis, dependency graph), CVE databases (NVD, OSV), FOSSA/Snyk (license/security scanning), Open Collective (funding data), Stack Overflow (sentiment analysis on project discussions)
