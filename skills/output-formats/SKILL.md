---
name: output-formats
description: >
  Standardized output format templates for technology research deliverables.
  This skill should be used whenever generating a research report, tech radar,
  comparison matrix, SWOT analysis, decision matrix, scorecard, or any structured
  tech intelligence output. Use when the user asks for "a report on", "analysis of",
  "comparison between", "SWOT for", "decision matrix for", or any deliverable format.
---

# Output Format Templates

This skill provides standardized templates for technology research deliverables. Use these formats to structure your research findings consistently and professionally.

## Available Formats

### 1. Tech Radar (ThoughtWorks-style)
**When to use:** Assessing the current state and trajectory of technologies across your organization. Best for teams deciding what to adopt, evaluate, or retire.

- Four quadrants: Languages & Frameworks, Tools, Platforms, Techniques
- Four rings: Adopt, Trial, Assess, Hold
- Tracks movement (new, unchanged, moved-in, moved-out)
- Includes rationale for placement

Reference: `/skills/output-formats/references/tech-radar-template.md`

### 2. Comparison Matrix
**When to use:** Choosing between multiple technology options. Includes performance, maturity, cost, and other dimensions with weighted scoring.

- 8 standard dimensions: Performance, Maturity, Community, Security, Cost, Developer Experience, Ecosystem, Scalability
- 1-5 scoring scale with defined criteria
- Weighted scoring methodology
- Color-coded results
- Clear verdict and confidence level

Reference: `/skills/output-formats/references/comparison-matrix-template.md`

### 3. SWOT Analysis
**When to use:** Understanding the strategic position of a technology or technology choice. Identifies internal strengths/weaknesses and external opportunities/threats.

- Four sections: Strengths, Weaknesses, Opportunities, Threats
- Strategic implications
- Priority matrix (high impact + high probability)

Reference: `/skills/output-formats/references/swot-template.md`

### 4. Decision Matrix
**When to use:** Making a final decision between options when multiple criteria matter. Provides mathematical rigor to qualitative assessment.

- Weighted criteria (weights sum to 100%)
- 1-5 scoring rubric per criterion
- Normalized weighted score calculation
- Sensitivity analysis (weight variation scenarios)
- Confidence level and recommendation

Reference: `/skills/output-formats/references/decision-matrix-template.md`

### 5. Deep Research Report
**When to use:** Comprehensive analysis requiring substantial depth (3000+ words). Includes methodology, evidence, recommendations, and risk analysis.

- Executive summary (standalone readable)
- Background and context
- Methodology section (sources, date range, search terms)
- Key findings organized by theme with confidence levels
- Analysis and discussion
- Actionable recommendations with effort estimates
- Risk factors
- Numbered sources with credibility tiers
- Appendices

Reference: `/skills/output-formats/references/deep-report-template.md`

### 6. Scorecard (Health Assessment)
**When to use:** Auditing the health of a technology, open-source project, or platform. Uses traffic light system for quick visual assessment.

- Traffic light system: GREEN, YELLOW, RED
- Six categories: Security, Maintenance, Community, Documentation, Performance, Compliance
- Scoring 1-10 per category
- Overall weighted score
- Actionable verdict

Reference: `/skills/output-formats/references/scorecard-template.md`

### 7. Executive Brief
**When to use:** One-page summary for decision-makers. Quick reference with key findings and clear recommendation.

- TL;DR (2-3 sentences)
- Key findings (3-5 bullets)
- Clear recommendation
- Risk summary (high/medium/low)
- Next steps (2-3 actions)
- Strict one-page format

Reference: `/skills/output-formats/references/executive-brief-template.md`

### 8. Risk Heat Map
**When to use:** Identifying and prioritizing risks across likelihood and impact dimensions. Useful for technology adoption, vendor selection, compliance.

- Likelihood (1-5) vs Impact (1-5) grid
- Color coding: Red (score >15), Orange (10-15), Yellow (5-9), Green (<5)
- Risk categories: Technical, Security, Vendor, Compliance, Operational
- Mitigation strategies for each risk
- ASCII visualization included

