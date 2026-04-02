---
name: FinTech Research
description: >
  Payments, neobanking, insurance tech, trading infrastructure, DeFi integration, open banking, PSD2.
  Address "fintech solution for", "payment processing", "neobank architecture", "trading system", "open banking" questions.
  Evaluate transaction latency, regulatory compliance, fraud detection, scalability, and settlement mechanisms.
  Critical for financial technology products and payment platforms.
---

# FinTech Research Domain

## Overview

FinTech research synthesizes financial infrastructure, regulatory frameworks, and technology platforms to understand how digital tools reshape financial services. This domain encompasses payments (traditional and crypto), neobanking (digital-only banks), insurance tech, trading infrastructure, and open banking (PSD2, Open Finance).

Effective research here means understanding: which payment processors meet your compliance and volume requirements? How do settlement mechanisms affect liquidity? What's the real cost of compliance for different business models?

## Key Research Dimensions

**Payment Infrastructure**
- Payment networks: Visa, Mastercard, ACH, SWIFT, Fedwire
- Settlement models: Batch, real-time, T+N clearing
- Payment methods: Cards, bank transfers, digital wallets, mobile payments
- Processing fees: Interchange, assessment, processor markup, gateway fees
- Compliance: PCI-DSS Level, KYC/AML requirements
- Fraud detection: Rules-based, ML-based, real-time monitoring
- Geographic coverage: Which payment methods available in target markets?

**Neobanking & Digital Banking**
- Deposit insurance: FDIC (US), equivalent in other regions
- Regulatory approach: Charter vs non-bank (constrained activities)
- Core banking system: Temenos, Fintech-specific, or in-house
- Customer acquisition cost (CAC): How expensive to get customers?
- Retention: Account abandonment rates, revenue per user
- Services: Just payments, or lending, savings, wealth management?
- Partnerships: Banking-as-a-service vs independent bank

**Open Banking & PSD2/Open Finance**
- PSD2 (Payment Services Directive 2): EU regulation enabling third-party access
- Open Banking API standards: UK, EU, Australia, Singapore variations
- Third-party provider (TPP) access: Account information, payment initiation
- Competitive dynamics: Banks vs FinTechs vs mega-platforms
- Revenue models: Interchange, subscription, data monetization
- Interoperability: Can TPPs work across bank APIs?
- Data residency: Where customer financial data can reside

**Trading Infrastructure**
- Market data: Real-time vs delayed, cost, latency sensitivity
- Order execution: Direct market access (DMA), broker-hosted
- Settlement: T+2 (traditional stocks) vs T+0 (crypto)
- Custody: Where assets held, counterparty risk
- Regulatory requirements: Pattern day trader rules, margin rules
- Trading platform architecture: Latency-sensitive systems
- Risk management: Position monitoring, margin calls

**Insurance Tech (InsurTech)**
- Digital underwriting: How to assess risk without manual review?
- Claims automation: Can AI process claims without human interaction?
- Fraud detection: False claims identification
- Customer acquisition: Online distribution channels
- Regulatory licensing: Insurance licenses by state/country
- Reinsurance integration: How to transfer risk?
- Ecosystem partnerships: APIs for broker integration

**Fraud Detection & AML/KYC**
- KYC (Know Your Customer): Identity verification on account opening
- AML (Anti-Money Laundering): Transaction monitoring and reporting
- Sanctions screening: Checking against OFAC, international lists
- False positive rate: How many legitimate transactions flagged?
- Detection latency: Real-time vs batch analysis
- Machine learning: Behavioral analysis, anomaly detection
- Regulatory reporting: Suspicious Activity Reports (SARs) requirements

## Data Sources & Query Methods

**Payment Industry Data**
- Nilson Report: Payment transaction volumes and trends
- FIS/Fiserv reports: Payment system market analysis
- Interchange rates: Published by card networks, varies by region/type
- Processor pricing: Stripe, Square, PayPal public pricing
- Query pattern: "payment processing cost comparison", "interchange rates"

**Neobanking & Digital Banking**
- Y Combinator database: Recent neobank startups and metrics
- CB Insights: Neobank funding, customer counts, valuations
- Reports: McKinsey, BCG on digital banking trends
- Public companies: Chime, SoFi financials and metrics
- Query pattern: "neobank market", "digital banking trends"

**Open Banking & PSD2**
- Open Banking Implementation Entity (OBIE): UK standards
- European Banking Authority (EBA): PSD2 guidance
- FinTech ecosystem reports: VC/PE trends in open banking
- API comparisons: Major banks' API capabilities
- Query pattern: "open banking PSD2", "API banking integration"

