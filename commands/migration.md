---
description: Technology migration planning and execution
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch, Agent
argument-hint: [from] to [to]
---

# Migration Command

Plan technology migrations with phased approach and risk mitigation.

## Workflow

1. **Parse Migration Path**
   - Extract source technology and target technology
   - Examples: "monolith to microservices", "Java to Kotlin", "REST to GraphQL"
   - Clarify scope: full migration vs gradual transition

2. **Migration Landscape Research**
   - Search for case studies and migration guides
   - Identify companies that completed this migration
   - Research common pitfalls and lessons learned
   - Find available tools and frameworks for migration
   - When available: ~~source-control (analyze current codebase structure)

3. **Source State Analysis**
   - Assess current system architecture and constraints
   - Identify dependencies and integration points
   - Research technical debt and modernization opportunities
   - Analyze team skill gaps for target technology
   - Document system metrics: size, complexity, testing coverage
   - When available: ~~source-control (repo analysis), ~~ui-components (for web output generation)

4. **Target State Definition**
   - Define desired end-state architecture
   - Establish success criteria and metrics
   - Identify performance, scalability, and maintainability goals
   - Research target technology maturity and ecosystem
   - Plan for future extensibility in new platform

5. **Risk Assessment**
   - Technical Risks: Complexity, unknown unknowns, tool maturity
   - Timeline Risks: Scope creep, learning curve, unexpected issues
   - Operational Risks: System stability during transition, customer impact
   - Business Risks: Resource allocation, opportunity cost, competitive impact
   - Team Risks: Skill gaps, turnover, morale
   - Mitigation strategies for each risk category

6. **Effort Estimation**
   - Research industry benchmarks for similar migrations
   - Break down by component/subsystem
   - Estimate person-months with contingency (typically +30-50%)
   - Account for parallel running period
   - Include testing and validation overhead

7. **Phased Migration Plan**
   - Phase 1 (Preparation): Tooling, spike, team training
   - Phase 2 (Pilot): Migrate lowest-risk component
   - Phase 3 (Rollout): Migrate remaining components in dependency order
   - Phase 4 (Optimization): Performance tuning, technical debt cleanup
   - Phase 5 (Decommission): Sunset old system
   - Timeline: Realistic duration for each phase

8. **Parallel Running Strategy**
   - Identify dual-write period (both systems active)
   - Plan data sync between old and new systems
   - Establish rollback procedures if new system fails
   - Define cutover strategy (big bang vs gradual)
   - Customer impact assessment and communication plan

9. **Known Pitfalls**
   - Common gotchas and how to avoid them
   - Team communication and alignment breakdowns
   - Underestimating complexity of legacy system
   - Insufficient testing of edge cases
   - Performance regression in new system
   - Data consistency issues during migration

10. **Output: Migration Playbook**
    - Executive Summary: Scope, timeline, key risks
    - Migration Overview: From/To technology summary
    - Risk Assessment Matrix:
      - Risk category
      - Severity and probability
      - Mitigation strategy
    - Detailed Phased Plan:
      - Phase name and duration
      - Objectives and success criteria
      - Teams involved
      - Key milestones
      - Resource requirements
    - Effort Estimation:
      - Person-months by phase
      - Critical path analysis
      - Resource allocation plan
    - Testing Strategy:
      - Unit test coverage requirements
      - Integration testing approach
      - Load and performance testing
      - Customer acceptance testing
    - Rollback Plan:
      - How to detect failure
      - Rollback procedures and decision criteria
      - Time to rollback estimate
    - Known Pitfalls and Mitigations:
      - Common issues in this type of migration
      - Preventive measures
      - Incident response procedures
    - Success Stories:
      - Examples of successful migrations
      - Key success factors
      - Lessons learned

11. **Communication Plan**
    - Stakeholder updates (engineering, product, exec, customers)
    - Change management for teams
    - Customer impact communication
    - Post-migration retrospective

12. **Monitoring and Metrics**
    - Key metrics to track progress
    - Performance regression detection
    - Reliability and stability metrics
    - Team velocity and morale

## Output Format

Ask user for preferred delivery format:
- **Markdown** (default) — Scientific structured document with inline LaTeX math and Mermaid diagrams
- **LaTeX/PDF** — IEEE Academic format with proper bibliography, TikZ diagrams, mathematical notation
- **Interactive Web** — React + shadcn dashboard with interactive charts, sortable tables, and tabbed navigation

Before producing output, read the scientific style guide at skills/output-formats/references/scientific-style-guide.md.
All numeric claims must be computed with Python, not estimated.

## Notes

- Be conservative with timeline estimates (migrations often take longer)
- Maintain parallel systems longer than expected for safety
- Invest in automated testing heavily before and during migration
- Consider hybrid approach: migrate gradually vs big bang
- Document learnings for future migrations