Reference: `/skills/output-formats/references/risk-heatmap-template.md`

### 9. Adoption Curve
**When to use:** Understanding where a technology sits in its adoption lifecycle. Helps predict evolution and community support.

- Five phases with percentages: Innovators (2.5%), Early Adopters (13.5%), Early Majority (34%), Late Majority (34%), Laggards (16%)
- Assessment criteria for each phase
- Chasm indicators
- Current position methodology
- Bell curve visualization

Reference: `/skills/output-formats/references/adoption-curve-template.md`

## Selecting the Right Format

**By Research Question:**

| Question Type | Best Format |
|---------------|------------|
| "Should we adopt X?" | Decision Matrix + Scorecard |
| "How does X compare to Y and Z?" | Comparison Matrix |
| "What's the strategic position of X?" | SWOT Analysis |
| "Is X healthy/viable?" | Scorecard |
| "Where does X sit in the market?" | Adoption Curve + Tech Radar |
| "What are the risks of X?" | Risk Heat Map |
| "I need a comprehensive analysis of X" | Deep Research Report |
| "I need to brief the executive team on X" | Executive Brief |
| "How should we think about X long-term?" | Tech Radar (organizational view) |

**By Audience:**

| Audience | Best Format |
|----------|------------|
| Technical team | Tech Radar, Comparison Matrix, Deep Report |
| Engineering leadership | Decision Matrix, Scorecard, Risk Heat Map |
| Executive team | Executive Brief, Tech Radar (summary), SWOT (strategic) |
| Board/external | Executive Brief, Risk Heat Map, Deep Report (if requested) |

**By Time Available:**

| Time Available | Best Format |
|----------------|------------|
| <30 minutes | Executive Brief |
| 30-60 minutes | Scorecard, Adoption Curve, Risk Heat Map |
| 1-2 hours | Comparison Matrix, SWOT Analysis, Decision Matrix |
| 4+ hours | Deep Research Report, Tech Radar (org-wide) |

## Format Selection Workflow

1. **Clarify the purpose:** Decision, assessment, strategy, or briefing?
2. **Identify the audience:** Technical, leadership, executive, or external?
3. **Define the scope:** Single technology, comparison, or portfolio view?
4. **Check time constraints:** How much analysis time is available?
5. **Choose format:** Select from the table above
6. **Add supporting materials:** Use multiple formats if needed (e.g., Executive Brief + Deep Report, or Decision Matrix + Risk Heat Map)

## Tips for Effective Use

- **Consistency:** Use these templates across all research to build organizational muscle
- **Customization:** Adapt dimensions, criteria, and categories to your context
- **Evidence:** Always include sources and rationale, not just scores
- **Confidence:** Be explicit about confidence levels and data quality
- **Action:** End every output with clear next steps or recommendations
- **Audience:** Tailor terminology and detail level to your audience
- **Regular review:** Revisit assessments periodically; technologies change

## Three Delivery Tiers

The same research can be delivered in three formats depending on audience needs and deliverable requirements. All three tiers contain identical findings but are styled for their specific context.

### Tier 1: Markdown (Default)

Use markdown as the default output format for all research deliverables. This is the most flexible and fastest to produce.

**Structure:**
- Scientific numbered sections (1, 1.1, 1.2, etc.)
- Inline citations using [1], [2] format corresponding to numbered reference list
- LaTeX math blocks for all formulas, using proper $$ display notation
- Mermaid diagrams embedded directly (flowchart, sequence, architecture)
- Computed tables with real Python data (show the formula and code)
- Confidence ratings per major claim [Confidence: High/Medium/Low, justification]

**Key requirements:**
- Executive summary (2-3 sentences) before TOC for long documents
- Methodology section describing data sources, search strategy, date range, and limitations
- All numeric claims must show: formula, Python code, input parameters, results with confidence intervals
- Evidence tier labeling for all sources [Tier 1: Official], [Tier 2: Case Study], [Tier 3: Blog], [Tier 4: Social]
- Tables instead of bullet points for comparisons
- No emojis, no contractions, third-person perspective
- Mermaid diagrams use default colors only

