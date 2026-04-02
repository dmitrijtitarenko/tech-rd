---
name: Cybersecurity Research
description: >
  CVEs, threat intelligence, zero-trust architecture, AppSec, SAST/DAST tools, supply chain security.
  Address "security audit", "vulnerability assessment", "CVE impact", "zero trust", "AppSec implementation", "supply chain security" questions.
  Evaluate CVE severity, exploit availability, patch status, attack surface, and breach risk.
  Essential for threat assessment, security architecture, and vulnerability management.
---

# Cybersecurity Research Domain

## Overview

Cybersecurity research synthesizes vulnerability data, threat intelligence, and architectural patterns to quantify risk and guide security decisions. This domain has matured from perimeter defense (firewalls) to zero-trust (assume breach, verify everything) and supply chain security (securing dependencies, not just code).

Effective research here means understanding: which CVEs actually pose risk to your architecture? How do threat actors exploit vulnerabilities in the wild? What security investments pay off in reduced breach probability?

## Key Research Dimensions

**Vulnerability Assessment**
- CVE severity scoring (CVSS v3.1 quantifies impact)
- Exploit availability: is this CVE exploited by attack tools?
- Patch status: can you easily update, or is it complex?
- Configuration factors: does vulnerability require specific setup?
- Practical exploitation difficulty: CVSS doesn't capture real-world effort

**Threat Intelligence**
- Active threat actors targeting your sector
- Attack patterns and techniques (MITRE ATT&CK framework)
- Exploit kits and tool availability
- Threat actor motivation: cybercriminals vs nation-state vs hacktivists
- Campaign analysis: how threats evolve and spread

**Application Security (AppSec)**
- SAST (Static Analysis): code review automation, false positive rates
- DAST (Dynamic Analysis): runtime testing, coverage of business logic
- Dependency scanning: vulnerable libraries in your supply chain
- Secrets detection: API keys, credentials in code repositories
- Code review practices: human review vs automated scanning

**Infrastructure Security**
- Zero-trust architecture: never trust, always verify
- Network segmentation: limiting lateral movement
- Identity and access management (IAM): principle of least privilege
- Encryption: at-rest and in-transit
- Logging and monitoring: detecting intrusions

**Supply Chain Security**
- Dependency vulnerability scanning (npm, pip, Maven, etc.)
- Software Bill of Materials (SBOM): tracking dependencies
- Build pipeline security: signed artifacts, attestation
- Third-party risk: vendor security posture assessment
- Open source license compliance

## Data Sources & Query Methods

**CVE & Vulnerability Databases**
- National Vulnerability Database (NVD) — authoritative CVE data, CVSS scores
- CISA Known Exploited Vulnerabilities catalog — CVEs actively exploited
- Exploit databases: Exploit-DB, Metasploit, PoC repositories
- Vendor security advisories: direct from affected vendor
- Query pattern: "CVE [number] impact", "vulnerability [software]"

**Threat Intelligence**
- MITRE ATT&CK framework — tactics, techniques, procedures (TTPs)
- Threat intelligence reports from security vendors (CrowdStrike, Mandiant, etc.)
- GitHub security advisories — vulnerability disclosure and reporting
- Security blogs from major tech companies (Google, Microsoft, Apple)
- Query pattern: "threat actor [name]", "attack technique [TTP]"

**AppSec Tool Evaluation**
- OWASP Top 10 and secure coding guidelines
- Tool comparison: SonarQube, Snyk, Checkmarx, Fortify
- GitHub security features: CodeQL, Dependabot, secret scanning
- Gartner Magic Quadrant for SAST/DAST tools
- Query pattern: "SAST tool comparison", "dependency vulnerability scanner"

**Supply Chain Security**
- SBOM standards: SPDX, CycloneDX, SWID
- Dependency tracking tools: Dependabot, Snyk, WhiteSource
- GitHub Advisory Database for vulnerability tracking
- Cloud provider supply chain tools: AWS artifact registry security scanning
- Query pattern: "software supply chain risk", "open source vulnerability"

**Compliance & Standards**
- CIS Controls for security benchmarks
- ISO 27001 for information security management
- SOC2 Type II audit results
- Regulatory requirements: PCI-DSS, HIPAA, GDPR
- Query pattern: "compliance requirement [regulation]", "security standard"

## Analysis Frameworks

**CVE Risk Assessment Matrix**
- **CVSS Score**: 0-3.9 (low), 4-6.9 (medium), 7-8.9 (high), 9-10 (critical)
- **Exploitability**: 0 (none) to 3.3 (high)
- **Impact**: Confidentiality, Integrity, Availability affected?
- **Your Exposure**: Is vulnerable component exposed to untrusted input?
- **Patching Effort**: Can you update safely without breaking dependencies?

**Threat Actor Profiling**
- **Motivation**: Financial gain, espionage, activism, geopolitical
- **Capability**: Script kiddies vs organized crime vs nation-state
- **Target selectivity**: Random vs industry-specific vs company-specific
- **Timeline**: How fast do they move from discovery to exploitation?
- **Detection difficulty**: Noisy attacks vs stealthy campaigns

**AppSec Investment ROI**
- **Risk reduction**: Which security improvements reduce breach probability most?
- **Cost**: Tool licensing, team training, process overhead
- **Coverage**: % of attack surface covered by each tool
- **False positive rate**: How much time wasted on non-issues?
- **Integration**: Can tools plug into existing CI/CD?

