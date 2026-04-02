---
name: Biotech & HealthTech Research
description: >
  Digital health, EHR interoperability (FHIR/HL7), FDA software guidance, genomics platforms, telemedicine.
  Address "healthtech for", "digital health platform", "EHR integration", "FHIR", "FDA software", "genomics platform" questions.
  Evaluate regulatory pathway, interoperability, clinical validation, data privacy, and integration complexity.
  Critical for healthcare technology and regulated medical device products.
---

# Biotech & HealthTech Research Domain

## Overview

Biotech and HealthTech research synthesizes healthcare informatics, regulatory frameworks, and clinical science to understand how technology improves patient outcomes and healthcare operations. This domain encompasses digital health platforms, electronic health records (EHR), genomics, telemedicine, and FDA-regulated medical software.

Effective research here means understanding: which FDA pathway applies to your product? How do FHIR standards enable EHR interoperability? What clinical evidence does the FDA require?

## Key Research Dimensions

**Digital Health & Telemedicine**
- Telemedicine platforms: Asynchronous, synchronous, store-and-forward
- Regulatory requirements: State licensure, cross-state practice, reimbursement
- Reimbursement models: Insurance coverage, out-of-pocket, subscription
- Compliance: HIPAA, state privacy laws, ADA accessibility
- Clinical workflow: Integration with EHR, prescription, referral systems
- Patient engagement: Medication adherence, preventive care
- Technology stack: Video, scheduling, EHR integration, compliance

**EHR Interoperability & Standards**
- FHIR (Fast Healthcare Interoperability Resources): Modern RESTful standard
- HL7 v2: Legacy EDI standard, still widely used
- CCD (Continuity of Care Document): XSD for care summaries
- DICOM: Medical imaging standard
- Integrations: How data flows between EHR systems
- Information blocking: ONC rules preventing interoperability
- Data exchange networks: CommonWell, eHealth Exchange

**FDA Regulatory Pathways**
- Software as a Medical Device (SaMD): When software is regulated
- Classification: Class I (lowest risk), Class II, Class III (highest risk)
- 510(k) pathway: Predicate device comparison, most common
- PMA (Premarket Approval): Highest risk, full clinical trial required
- De Novo: Pathway for novel devices with no predicate
- Breakthrough devices: Expedited pathway for innovative products
- Post-market: Adverse event reporting, recalls, surveillance

**Genomics & Precision Medicine**
- Genomic testing: DNA sequencing, variant calling, interpretation
- Variant databases: ClinVar, gnomAD for variant assessment
- Interpretation standards: ACMG guidelines for pathogenicity
- Testing companies: Myriad, Invitae, Foundation Medicine business models
- Data integration: Genomic data in EHR
- Privacy: Genetic data sensitivity, special consent requirements
- Reimbursement: Coverage for different genetic tests

**Clinical Validation & Evidence**
- Real-world evidence (RWE): Data from clinical practice
- Randomized controlled trials (RCTs): Gold standard for effectiveness
- Validation requirements: By FDA, payers, clinical practice
- Retrospective vs prospective: Study design implications
- Bias sources: Selection bias, unmeasured confounding
- Sample size: Statistical power and recruitment
- Cost and timeline: Clinical studies take years and millions

**Data Privacy & HIPAA Compliance**
- HIPAA requirements: Privacy Rule, Security Rule, Breach Notification
- PHI (Protected Health Information): Identifiable health data
- De-identification: Removing PHI to enable research
- Authorization: Patient consent for data use
- Business Associate Agreements (BAA): Required for vendors
- State privacy laws: Additional restrictions beyond HIPAA
- International: GDPR for EU patient data

## Data Sources & Query Methods

**FDA & Regulatory Information**
- FDA CDRH database: Medical device classifications and clearances
- FDA guidance documents: SaMD guidance, 510(k) submission guides
- 510(k) predicate device searches: Finding comparable cleared products
- Adverse Event Reporting System (FAERS): Post-market safety data
- Recalls and enforcement actions: FDA public database
- Query pattern: "FDA clearance [device type]", "SaMD regulatory pathway"

**Clinical Evidence & Validation**
- PubMed: Peer-reviewed medical literature searches
- ClinicalTrials.gov: Active and completed studies database
- Cochrane Reviews: Systematic reviews and meta-analyses
- Real-world data: Patient registry data, EHR-derived evidence
- Query pattern: "clinical evidence [condition]", "healthcare technology effectiveness"

**EHR & Interoperability Standards**
- HL7 FHIR specification: Official standard documentation
- CommonWell and eHealth Exchange: Data exchange network info
- EHR vendor APIs: Cerner, Epic, Athena documentation
- ONC regulations: Federal requirements for information blocking
- Query pattern: "FHIR implementation", "EHR integration [vendor]"