**Example structure:**

```markdown
# Title

## 1. Introduction
Research question and context.

## 2. Methodology
Searched: PubMed, IEEE Xplore, vendor documentation.
Date range: 2023-2026.
Inclusion criteria: peer-reviewed studies, official specs, case studies from Tier 1-2 sources.
Limitations: excluded proprietary vendor claims without third-party validation.

## 3. Key Findings

**Finding 3.1: System throughput at scale**

The system processes an average of 50M records daily [1] [Tier 1: Official].

$$\text{Throughput} = \frac{\text{Total Records}}{\text{Time in Hours}} = \frac{50,000,000}{24} = 2,083,333 \text{ records/hour}$$

Python verification:
```python
total_records = 50_000_000
hours = 24
throughput = total_records / hours
print(f"Throughput: {throughput:,.0f} records/hour")
# Output: Throughput: 2,083,333 records/hour
```

[Confidence: High, from official vendor specification published 2025 with production deployment validation].

## References
[1] Acme Corp. "System Performance White Paper." https://example.com/perf, 2025.
```

---

### Tier 2: LaTeX/PDF (IEEE Academic)

Use LaTeX for formal academic publication, peer-reviewed submissions, or comprehensive technical reports (8+ pages for deep research, 4+ pages for comparisons).

**Document class:**
```latex
\documentclass[conference]{IEEEtran}
```

**Key requirements:**

**Tables:**
- ALWAYS use `tabularx` with `\columnwidth` for standard tables, or `table*` with `\textwidth` for full-width tables
- Use `booktabs` for professional spacing and line quality (\toprule, \midrule, \bottomrule)
- NEVER use `p{}` widths that exceed column width — use relative sizing with X columns
- Right-align numbers, left-align text
- Include units in headers

Example:
```latex
\begin{table*}[!t]
\renewcommand{\arraystretch}{1.3}
\caption{Comparison of Framework Performance Metrics}
\label{tab:performance}
\centering
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Metric} & \textbf{Framework A} & \textbf{Framework B} & \textbf{Framework C} \\
\midrule
Throughput (req/s) & 10,500 & 8,200 & 12,100 \\
Latency (ms) & 45 & 62 & 38 \\
Memory (GB) & 2.3 & 1.8 & 3.1 \\
\bottomrule
\end{tabularx}
\end{table*}
```

**TikZ diagrams:**
- Use `figure*` for full-width diagrams
- Include libraries: shapes, arrows, positioning, fit
- Professional styling, consistent with IEEE standards
- ALWAYS wrap in `\resizebox{\textwidth}{!}{...}` to prevent overflow
- ANTI-OVERLAP: When 3+ nodes sit in a horizontal row, use `minimum width=0.85cm`, `\tiny` font, and 2cm+ center-to-center spacing. Horizontal spacing MUST be >= 2x node rendered width.
- Define reusable styles: `box/.style={draw,rectangle,minimum width=0.85cm,minimum height=0.5cm,inner sep=1pt}`
- For side-by-side sub-diagrams, use 6+ units gap between sub-diagram centers

Example (anti-overlap pattern for 3-column comparison):
```latex
\begin{figure*}[htb]
\centering
\resizebox{\textwidth}{!}{
\begin{tikzpicture}[
  every node/.style={font=\tiny},
  box/.style={draw,rectangle,minimum width=0.85cm,minimum height=0.5cm,inner sep=1pt},
  widebox/.style={draw,rectangle,minimum width=2.5cm,minimum height=0.5cm,inner sep=1pt},
]
% Sub-diagram A (center x=2)
\node[box] (a1) at (2,0) {Node A};
\node[box] (a2) at (0,-1.3) {Left};
\node[box] (a3) at (2,-1.3) {Center};
\node[box] (a4) at (4,-1.3) {Right};
% 2cm spacing, 0.85cm nodes = no overlap

% Sub-diagram B (center x=10, gap=8 from A)
\node[box] (b1) at (10,0) {Node B};
% ...
\end{tikzpicture}
}
\caption{Comparison diagram with zero overlaps.}
\end{figure*}
```

