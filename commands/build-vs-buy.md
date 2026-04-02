---
description: Build vs buy decision analysis framework
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [capability]
---

# Build vs Buy Command

Execute build vs buy decision analysis for technology capabilities.

## Workflow

1. **Parse Input**
   - Identify capability/system to evaluate (e.g., "observability platform", "search engine")
   - Clarify scope and constraints

2. **Build Path Analysis**
   - Estimate development effort in person-months
   - Identify skill requirements and team capability
   - Research development timeline (optimistic, realistic, pessimistic)
   - Calculate infrastructure and hosting costs
   - Estimate ongoing maintenance burden
   - Consider technical debt and future upgrades
   - Evaluate security and compliance implementation
   - Research learning curve for emerging technologies

3. **Buy Path Analysis**
   - Identify available commercial solutions (SaaS, on-premise, open-source)
   - Research pricing models (per-unit, per-user, tiered, custom)
   - Analyze feature completeness vs requirements
   - Evaluate vendor stability and roadmap
   - Research integration effort and complexity
   - Assess vendor lock-in risks
   - When available: ~~financial-data (vendor financials), ~~ui-components (for web output generation)

4. **TCO Calculation**
   - 1-Year TCO: Build vs Buy comparison
   - 3-Year TCO: Multi-year cost comparison
   - 5-Year TCO: Long-term cost projections
   - Include: Development, licensing, hosting, maintenance, training, support
   - Account for headcount costs (salary + benefits)
   - Factor scaling costs as volume grows

5. **Non-Financial Factors**
   - Time to Market: Build vs Buy readiness
   - Maintenance Burden: Ongoing effort required
   - Vendor Lock-in: Switching costs and risk
   - Feature Control: Ability to customize and extend
   - Team Capability: Do you have skills in-house?
   - Strategic Value: Core differentiator vs commodity function
   - Risk Profile: Execution risk vs vendor risk

6. **Decision Matrix**
   - Build Advantages:
     - Full customization control
     - No vendor lock-in
     - Competitive advantage potential
     - Team skill development
   - Build Disadvantages:
     - Higher upfront cost
     - Longer time to market
     - Ongoing maintenance burden
     - Hiring and retention risk
   - Buy Advantages:
     - Lower upfront cost
     - Faster time to market
     - Vendor handles updates/scaling
     - Proven solution
   - Buy Disadvantages:
     - Limited customization
     - Vendor lock-in
     - Recurring licensing costs
     - Dependency on vendor roadmap

7. **Output: Build vs Buy Analysis**
   - Executive Summary: Recommendation with confidence level
   - Capability Overview: What are we evaluating?
   - TCO Comparison Table:
     - 1-Year, 3-Year, 5-Year costs
     - Build vs Buy side-by-side
     - Breakeven analysis (when does build become cheaper?)
   - Build Path Details:
     - Timeline and milestones
     - Team requirements
     - Key risks and mitigation
   - Buy Path Details:
     - Top 3-5 alternative solutions
     - Pricing and licensing terms
     - Feature comparison matrix
     - Vendor evaluation scores
   - Decision Framework:
     - Weighted scoring of factors
     - Risk assessment: Build vs Buy risk profile
     - Sensitivity analysis: How do assumptions affect decision?
   - Final Recommendation:
     - Best path forward given constraints
     - Alternative paths if primary option infeasible
     - Implementation roadmap

8. **Financial Analysis**
   - Breakeven analysis: When does build cost equal buy cost?
   - Sensitivity: How sensitive is decision to cost assumptions?
   - Scaling costs: How do costs change as usage grows?
   - Hidden costs: What's often overlooked? (integration, training, opportunity costs)

9. **Strategic Considerations**
   - Competitive advantage: Does this differentiate us?
   - Core vs non-core: Is this central to our value proposition?
   - Organizational capability: Do we want to own this?
   - Future flexibility: How might requirements change?

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Challenge assumptions: Be realistic about build timelines
- Include opportunity cost of engineering resources
- Evaluate open-source solutions (often hybrid approach)
- Consider hybrid: Buy with build customization
- Revisit decision annually as costs and capabilities change