**Regulatory & Compliance**
- FFIEC guidance: Federal Financial Institutions Examination Council
- OCC/Fed/FDIC guidance: Banking regulator requirements
- CFTC: Futures and derivatives regulation
- FinCEN: AML/KYC requirements and reporting
- Query pattern: "fintech regulatory requirements", "money transmitter license"

**Fraud & AML Data**
- Fraud statistics: Prevalence by transaction type
- Case studies: How fraud was detected and prevented
- Machine learning research: AML/fraud detection papers
- Sanctions: OFAC list updates and trends
- Query pattern: "payment fraud detection", "AML compliance"

## Analysis Frameworks

**Payment Processor Selection Matrix** (for business)
- **Transaction volume**: Expected monthly transaction count and value
- **Transaction types**: Domestic, international, recurring, variable amount
- **Rate structure**: Fixed %, flat fee, tiered, volume-based discount
- **Settlement**: Daily, weekly, monthly timing
- **Chargeback rate**: Your industry's typical chargeback rate
- **Compliance burden**: Which are included vs additional cost?
- **Integration**: API quality, developer experience, SDKs
- **Support**: Level of support available for issues

**Neobank Viability Assessment**
- **Market differentiation**: What's the unique value proposition?
- **Unit economics**: CAC, retention, revenue per user, path to profitability?
- **Regulatory path**: Can you get charter or do you need banking partner?
- **Core platform**: Which banking system provider?
- **Capital requirements**: How much to launch and reach profitability?
- **Time to market**: How long to build and obtain licenses?
- **Competitive response**: How will incumbent banks react?

**Open Banking Implementation Strategy**
- **Use case**: Account aggregation, payment initiation, or data export?
- **Bank coverage**: Which banks have open APIs in your regions?
- **Standardization**: Are you following PSD2, Open Banking UK, or other?
- **User experience**: Friction of authentication and authorization?
- **Data management**: Storing/caching customer authorization?
- **Scalability**: Can infrastructure handle customer growth?
- **Regulatory**: Handling open banking compliance and audit trails

**Trading System Architecture Decision**
- **Latency SLA**: How fast must order execution be? (ms matters at scale)
- **Order volume**: Peak orders per second at surge traffic?
- **Asset class**: Stocks, options, futures, crypto (regulatory differences)?
- **Market access**: Which exchanges/markets must you connect to?
- **Risk controls**: Position limits, margin calls, circuit breakers
- **Custody model**: Self-custody (crypto) vs custodian (traditional)?
- **Cost**: Infrastructure, market data, licensing vs volume?

**Fraud Detection System Assessment**
- **False positive rate**: How many legitimate transactions incorrectly flagged?
- **False negative rate**: How many fraudulent transactions slip through?
- **Detection latency**: Real-time or batch analysis acceptable?
- **Explainability**: Can system explain why transaction flagged?
- **Tuning burden**: How often require model updates?
- **Scale**: Can system process peak transaction volume?
- **Cost**: Internal team vs vendor solution vs hybrid approach?

**AML/KYC Compliance Framework**
- **KYC requirements**: Verification documents needed by regulation
- **Ongoing monitoring**: Periodic re-verification cadence
- **Transaction monitoring**: Behavioral rules and ML anomaly detection
- **Reporting**: SARs, CTRs, other regulatory reports
- **Audit trail**: Documentation for regulatory examination
- **Sanctions screening**: Which lists (OFAC, UN, EU, etc.)?
- **Geographic risk**: Higher scrutiny for high-risk jurisdictions

## Output Format Templates

### Payment Processor Evaluation
```
Business: [type, monthly volume, transaction types]
Payment Methods: [cards, bank transfers, wallets, etc.]

Processor Candidates: [Stripe, Square, PayPal, etc.]

Stripe: [rates, fees, settlement, compliance included]
Square: [rates, fees, settlement, compliance included]
PayPal: [rates, fees, settlement, compliance included]

Cost Analysis: [expected monthly processing costs]
Compliance: [PCI-DSS requirements and burden]
Integration: [API quality, developer experience]
Support: [availability, quality for issues]

Recommendation: [which processor best fits]
Contract Terms: [setup, transaction minimums, early exit]
```

### Neobank Business Model
```
Value Proposition: [unique differentiation]
Target Market: [customer segment, geography]

Core Services: [payments, savings, lending, wealth, insurance]
Revenue Model: [interchange, spreads, fees, data]
Go-to-Market: [customer acquisition strategy]

Banking Partner: [who holds deposits, if not charter?]
Core System: [technology platform, vendor]
Capital Requirements: [estimated funding to launch and profitability]
Time to Market: [months to beta, months to launch]

Unit Economics: [CAC, monthly retention, LTV]
Path to Profitability: [when break-even expected]
Competitive Response: [how incumbents will react]
```

