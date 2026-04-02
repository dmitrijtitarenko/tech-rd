---
description: Standards and compliance requirements
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [domain]
---

# Standards Command

Research current standards and compliance requirements for technology domains.

## Workflow

1. **Parse Domain Input**
   - Identify domain (e.g., "cloud security", "data protection", "API design")
   - Research applicable standards bodies

2. **Standards Bodies Research**
   - ISO (International Organization for Standardization)
   - W3C (World Wide Web Consortium)
   - IETF (Internet Engineering Task Force)
   - IEEE (Institute of Electrical and Electronics Engineers)
   - NIST (National Institute of Standards and Technology)
   - OWASP (Open Web Application Security Project)
   - CNCF (Cloud Native Computing Foundation)
   - Domain-specific bodies (e.g., PCI DSS for payment, HIPAA for healthcare)

3. **Standard Identification**
   - Search for all relevant standards in domain
   - Research standard designations (ISO 27001, RFC 3986, etc.)
   - Identify standard status: Draft, Active, Deprecated
   - Retrieve publication and last update dates

4. **Standard Details**
   - Scope: What does this standard cover?
   - Applicability: When/where is it required?
   - Compliance: How is compliance verified?
   - Cost: Licensing, certification, auditing expenses
   - Adoption: Industry acceptance level

5. **Compliance Requirements Mapping**
   - Regulatory requirements (legal mandate)
   - Industry best practices (competitive necessity)
   - Customer requirements (contractual obligations)
   - Security requirements (risk mitigation)

6. **Implementation Guidance**
   - Common approaches to achieve compliance
   - Tools and frameworks supporting compliance
   - Effort and timeline estimates
   - Common pitfalls and gotchas
   - Continuous monitoring/renewal requirements

7. **Output Structure**
   - Domain Overview: What domain and why standards matter
   - Standards Landscape Table:
     - Standard Name/Number
     - Status (Draft/Active/Deprecated)
     - Scope/Coverage
     - Maturity Level
     - Adoption Level
     - Compliance Effort
   - Regulatory vs Optional: Which are mandated vs recommended
   - Implementation Roadmap: Phased approach for compliance
   - Key Resources: Documentation, training, certification bodies
   - Timeline: Typical implementation and certification duration
   - Cost Estimate: Licensing, tools, audit, training

8. **Special Considerations**
   - Cross-border implications (EU, US, APAC differences)
   - Industry-specific mandates (finance, healthcare, etc.)
   - Evolving standards (track deprecation, new versions)
   - Conflicting requirements (how to reconcile)

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Focus on current standards (be specific about versions/years)
- Distinguish legal requirements from best practices
- Flag standards with significant implementation costs
- Provide links to official standard documentation
- Recommend implementation order (dependencies)