**Zero-Trust Architecture Assessment**
- **Identity**: Can you verify every user, device, and service?
- **Network**: Can you segment traffic to prevent lateral movement?
- **Data**: Can you encrypt and protect sensitive data at rest/in-transit?
- **Monitoring**: Can you detect suspicious behavior in real-time?
- **Maturity**: What's the incremental path from current state?

**Supply Chain Risk Scoring**
- **Dependency count**: More dependencies = larger attack surface
- **Maintenance**: Is library actively maintained? Abandoned projects more likely compromised
- **Vulnerability history**: Does library have history of security issues?
- **Threat modeling**: What would attacker gain from compromising this library?
- **Alternatives**: Are less risky alternatives available?

## Output Format Templates

### CVE Impact Assessment
```
CVE ID: [CVE-XXXX-XXXXX]
Severity: [CVSS Score + Category]
Affected Software: [product, version ranges]

Exploitability: [is public PoC available?]
Your Exposure: [does your environment match vulnerability conditions?]
Blast Radius: [if exploited, what can attacker do?]
Patch Status: [available, timeline, breaking changes?]
Workarounds: [if patch not immediately available]
Recommendation: [urgent patch, monitor, or acceptable risk]
```

### Threat Assessment
```
Threat Landscape: [your industry and company size]
Primary Threat Actors: [which groups target you]
Attack Patterns: [most likely techniques]
Historical Incidents: [previous breaches in your sector]

Risk Profile: [high/medium/low for each TTP]
Detection Capability: [can you identify these attacks?]
Response Readiness: [can you contain/remediate quickly?]
Investment Priorities: [which defenses matter most]
```

### AppSec Program Design
```
Current State: [existing security practices]
Target Capability: [AppSec maturity level]

Tool Stack: [SAST, DAST, dependency scanner, secrets detection]
Integration: [where tools fit in CI/CD pipeline]
Process: [code review requirements, approval workflows]
Training: [team education, secure coding practices]
Metrics: [what success looks like]

Implementation Timeline: [phases, team effort]
Quick Wins: [start here for fast wins]
Long-term Investments: [capability buildout]
```

### Supply Chain Security Strategy
```
Current Dependencies: [# of direct and transitive]
Vulnerability Status: [# with known CVEs, unpatched count]

Dependency Management: [automated updates, testing]
SBOM Generation: [format, maintenance]
Vendor Assessment: [critical suppliers, risk scoring]
Build Pipeline Security: [artifact signing, attestation]
Incident Response: [if supply chain compromise detected]
```

## Key Metrics to Always Collect

For cybersecurity decisions, track:
1. **Vulnerability metrics**: Total CVEs, unpatched count, CVSS distribution
2. **Exposure**: Services exposed to untrusted input, default credentials, unencrypted data
3. **Patch management**: Mean time to patch critical CVEs, update compliance rate
4. **Threat indicators**: Suspicious network traffic, failed auth attempts, policy violations
5. **Incident metrics**: Detection time, response time, impact (if breached)
6. **Code quality**: Security scan findings, false positive rate, remediation rate

## Computational Workflows

**Pre-built Analysis Scripts**
- `cve_risk_scorer.py` — Compute weighted risk score from CVSS, exploitability, exposure, patch difficulty using pandas
- `vulnerability_severity_analyzer.py` — Aggregate CVE counts by severity and calculate remediation priority using numpy
- `mttr_distribution_modeler.py` — Analyze mean time to remediate across vulnerability types with scipy distributions
- `threat_actor_probability_calculator.py` — Estimate breach probability by sector/company size using Bayesian models

**Dynamic Computation Examples**
- When assessing CVE risk, compute exposure score accounting for network exposure and patch complexity weighted by CVSS
- When building AppSec metrics, calculate false positive rates across SAST tools to optimize signal-to-noise
- When prioritizing security investments, run Monte Carlo simulation on incident likelihood vs mitigation cost

**Output Artifacts**
- Vulnerability severity distribution histogram (counts by CVSS category with remediation timeline)
- Risk heatmap (axes: vulnerability count vs patch difficulty, color: business impact)
- MTTR comparison bar chart across vulnerability categories with confidence intervals
- Mermaid threat model diagram (assets, threats, mitigations)
- LaTeX formula: Risk_Score = CVSS * (Exploitability * Exposure) / Patch_Difficulty, normalized 0-100

## References

Load from `references/` directory:
- `cve-severity-guide.md` — interpreting CVSS and real-world risk
- `mitre-attck-tactics.md` — threat actor techniques and detection strategies
- `appsec-tool-comparison.md` — SAST vs DAST vs SCA features and tradeoffs
- `zero-trust-implementation.md` — architectural patterns and best practices
- `supply-chain-security-sbom.md` — SBOM standards and dependency management
- `threat-intelligence-sources.md` — where to find actionable threat data

## Common Pitfalls to Avoid

- **CVSS overreliance**: High CVSS doesn't mean it affects you; check configuration
- **Tool proliferation**: SAST + DAST + scanner + secrets detection creates alert fatigue
- **False confidence**: Running security tools doesn't mean you're secure (coverage and fixes matter)
- **Patch hesitation**: Waiting for perfect moment to patch creates risk window
- **Threat actor assumptions**: Assuming only sophisticated attackers creates blind spots
- **Supply chain blindness**: Trusting open source without scanning introduces risk
- **Alert fatigue**: Alerting on low-severity issues creates noise that hides real threats

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~source control**: GitHub security advisories, dependency scanning results, vulnerability tracking
- **~~monitoring**: Real-time vulnerability alerts, CVE monitoring feeds, threat intelligence updates
- **~~web research**: Latest CVE disclosures, security research publications, exploit availability data

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