**Mathematics:**
- Minimum 5 numbered equations using `equation` environment
- Proper LaTeX notation with \text{} for words in formulas
- Reference equations with \eqref{eq:label}

**Document structure:**
- Abstract (150-250 words)
- Introduction with research question
- Literature review
- Methodology section describing approach and limitations
- Results with computed data and validation
- Discussion and analysis
- Conclusion
- References (minimum 15, IEEE format)
- Appendices as needed

**Writing style:**
- Third person, formal academic register
- No contractions ("cannot", not "can't")
- No marketing language or hedging
- Explicit confidence levels and uncertainty quantification

**Full preamble example that works:**
```latex
\documentclass[conference]{IEEEtran}
\usepackage[utf-8]{inputenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,fit}
\usepackage{hyperref}
\usepackage{cite}

\begin{document}

\title{Research Title Here}
\author{Author Name}
\date{2026}

\maketitle

\begin{abstract}
Abstract text here (150-250 words).
\end{abstract}

% Document content follows

\end{document}
```

---

### Tier 3: Interactive Web (React + shadcn)

Use a full Vite + React + Tailwind + shadcn project for interactive research deliverables. This is NOT a single JSX file — it requires a proper project structure with CSS variables, shadcn components, and Recharts.

#### Decoding a shadcn Preset

shadcn presets (e.g., `--preset b50cupeFP`) encode base62-compressed design tokens. To decode what a preset contains, run:

```bash
npx shadcn@latest init --preset b50cupeFP --yes --defaults 2>&1
```

Even if the command fails (e.g., egress blocked), the error message reveals the decoded URL with all parameters:

```
style=lyra&baseColor=neutral&theme=neutral&iconLibrary=phosphor
&font=playfair-display&menuColor=inverted-translucent&radius=default&chartColor=rose
```

This tells you exactly which CSS variables, fonts, icon library, and radius to use.

#### Cross-Platform Compatibility: Use Vite 5 + Tailwind v3

CRITICAL: Vite 8 uses `rolldown` which has native bindings (`@rolldown/binding-darwin-arm64`, `@rollup/rollup-linux-arm64-gnu`). If node_modules are installed on one platform (e.g., macOS ARM), the build will crash on another platform (e.g., Linux x86/ARM). **Always use Vite 5.4 + Tailwind v3 for maximum compatibility.**

**Project structure:**

```
showcase-web-output/
  src/
    index.css          # @import font, @tailwind directives, @layer base CSS variables
    main.tsx           # Entry point, imports index.css
    App.tsx            # Main dashboard component (500+ lines for deep research)
    lib/
      utils.ts         # cn() utility from clsx + tailwind-merge
    components/
      ui/
        card.tsx       # shadcn Card (border bg-card text-card-foreground shadow-sm)
        badge.tsx      # shadcn Badge with variant support (default/secondary/destructive/outline)
        tabs.tsx       # shadcn Tabs with TabsList/TabsTrigger/TabsContent
  components.json      # shadcn CLI config (style, baseColor, chartColor, iconLibrary)
  tailwind.config.js   # Maps CSS vars to Tailwind utilities (Tailwind v3)
  postcss.config.js    # tailwindcss + autoprefixer (Tailwind v3)
  vite.config.ts       # Vite 5 + react plugin + path alias @/ -> ./src
  index.html           # Google Fonts link for custom font
  tsconfig.app.json    # paths: { "@/*": ["./src/*"] }
  package.json         # vite ^5.4.0, tailwindcss ^3.4.0
```

**package.json dependencies (Vite 5 + Tailwind v3):**
```json
{
  "devDependencies": {
    "vite": "^5.4.0",
    "@vitejs/plugin-react": "^4.2.1",
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.35",
    "autoprefixer": "^10.4.17",
    "typescript": "~5.6.2"
  },
  "dependencies": {
    "react": "^18.3.1",
    "recharts": "^2.12.7",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.0",
    "class-variance-authority": "^0.7.0"
  }
}
```