### Open Banking Integration Strategy
```
Use Case: [account aggregation, payments, data]
Target Banks: [which banks in your market]

API Standard: [PSD2, Open Banking UK, other]
Integration Approach: [which banks first, phased rollout]
Data Requirements: [which account/transaction data needed]

User Experience: [authentication, authorization flow]
Technical Architecture: [token management, data caching]
Data Security: [encryption, access controls]
Compliance: [open banking regulations, privacy]

Timeline: [MVP launch with X banks]
Success Metrics: [connected account count, transaction volume]
Scaling: [adding banks, extending coverage]
```

### Fraud Detection System Design
```
Transaction Volume: [expected monthly, peak TPS]
Transaction Types: [cards, transfers, digital wallets, crypto]

Detection Approach: [rules-based, ML, hybrid]
Data Sources: [transaction, device, behavioral, external]

Rules Engine: [key decision rules for flagging]
ML Model: [algorithms, features, retraining cadence]
Real-time vs Batch: [SLA for fraud decisions]

Acceptable Thresholds: [% false positives, false negatives]
Explainability: [can system explain decisions to users?]
Scaling: [infrastructure to handle volume]
Cost: [build vs buy analysis]

Testing: [fraud simulation, model performance metrics]
Monitoring: [model drift, rule effectiveness]
Updates: [cadence for retraining, rule adjustments]
```

## Key Metrics to Always Collect

For FinTech decisions, track:
1. **Cost**: Per-transaction fees, monthly fixed costs, total cost per unit volume
2. **Speed**: Settlement time, transaction latency, funds availability
3. **Compliance**: KYC/AML rejection rate, suspicious activity detection rate
4. **Security**: Fraud rate, chargebacks, customer complaints
5. **Reliability**: Uptime %, incident frequency, mean time to recovery
6. **Growth**: Customer acquisition rate, retention rate, revenue per user
7. **Risk**: False positives, false negatives, regulatory fines/audits

## Computational Workflows

**Pre-built Analysis Scripts**
- `transaction_cost_analyzer.py` — Model end-to-end payment costs (interchange + fees + spread) across processors with pandas
- `roi_calculator.py` — Compute return on investment for fintech product considering acquisition cost and lifetime value
- `fraud_risk_scorer.py` — Combine false positive/negative rates with business impact to compute fraud system ROI
- `compliance_cost_projector.py` — Estimate KYC/AML implementation cost and regulatory reporting burden by jurisdiction

**Dynamic Computation Examples**
- When selecting payment processor, compute monthly cost across expected transaction distribution (volume, type, geography)
- When evaluating fraud systems, run sensitivity analysis on cost vs false positive rate to optimize threshold
- When modeling neobank unit economics, calculate CAC payback period and lifetime value scenarios

**Output Artifacts**
- Transaction cost breakdown (interchange/fees/spread pie chart, total cost per transaction)
- Unit economics waterfall (revenue - CAC - COGS - operating cost = gross margin)
- Fraud system ROI analysis (cost vs prevented losses across thresholds, break-even point)
- Mermaid flowchart showing payment processing architecture and settlement timeline
- LaTeX formula: Effective_Cost_Per_Transaction = (Interchange + Processor_Fee + Spread) / Transaction_Value * 100 (bps)

## References

Load from `references/` directory:
- `payment-processor-comparison-2024.md` — rates, fees, settlement details
- `neobank-business-model-framework.md` — customer acquisition, unit economics
- `psd2-open-banking-guide.md` — implementation and regulatory requirements
- `trading-system-architecture.md` — latency, risk management, market access
- `fraud-detection-methodology.md` — rules, ML models, testing approaches
- `aml-kyc-compliance.md` — requirements by jurisdiction, customer verification
- `fintech-regulatory-landscape.md` — money transmitter licenses, banking regulations

## Common Pitfalls to Avoid

- **Fee blindness**: Comparing interchange rates without accounting for volume-based discounts
- **Settlement surprise**: Funds availability can be 1-3 days; impacts cash flow
- **Compliance underestimation**: KYC/AML processes more burdensome than expected
- **Charter complexity**: Bank charter takes years and millions; partnership often faster
- **Fraud false confidence**: Rules work until fraudsters adapt; constant tuning needed
- **API fragmentation**: Open Banking APIs differ by country; scaling hard
- **Regulatory surprise**: Rules change (e.g., strong customer authentication); must adapt
- **Customer acquisition shock**: CAC for fintech often 2-3x higher than expected
- **Latency blindness**: Microseconds matter for trading; standard infrastructure insufficient
- **Chargebacks ignored**: High chargeback rate kills processor relationships

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~financial data**: Real-time pricing, regulatory guidance, compliance requirements, market data
- **~~web research**: Payment processor pricing updates, regulatory announcements, market trends
- **~~source control**: Open-source fintech implementations, fraud detection algorithms

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