**Healthcare Reimbursement**
- CMS.gov: Medicare coverage and billing codes
- CPT codes: Procedure and service coding (AMA)
- ICD-10 codes: Diagnosis coding
- Payer policies: Commercial insurance coverage requirements
- Query pattern: "Medicare reimbursement [service]", "insurance coverage"

**Genomics & Precision Medicine**
- ClinVar: NCBI variant-phenotype database
- gnomAD: Population variant frequencies
- ACMG guidelines: Variant classification standards
- Genomic testing company coverage: Insurance reimbursement
- Query pattern: "genomic testing reimbursement", "variant interpretation"

## Analysis Frameworks

**FDA Regulatory Pathway Selection**
- **Is software a medical device?** (Does it diagnose, treat, prevent, monitor disease?)
- **Intended use**: What specific clinical function?
- **Risk classification**: I (simple checklist), II (moderate, 510(k) typical), III (high, PMA)
- **Predicate devices**: Can you find comparable cleared product?
- **Novel functionality**: No predicate = De Novo pathway (longer, more complex)
- **Breakthrough designation**: Does FDA consider innovative?
- **Timeline**: 510(k) months vs PMA years
- **Cost**: 510(k) hundreds of thousands vs PMA millions

**Clinical Validation Plan**
- **Data sources**: Real-world data vs RCT vs retrospective chart review?
- **Sample size**: Statistical power needed for claims?
- **Study duration**: Timeline realistic for business plan?
- **Endpoints**: What outcomes prove safety/effectiveness?
- **Confounding**: Can you control for alternative explanations?
- **Bias**: Selection bias, measurement bias risks?
- **Budget**: Realistic cost and timeline estimates

**EHR Integration Strategy**
- **Standard**: FHIR (modern), HL7 v2 (legacy), or direct?
- **Vendors**: Which EHRs must you support? (Epic, Cerner, Athena, others)
- **APIs**: Are vendors' APIs available and mature?
- **Data flows**: Direction of data (pull, push, real-time)?
- **Data types**: Which data elements needed from EHR?
- **Compliance**: Can integration maintain HIPAA compliance?
- **Timeline**: How long to integrate with target EHRs?

**Healthcare Business Model Viability**
- **Revenue source**: Payer, patient, provider, or combination?
- **Reimbursement**: Will insurance cover your service?
- **Competitive advantage**: Why would customers choose you?
- **Market size**: How many potential patients/providers?
- **Customer acquisition**: How will you reach users?
- **Unit economics**: Revenue per user vs acquisition + support cost?
- **Sustainability**: Can you reach profitability on current model?

**Genomic Testing Feasibility**
- **Testing type**: Germline or somatic? Targeted or whole-genome?
- **Laboratory**: Build or partner with CLIA-certified lab?
- **Interpretation**: In-house variant calling or use service?
- **Reporting**: Clinical reports that meet medical standard?
- **Reimbursement**: Payer coverage for your test?
- **Accreditation**: CLIA certification, CAP accreditation needed
- **Data privacy**: Genetic data is especially sensitive; extra protections
- **Scale**: Sequencing cost per sample at volume?

## Output Format Templates

### FDA Regulatory Strategy
```
Product: [software description, intended use]
Clinical Application: [specific diagnosis/treatment/monitoring]

Is it a Medical Device?: [yes/no, reasoning]
Risk Classification: [I/II/III likely]
Comparable Devices: [510(k) predicate candidates]
Regulatory Pathway: [510(k)/PMA/De Novo/general wellness]

Clinical Evidence Needed: [study design, sample size, endpoints]
Timeline to Clearance: [months realistic]
Budget: [estimated regulatory costs]
Post-Market: [adverse event monitoring, registries]

Go/No-Go Decision: [is regulatory pathway feasible?]
```

### Clinical Validation Study Design
```
Product: [technology being validated]
Clinical Question: [what do you need to prove?]

Study Type: [RCT, retrospective, prospective observational]
Study Population: [inclusion/exclusion criteria]
Sample Size: [power calculation, required N]
Duration: [months/years to complete]

Primary Endpoint: [what success looks like]
Secondary Endpoints: [additional outcomes]
Safety Monitoring: [adverse event tracking]
Statistical Plan: [analysis approach]

Budget: [estimated cost]
Timeline: [enrollment period, analysis, publication]
Bias Control: [addressing confounders, selection bias]
```

