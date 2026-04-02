---
name: standards-tracker
description: >
  Monitors standards evolution and compliance requirements from ISO, W3C, IETF, IEEE,
  NIST, OWASP, CNCF. Tracks status (draft/active/deprecated), impact analysis, compliance
  requirements. Triggered by "standards compliance", "ISO certification", "W3C standards",
  "NIST framework", "OWASP top 10". Outputs standards landscape report with roadmap.
---

## Overview

This skill helps organizations track technical standards, understand compliance implications, and plan adoption roadmaps. It connects abstract standards to concrete implementation requirements and competitive advantage.

## Standards Organizations & Domains

### ISO (International Organization for Standardization)
- **ISO 9001**: Quality management systems
- **ISO 27001**: Information security management
- **ISO 27002**: Information security code of practice
- **ISO/IEC 27035**: Incident management
- **ISO/IEC 42001**: AI risk management (emerging 2024)

**Relevance**: Certification signal for enterprise buyers; compliance requirement for regulated industries

### W3C (World Wide Web Consortium)
- **HTML5**: Current web standard (living standard model, not versioned)
- **CSS3+**: Styling (CSS4 under development; modular specifications)
- **WebAssembly**: Binary format for browser execution
- **Web Authentication**: FIDO2, passwordless authentication
- **Web Accessibility Guidelines (WCAG)**: A11y conformance levels (A, AA, AAA)

**Relevance**: Ensures cross-browser compatibility, accessibility, modern web capabilities

### IETF (Internet Engineering Task Force)
- **RFC 3986**: URI syntax
- **RFC 6749**: OAuth 2.0 authorization
- **RFC 8446**: TLS 1.3 (current cryptographic standard)
- **RFC 9000**: QUIC protocol (HTTP/3 foundation)
- **RFC 9110**: HTTP Semantics (HTTP/1.1, 2.0 consolidation)

**Relevance**: Protocol standards; security/authentication patterns; interoperability

### IEEE (Institute of Electrical and Electronics Engineers)
- **IEEE 802.11**: Wireless (WiFi standards)
- **IEEE 802.1X**: Network access control (port-based authentication)
- **IEEE 1016**: Software design
- **IEEE 12207**: Software lifecycle processes

**Relevance**: Hardware/networking standards; processes for critical systems

### NIST (National Institute of Standards & Technology)
- **NIST Cybersecurity Framework**: 5 functions (Identify, Protect, Detect, Respond, Recover)
- **NIST SP 800-53**: Security and privacy controls for federal systems
- **NIST SP 800-171**: Protecting Controlled Unclassified Information (CUI)
- **FIPS 140-3**: Cryptographic module validation

**Relevance**: US federal compliance; critical infrastructure; cryptographic standards

### OWASP (Open Web Application Security Project)
- **OWASP Top 10 2021**: Most critical web application risks
  - A01: Broken Access Control
  - A02: Cryptographic Failures
  - A03: Injection
  - A04: Insecure Design
  - A05: Security Misconfiguration
  - A06: Vulnerable & Outdated Components
  - A07: Authentication Failures
  - A08: Data Integrity Failures
  - A09: Logging & Monitoring Failures
  - A10: SSRF
- **OWASP API Top 10**: API-specific risks
- **OWASP Dependency-Check**: Vulnerability scanner

**Relevance**: Application security assessment, remediation prioritization

### CNCF (Cloud Native Computing Foundation)
- **Kubernetes**: Container orchestration (de facto standard)
- **Service Mesh Interface**: Standardizing service mesh APIs
- **CloudEvents**: Event format specification
- **OpenTelemetry**: Observability standards (traces, metrics, logs)
- **CertManager**: Certificate management standards

**Relevance**: Cloud-native architecture, microservices, Kubernetes ecosystem

## Standards Tracking Model

### Status Tracking

**Lifecycle Stages**:
- **Draft**: Early proposals (RFC with 0- prefix); high volatility
- **Proposed**: Community consensus emerging; may change
- **Active**: Published, stable; safe to adopt
- **Deprecated**: Replaced by newer standard; migrate off timeline defined
- **Obsolete**: No longer relevant; remove from systems

**Example Tracking**:

| Standard | Version | Status | Adoption | Deadline |
|----------|---------|--------|----------|----------|
| TLS | 1.2 | Deprecated | 2023+ | EOL Jan 2024 |
| TLS | 1.3 | Active | 2018+ | Adopt by 2024 |
| OWASP Top 10 | 2021 | Active | 2021+ | Baseline for 2024 |
| ISO 27001 | 2022 | Active | 2022+ | Certification target |
| OAuth 2.0 | 2.0 | Active | 2012+ | Legacy; OAuth 2.1 in progress |
| OAuth 2.1 | 2.1 (draft) | Draft | Early adopters | Monitor; adopt 2024 |

### Impact Analysis

**Dimensions**:
- **Scope**: Which systems affected? (all APIs, payments only, internal tools)
- **Effort**: How much work to comply? (days vs months vs quarters)
- **Timeline**: When compliance required? (immediately vs 12-month grace period)
- **Cost**: Licensing, training, tooling, architectural changes
- **Risk**: Non-compliance consequences (customer trust, legal liability, SLAs)

**Example: TLS 1.3 Adoption**
- Scope: All customer-facing APIs + internal services (critical)
- Effort: 2-4 weeks per service (certificate renewal, load balancer config)
- Timeline: Most payment processors now require TLS 1.3+; critical by Q4 2024
- Cost: Certificate renewal, load balancer upgrades (~$50K one-time infra cost)
- Risk: PCI-DSS non-compliance; payment processing failure; customer data exposure

### Compliance Requirements

**Regulatory Mapping**:

| Regulation | Standards Applied | Scope |
|-----------|---|---|
| HIPAA (healthcare) | NIST SP 800-88 (encryption), ISO 27001, FIPS 140-3 | Data at rest/transit encryption |
| PCI-DSS (payments) | OWASP, TLS 1.2+, FIPS 140-2 | Cardholder data protection |
| GDPR (EU privacy) | ISO 27001, NIST CSF | Data protection, breach notification |
| SOC 2 Type II | ISO 27001 aligned | Security controls certification |
| FedRAMP (US federal) | NIST SP 800-53 | 300+ security controls |

**Compliance Roadmap**:
1. Identify applicable regulations (HIPAA, PCI-DSS, SOC 2, GDPR)
2. Map to specific standards (ISO 27001 for information security)
3. Gap analysis (what we have vs. required)
4. Remediation plan (priority, timeline, owner)
5. Audit/certification (external validation)

## Standards Adoption Strategy

### Quick Wins (Low Effort, High Impact)
- OAuth 2.0 for API authentication (replaces in-house auth)
- OWASP Top 10 checklist for application security
- WCAG 2.1 AA for web accessibility
- CloudEvents for event standardization

### Strategic Investments (Medium Effort, High Impact)
- ISO 27001 certification (3-6 months, $50-200K)
- NIST Cybersecurity Framework adoption (6-12 months)
- OpenTelemetry migration (observability standardization, 2-3 months)
- Kubernetes as standard orchestration (6-12 months, vendor support benefit)

### Watch & Learn (Monitor, Adopt Later)
- OAuth 2.1 (final draft expected 2024)
- ISO/IEC 42001 (AI governance; early stage 2024)
- SLSA framework (supply chain security; emerging)
- CertManager for certificate lifecycle (not yet industry standard)

## When to Use This Skill

- **Compliance roadmap planning**: Which standards apply to our business?
- **Audit preparation**: Standards documentation for certifications
- **Technology selection**: Does this tool/platform meet relevant standards?
- **Security assessment**: Are we following OWASP/NIST guidance?
- **Regulatory response**: New regulation announced; what's the compliance path?
- **Customer requirements**: Enterprise buyer requesting SOC2/ISO27001 compliance
- **Supply chain security**: SLSA framework adoption for artifact signing

## Output Examples

- Standards landscape report (applicable standards per domain: security, web, cloud)
- Compliance matrix (standards vs. current state vs. target state)
- Gap analysis with remediation roadmap (priority, effort, timeline, cost)
- Certification roadmap (ISO 27001, SOC2, FedRAMP timeline)
- Technology selection checklist (evaluating tools against standards requirements)
- Audit readiness report (evidence collection for certification body)

## Computational Workflows

### Pre-built Analysis Scripts

**standards_gap_analyzer.py**: Maps current system against standards checklist (OWASP Top 10, NIST SP 800-53, ISO 27001 controls). Inputs: security audit results, compliance status. Outputs: gap matrix (implemented vs required), severity ranking (critical/high/medium/low), remediation effort estimate per gap.

**compliance_roadmap_generator.py**: Generates phased implementation plan. Inputs: applicable standards, current state, target deadline. Outputs: milestone timeline (0-3 month quick wins, 3-6 month strategic, 6-12 month long-term), resource allocation, cost estimate per phase.

**standards_status_tracker.py**: Monitors RFC/standard status changes. Parses W3C, IETF, ISO updates. Tracks: draft → proposed → active → deprecated transitions. Outputs: upcoming EOL alerts (TLS 1.2 January 2024 EOL), new standards recommended for adoption, deprecation timeline.

**certification_audit_readiness_scorer.py**: Checks readiness for SOC2/ISO27001 certification. Audits: evidence collection, control implementation, policy documentation. Outputs: readiness percentage, gap items blocking certification, remediation priority, audit timeline estimate.

### Dynamic Computation Examples

1. **Compliance Cost-Benefit Analysis**: Input: target standards (HIPAA, PCI-DSS, SOC2), implementation cost per standard, time-to-certification. Compute: ROI by standard (customer value, competitive advantage), cumulative cost, prioritized adoption sequence. Output: standards selection roadmap (implement high-ROI first).

2. **Standards Version Migration Impact**: Given standard version upgrade (OAuth 2.0 → 2.1, TLS 1.2 → 1.3), compute: breaking change impact, affected systems, migration complexity, timeline. Output: phased migration plan, risk assessment, rollback strategy.

3. **Regulatory Compliance Requirement Mapping**: Input: target market geography and regulations (GDPR, CCPA, HIPAA). Map: required standards per regulation. Output: combined compliance roadmap (avoid redundant work), overlap analysis (GDPR and ISO 27001 control alignment).

### Output Artifacts

- **Standards Compliance Matrix**: Applicable standards (per domain: security, web, cloud, privacy) vs current state (not implemented, partial, complete), gap severity
- **Compliance Roadmap Gantt Chart**: Phases (0-3 month, 3-6 month, 6-12 month) with standards adoption sequence, resource allocation, milestone gates
- **Regulatory Mapping Table**: Regulations applicable (GDPR, HIPAA, PCI-DSS, SOC2) linked to implementing standards (ISO 27001, NIST CSF, OWASP), overlap analysis
- **Certification Readiness Dashboard**: Evidence collection percentage, control implementation status, gap items blocking certification, expected audit timeline

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~web research**: Standards body updates (W3C, IETF RFCs), regulatory announcements, compliance guidance
- **~~research**: Academic standards, emerging specifications, technical working groups

Replace `~~category` with your configured MCP server (see CONNECTORS.md).

---

**Supercharged By**: Regulatory databases (ISO catalog, RFC repositories), certification tracking (SOC2 audit status), standards body RSS feeds (W3C, IETF updates), compliance tools (audit logging, policy automation)