**postcss.config.js (required for Tailwind v3):**
```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

**vite.config.ts (Vite 5 — NO @tailwindcss/vite):**
```ts
import path from "path"
import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
export default defineConfig({
  plugins: [react()],
  resolve: { alias: { "@": path.resolve(__dirname, "./src") } },
})
```

#### CSS Variables by Base Color

shadcn offers multiple base colors. Each changes the hue family used for all neutral surfaces.

**How to identify:** The base color determines the hue value:
- **Neutral** (hue 0, saturation 0%) — pure grays, no color cast
- **Zinc** (hue 240, saturation ~4-10%) — slight blue/indigo tint
- **Slate** (hue 215-222, saturation ~16-47%) — blue-gray tint
- **Stone** (hue 20-25, saturation ~5-14%) — warm gray tint
- **Gray** (hue 220, saturation ~9-14%) — cool gray

#### Tailwind v3 Setup (`tailwind.config.js`):

In Tailwind v3, CSS variables map to utilities via the config file (NOT `@theme` block):

```js
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["'Playfair Display'", "Georgia", "serif"],   // from preset font
        heading: ["'Playfair Display'", "Georgia", "serif"],
      },
      colors: {
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        card: "hsl(var(--card))",
        "card-foreground": "hsl(var(--card-foreground))",
        popover: "hsl(var(--popover))",
        "popover-foreground": "hsl(var(--popover-foreground))",
        primary: "hsl(var(--primary))",
        "primary-foreground": "hsl(var(--primary-foreground))",
        secondary: "hsl(var(--secondary))",
        "secondary-foreground": "hsl(var(--secondary-foreground))",
        muted: "hsl(var(--muted))",
        "muted-foreground": "hsl(var(--muted-foreground))",
        accent: "hsl(var(--accent))",
        "accent-foreground": "hsl(var(--accent-foreground))",
        destructive: "hsl(var(--destructive))",
        "destructive-foreground": "hsl(var(--destructive-foreground))",
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        "chart-1": "hsl(var(--chart-1))",
        "chart-2": "hsl(var(--chart-2))",
        "chart-3": "hsl(var(--chart-3))",
        "chart-4": "hsl(var(--chart-4))",
        "chart-5": "hsl(var(--chart-5))",
        sidebar: {
          DEFAULT: "hsl(var(--sidebar-background))",
          foreground: "hsl(var(--sidebar-foreground))",
          primary: "hsl(var(--sidebar-primary))",
          "primary-foreground": "hsl(var(--sidebar-primary-foreground))",
          accent: "hsl(var(--sidebar-accent))",
          "accent-foreground": "hsl(var(--sidebar-accent-foreground))",
          border: "hsl(var(--sidebar-border))",
          ring: "hsl(var(--sidebar-ring))",
        },
      },
      borderRadius: {
        sm: "calc(var(--radius) - 4px)",
        md: "calc(var(--radius) - 2px)",
        lg: "var(--radius)",
        xl: "calc(var(--radius) + 4px)",
      },
    },
  },
  plugins: [],
}
```

#### CSS Variables: Neutral Base + Rose Charts (Reference Implementation)

The example below shows the EXACT CSS for `--preset b50cupeFP` (Lyra + Neutral + Rose):

**`src/index.css`:**

```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {

:root {
  /* Neutral base (hue 0, saturation 0%) — pure grays */
  --background: 0 0% 100%;
  --foreground: 0 0% 3.9%;
  --card: 0 0% 100%;
  --card-foreground: 0 0% 3.9%;
  --popover: 0 0% 100%;
  --popover-foreground: 0 0% 3.9%;
  --primary: 0 0% 9%;
  --primary-foreground: 0 0% 98%;
  --secondary: 0 0% 96.1%;
  --secondary-foreground: 0 0% 9%;
  --muted: 0 0% 96.1%;
  --muted-foreground: 0 0% 45.1%;
  --accent: 0 0% 96.1%;
  --accent-foreground: 0 0% 9%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 0 0% 98%;
  --border: 0 0% 89.8%;
  --input: 0 0% 89.8%;
  --ring: 0 0% 3.9%;

  /* Lyra style: radius None = 0 */
  --radius: 0rem;

  /* Rose chart colors (Tailwind rose scale) */
  --chart-1: 347 77% 50%;
  --chart-2: 349 89% 60%;
  --chart-3: 351 95% 72%;
  --chart-4: 353 96% 82%;
  --chart-5: 355 100% 91%;

  /* Sidebar (inverted-translucent menu) */
  --sidebar-background: 0 0% 98%;
  --sidebar-foreground: 0 0% 3.9%;
  --sidebar-primary: 0 0% 9%;
  --sidebar-primary-foreground: 0 0% 98%;
  --sidebar-accent: 0 0% 96.1%;
  --sidebar-accent-foreground: 0 0% 9%;
  --sidebar-border: 0 0% 89.8%;
  --sidebar-ring: 0 0% 3.9%;
}

.dark {
  --background: 0 0% 3.9%;
  --foreground: 0 0% 98%;
  --card: 0 0% 3.9%;
  --card-foreground: 0 0% 98%;
  --popover: 0 0% 3.9%;
  --popover-foreground: 0 0% 98%;
  --primary: 0 0% 98%;
  --primary-foreground: 0 0% 9%;
  --secondary: 0 0% 14.9%;
  --secondary-foreground: 0 0% 98%;
  --muted: 0 0% 14.9%;
  --muted-foreground: 0 0% 63.9%;
  --accent: 0 0% 14.9%;
  --accent-foreground: 0 0% 98%;
  --destructive: 0 62.8% 30.6%;
  --destructive-foreground: 0 0% 98%;
  --border: 0 0% 14.9%;
  --input: 0 0% 14.9%;
  --ring: 0 0% 83.1%;

  --chart-1: 347 77% 50%;
  --chart-2: 349 89% 60%;
  --chart-3: 351 95% 72%;
  --chart-4: 353 96% 82%;
  --chart-5: 355 100% 91%;

  --sidebar-background: 0 0% 3.9%;
  --sidebar-foreground: 0 0% 98%;
  --sidebar-primary: 0 0% 98%;
  --sidebar-primary-foreground: 0 0% 9%;
  --sidebar-accent: 0 0% 14.9%;
  --sidebar-accent-foreground: 0 0% 98%;
  --sidebar-border: 0 0% 14.9%;
  --sidebar-ring: 0 0% 83.1%;
}

  * { border-color: hsl(var(--border)); }

  body {
    background-color: hsl(var(--background));
    color: hsl(var(--foreground));
    font-family: 'Playfair Display', Georgia, 'Times New Roman', serif;
    margin: 0;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', Georgia, 'Times New Roman', serif;
    font-weight: 700;
  }
}
```

IMPORTANT NOTES:
- `@import url(...)` MUST come BEFORE `@tailwind` directives, or Vite will emit a warning
- Color variable format: bare HSL values (no `hsl()` wrapper): `0 0% 9%` — enables Tailwind opacity modifiers like `bg-primary/50`
- Neutral base uses hue 0 with 0% saturation (NOT Zinc hue 240)
- Rose chart colors use the Tailwind rose scale (hue 347-355)
- Lyra "Radius: None" = `--radius: 0rem` (all rounded-* classes resolve to 0)

#### Chart Color Reference by Palette

| Palette | chart-1 | chart-2 | chart-3 | chart-4 | chart-5 |
|---------|---------|---------|---------|---------|---------|
| Rose    | 347 77% 50% | 349 89% 60% | 351 95% 72% | 353 96% 82% | 355 100% 91% |
| Orange  | 12 76% 61%  | 16 85% 68%  | 20 90% 76%  | 24 94% 83%  | 28 100% 90% |
| Blue    | 221 83% 53% | 217 91% 60% | 213 93% 68% | 210 98% 78% | 206 100% 88% |
| Green   | 142 76% 36% | 142 69% 45% | 142 58% 55% | 141 50% 65% | 140 45% 78% |
| Default | 12 76% 61%  | 173 58% 39% | 197 37% 24% | 43 74% 66%  | 27 87% 67% |

#### Font Setup

When the preset specifies a custom font (e.g., Playfair Display):

1. Add `<link>` in `index.html` for faster loading:
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet" />
```