### EHR Integration Implementation
```
Target EHRs: [Epic, Cerner, Athena, others]
Data Elements: [which EHR data needed]

Integration Standard: [FHIR/HL7/direct/other]
Approach: [pull, push, real-time, batch]
API Assessment: [are vendor APIs available?]

Technical Architecture: [how data flows between systems]
HIPAA Compliance: [security controls, BAA requirements]
Testing: [validation that data transfers correctly]

Timeline per EHR: [months to integration, testing, go-live]
Maintenance: [ongoing support, API updates]
Scaling: [can architecture handle growth?]
```

### Telemedicine Platform Strategy
```
Clinical Service: [what clinical services via telemedicine?]
Target Market: [patient population, geography]

Regulatory Requirements: [state licensure, insurance, compliance]
Reimbursement Model: [insurance, patient-pay, subscription]
Clinical Workflow: [how integrated with in-person care?]

Technology Stack: [video platform, scheduling, EHR integration]
Compliance Approach: [HIPAA, state privacy, accessibility]
User Experience: [patient, provider, admin workflows]

Go-to-Market: [customer acquisition strategy]
Unit Economics: [revenue per patient, cost per consultation]
Scaling: [how to add providers, expand geographies]
```

## Key Metrics to Always Collect

For HealthTech decisions, track:
1. **Regulatory**: Pathway timeline, approval/clearance timeline, post-market requirements
2. **Clinical**: Safety events, effectiveness outcomes, real-world performance
3. **Interoperability**: % of target EHRs integrated, data exchange rate, latency
4. **Compliance**: HIPAA violations, audit findings, patient consent rate
5. **Market**: Patient adoption, provider adoption, insurance coverage rate
6. **Financial**: Reimbursement rate, per-patient cost, revenue per user
7. **Evidence**: Publication record, citation count, real-world data accumulation

## Computational Workflows

**Pre-built Analysis Scripts**
- `clinical_trial_power_calculator.py` — Estimate required sample size given effect size and statistical power using scipy.stats
- `fda_timeline_projector.py` — Model FDA submission timeline (510k vs PMA) from control complexity and predicate device availability
- `drug_pipeline_probability_model.py` — Calculate expected pipeline value accounting for phase transition probabilities and failure rates
- `ehr_integration_effort_estimator.py` — Estimate development effort across EHR vendors based on API maturity and data complexity

**Dynamic Computation Examples**
- When planning clinical validation, compute required sample size and study duration from efficacy assumptions
- When assessing regulatory pathway, estimate timeline and cost for 510k vs PMA based on control novelty
- When modeling revenue, run Monte Carlo simulation on clinical success rates, reimbursement coverage, and market adoption

**Output Artifacts**
- Clinical trial power analysis table (effect size x sample size with alpha/beta specified)
- FDA pathway timeline comparison (Gantt: 510k vs PMA with critical path and decision points)
- Drug pipeline valuation chart (bar: expected value per stage with success probability weighting)
- Mermaid flowchart showing regulatory pathway selection for medical device software
- LaTeX formula: Pipeline_Value = Sum(Stage_Revenue * Success_Probability_To_Stage / Discount_Factor^Years)

## References

Load from `references/` directory:
- `fda-samd-guidance-2024.md` — software as medical device regulatory pathways
- `fhir-implementation-guide.md` — standards for EHR interoperability
- `clinical-validation-framework.md` — study design and statistical considerations
- `hipaa-compliance-checklist.md` — privacy and security requirements
- `genomic-testing-landscape.md` — testing types, reimbursement, precision medicine
- `telemedicine-reimbursement-2024.md` — coverage by payer and service type
- `ehr-vendor-api-comparison.md` — Epic, Cerner, Athena integration approaches

## Common Pitfalls to Avoid

- **FDA surprise**: Assuming your software isn't a medical device (most healthcare software is)
- **Predicate blindness**: Finding predicate device harder than expected; affects timeline
- **Clinical evidence gap**: Real-world data insufficient for FDA; randomized trial needed
- **EHR integration myth**: "We'll integrate with Epic" much harder than expected (API access, certification)
- **HIPAA false confidence**: De-identified data isn't truly anonymous; re-identification possible
- **Reimbursement assumption**: Your product not covered by insurance requires out-of-pocket sales
- **Telemedicine state complexity**: State-by-state licensure, telehealth practice rules vary widely
- **Genomic data liability**: Incidental findings, uncertain variants create medical-legal risk
- **Patient enrollment difficulty**: Healthcare studies take longer and cost more than expected
- **Vendor change surprise**: EHR vendors deprecate APIs or implement breaking changes

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~research**: Clinical trial databases, medical literature, genomic research databases
- **~~web research**: FDA guidance updates, regulatory announcements, reimbursement policy changes
- **~~source control**: Open-source FHIR implementations, healthcare interoperability standards

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
