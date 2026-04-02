---
name: Interactive Brainstorming
description: >
  Structured discovery and brainstorming for technology research. Assess user's
  existing knowledge, then adapt the approach. For complex topics, generate HTML
  intake forms. For simple queries, use targeted questions. Triggered by
  "brainstorm", "explore options", "help me think through", "what should I consider".
---

# Interactive Brainstorming

## Workflow Overview

This skill guides structured discovery for technology research by assessing user context and adapting the approach accordingly. It ensures research is targeted, avoids redundancy, and surfaces the most relevant dimensions for investigation.

### Assessment Phase

Begin with: "How much do you already know about [topic]?" Then adapt based on response:

- **Deep existing context**: Skip introduction. Jump directly to focused clarifying questions, then research. Ask about specific gaps, edge cases, or decisions they're stuck on.
- **Some foundational knowledge**: Guided Q&A to identify gaps and priorities. Map what they know vs. what they need.
- **Exploring new territory**: Open discovery session with broader pattern identification. Start with landscape overview before narrowing.

### Complex Topics: HTML Intake Form

For multi-faceted research (3+ dimensions, cross-cutting concerns), generate an interactive HTML form with these fields:

- Project context and objectives (free text)
- Current technology stack (checklist + free text)
- Constraints: budget range, timeline, team expertise level (dropdowns)
- Priorities and success metrics (ranked list)
- Timeline and milestones (date ranges)
- Team size and roles (numeric + dropdowns)
- Existing vendor relationships or lock-ins (checklist)
- Risk tolerance: conservative, moderate, aggressive (radio buttons)
- Compliance requirements: SOC2, HIPAA, GDPR, FedRAMP, none (checkboxes)

User fills form in browser. Claude processes structured input and generates tailored research plan.

#### HTML Form Template

```html
<form id="research-intake">
  <h2>Technology Research Intake</h2>
  <fieldset>
    <legend>Project Context</legend>
    <label>What problem are you trying to solve?</label>
    <textarea name="problem" rows="3" placeholder="Describe the problem..."></textarea>
    <label>Current technology stack</label>
    <input type="text" name="stack" placeholder="e.g., Python, PostgreSQL, AWS...">
  </fieldset>
  <fieldset>
    <legend>Constraints</legend>
    <label>Budget range</label>
    <select name="budget">
      <option>Under $10K/year</option>
      <option>$10K-$50K/year</option>
      <option>$50K-$200K/year</option>
      <option>$200K+/year</option>
    </select>
    <label>Timeline</label>
    <select name="timeline">
      <option>Under 1 month</option>
      <option>1-3 months</option>
      <option>3-6 months</option>
      <option>6-12 months</option>
      <option>12+ months</option>
    </select>
    <label>Team expertise in target domain</label>
    <select name="expertise">
      <option>No experience</option>
      <option>Some familiarity</option>
      <option>Moderate experience</option>
      <option>Deep expertise</option>
    </select>
  </fieldset>
  <fieldset>
    <legend>Priorities (rank 1-5)</legend>
    <label>Performance</label><input type="number" min="1" max="5" name="p_perf">
    <label>Cost</label><input type="number" min="1" max="5" name="p_cost">
    <label>Developer Experience</label><input type="number" min="1" max="5" name="p_dx">
    <label>Scalability</label><input type="number" min="1" max="5" name="p_scale">
    <label>Security/Compliance</label><input type="number" min="1" max="5" name="p_sec">
  </fieldset>
</form>
```

### Simple Queries: Targeted Questions

For straightforward inquiries (single-dimension, clear scope):

1. Ask 1-2 clarifying questions in chat
2. Use multiple choice where possible
3. Proceed directly to focused research

Example patterns:
- "Are you comparing options or exploring a new space?" (Comparison vs Discovery)
- "What's your primary concern: performance, cost, or team productivity?" (Priority filter)
- "Is this for a new project or migrating an existing system?" (Context filter)

### Socratic Questioning Patterns

- Ask one question at a time
- Build on prior responses
- Offer 2-3 multiple choice options when applicable
- Guide toward discovery rather than prescribing answers
- Use "What if..." to explore edge cases
- Use "How would you handle..." to test assumptions

### Alternative Approaches

Before committing to a research direction:

1. Identify 2-3 alternative approaches to the problem
2. Outline trade-offs for each in a quick comparison table
3. Recommend based on user priorities
4. Remain flexible if user preferences change mid-research

### Priority Scoring Framework

When brainstorming surfaces multiple options or directions, use a lightweight scoring framework to help the user prioritize:

| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| Alignment with goals | 30% | ? | ? | ? |
| Feasibility (time/budget) | 25% | ? | ? | ? |
| Risk level | 20% | ? | ? | ? |
| Team readiness | 15% | ? | ? | ? |
| Innovation potential | 10% | ? | ? | ? |

Score each option 1-5 per criterion. Compute weighted scores to provide a data-driven starting point for discussion.

### Brainstorming Session Templates

#### Technology Selection Brainstorm
1. Define requirements (functional + non-functional)
2. Generate candidate list (aim for 5-10 options)
3. Quick-filter against hard constraints (eliminates 50%+)
4. Deep-evaluate remaining candidates
5. Score and rank
6. Present recommendation with rationale

#### Architecture Brainstorm
1. Identify system requirements and quality attributes
2. Generate 2-3 candidate architectures
3. Map trade-offs (consistency vs availability, simplicity vs flexibility)
4. Evaluate against operational constraints
5. Recommend with migration path

#### Problem Decomposition Brainstorm
1. State the problem clearly
2. Break into sub-problems (aim for 3-5 components)
3. Identify dependencies between sub-problems
4. Prioritize by impact and feasibility
5. Assign research depth per sub-problem

## Computational Workflows

### Pre-built Analysis Scripts

**priority_scorer.py**: Weighted scoring model for brainstormed options. Inputs: options list, criteria with weights, scores per option. Outputs: ranked options with weighted scores, sensitivity analysis showing how rank changes with weight adjustments.

**decision_tree_builder.py**: Generates a decision tree from brainstorming outcomes. Inputs: decision points, criteria, options at each node. Outputs: Mermaid flowchart of the decision path, with annotations for confidence level at each branch.

### Dynamic Computation Examples

1. **Option Scoring**: Input: 3-5 technology options, 4-6 weighted criteria, scores 1-5. Compute: weighted scores, rank, sensitivity analysis. Output: Ranked table with confidence.

2. **Feasibility Estimator**: Input: team size, timeline, complexity estimate. Compute: rough effort estimate using COCOMO-style model. Output: feasibility assessment (green/yellow/red).

## Output Examples

- Research intake form (HTML) tailored to the topic
- Priority-scored option comparison table
- Decision tree (Mermaid) showing evaluation path
- Research plan with scope, agents, and expected outputs

## Implementation Notes

- Assess knowledge level upfront to avoid repeating basics
- Generate forms only when justified by topic complexity (3+ dimensions)
- Use conversational tone while maintaining structured logic
- Document assumptions about user's research goals
- Provide clear next steps after each phase
- If the user changes direction mid-session, acknowledge and pivot gracefully
- Use ~~web research for real-time context during brainstorming sessions