2. Also add `@import` in `index.css` (before @tailwind) as fallback
3. Map in `tailwind.config.js` via `fontFamily.sans` and `fontFamily.heading`
4. Set in `body` CSS: `font-family: 'Playfair Display', Georgia, serif;`

#### components.json (shadcn CLI config)

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "lyra",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/index.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  },
  "iconLibrary": "phosphor",
  "chartColor": "rose"
}
```

#### Strict UI rules:
- ONLY semantic CSS variable classes: `bg-background`, `text-foreground`, `bg-card`, `text-card-foreground`, `bg-primary`, `text-primary-foreground`, `bg-secondary`, `bg-muted`, `text-muted-foreground`, `bg-accent`, `bg-destructive`, `border-border`, `ring-ring`
- NO hardcoded colors (no `bg-blue-500`, no `text-slate-700`, no hex codes, no `rgb()`)
- ALWAYS pair background + foreground: `bg-primary text-primary-foreground`
- Border radius via `rounded-md` / `rounded-lg` (maps to --radius from preset)

#### Charts (Recharts with CSS variables):

```tsx
const chartColors = {
  c1: "hsl(var(--chart-1))",
  c2: "hsl(var(--chart-2))",
  c3: "hsl(var(--chart-3))",
  c4: "hsl(var(--chart-4))",
  c5: "hsl(var(--chart-5))",
}

<BarChart data={data}>
  <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
  <Bar dataKey="valueA" fill={chartColors.c1} />
  <Bar dataKey="valueB" fill={chartColors.c2} />
</BarChart>
```

NOTE: Recharts Tooltip `formatter` prop expects `(value: unknown)` not `(value: number)`. Cast inside: `(v: unknown) => Number(v).toLocaleString()`.

#### Content requirements for research dashboards:

The web output must be COMPREHENSIVE, not a small summary. Minimum requirements:
- Header with Badge components (report type, domain, confidence score)
- 4+ metric cards (CardHeader + CardContent with computed values)
- 5+ tabs minimum, each containing a different analysis dimension
- Each tab: chart (BarChart/LineChart/RadarChart/AreaChart) + analysis sidebar card
- Weighted decision matrix as interactive table with sortable columns
- Methodology section (4-column grid: literature review, environment, statistics, limitations)
- References section with formatted citations
- Dark mode toggle (shadcn approach: `document.documentElement.classList.toggle("dark")`)
- Footer with generation metadata

**Example working project:** See `examples/showcase-web-output/` for a complete buildable Vite 5 project.

#### cn() utility (`src/lib/utils.ts`):
```ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

#### Tailwind v4 Alternative (if Vite 8 + platform-specific native bindings are available)

If you can guarantee a single platform (e.g., only deploying on Linux x86), Tailwind v4 is an option. Key differences:
- Uses `@import "tailwindcss"` instead of `@tailwind base/components/utilities`
- Uses `@theme { ... }` block to register CSS vars as utilities (REPLACES tailwind.config.js)
- Uses `@tailwindcss/vite` plugin instead of PostCSS
- No `tailwind.config.js` or `postcss.config.js` needed

However, Tailwind v3 + Vite 5 is RECOMMENDED for maximum cross-platform compatibility.

---

## File Structure

All templates are in `/references/`:
- tech-radar-template.md
- comparison-matrix-template.md
- swot-template.md
- decision-matrix-template.md
- deep-report-template.md
- scorecard-template.md
- executive-brief-template.md
- risk-heatmap-template.md
- adoption-curve-template.md
