/*
 * WEB OUTPUT TEMPLATE - Reference Implementation
 *
 * This file is a REFERENCE for the App.tsx pattern used in web output projects.
 * For a complete working example, see: examples/showcase-web-output/
 *
 * Web outputs are full Vite 5 + React + Tailwind v3 + shadcn projects, NOT single JSX files.
 * Use Vite 5 (not 8) for cross-platform compatibility (no native rolldown bindings).
 * Use Tailwind v3 with PostCSS (not v4 with @tailwindcss/vite).
 *
 * Required project structure:
 *   src/index.css          - @import font FIRST, then @tailwind directives, then @layer base CSS vars
 *   src/main.tsx           - Entry point importing index.css
 *   src/App.tsx            - Main dashboard component (this template)
 *   src/lib/utils.ts       - cn() utility from clsx + tailwind-merge
 *   src/components/ui/     - shadcn components (card.tsx, badge.tsx, tabs.tsx)
 *   components.json        - shadcn CLI config (style, baseColor, chartColor, iconLibrary)
 *   tailwind.config.js     - Maps CSS vars to Tailwind utilities (Tailwind v3)
 *   postcss.config.js      - tailwindcss + autoprefixer (Tailwind v3)
 *   vite.config.ts         - Vite 5 + react plugin + @ path alias (NO @tailwindcss/vite)
 *   index.html             - Google Fonts <link> for custom font (e.g., Playfair Display)
 *   tsconfig.app.json      - With paths: { "@/*": ["./src/*"] }
 *
 * PRESET DECODING: Run `npx shadcn@latest init --preset <code> --yes --defaults` and read
 * the decoded URL in the output to get style, baseColor, chartColor, font, radius, etc.
 *
 * BASE COLOR determines the hue family:
 *   Neutral = hue 0, saturation 0% (pure grays)
 *   Zinc    = hue 240, saturation ~4-10% (blue tint)
 *   Slate   = hue 215-222, saturation ~16-47% (blue-gray)
 *   Stone   = hue 20-25, saturation ~5-14% (warm gray)
 *
 * CRITICAL: All colors MUST use shadcn semantic CSS variable classes:
 *   bg-background, text-foreground, bg-card, text-card-foreground,
 *   bg-primary, text-primary-foreground, bg-secondary, text-secondary-foreground,
 *   bg-muted, text-muted-foreground, bg-accent, bg-destructive,
 *   border-border, ring-ring
 *
 * Charts use: hsl(var(--chart-1)) through hsl(var(--chart-5))
 * Grid strokes use: hsl(var(--border))
 *
 * Recharts Tooltip formatter: use (v: unknown) => Number(v).toLocaleString()
 *   NOT (v: number) — TypeScript will reject the wrong type.
 *
 * NO hardcoded colors. NO bg-blue-500, NO text-slate-700, NO hex codes.
 */

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import {
  BarChart, Bar, LineChart, Line, RadarChart, Radar, AreaChart, Area,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  ResponsiveContainer, PolarAngleAxis, PolarGrid, PolarRadiusAxis,
} from "recharts"

// Chart colors from CSS variables — resolve at runtime via shadcn preset
const chartColors = {
  c1: "hsl(var(--chart-1))",
  c2: "hsl(var(--chart-2))",
  c3: "hsl(var(--chart-3))",
  c4: "hsl(var(--chart-4))",
  c5: "hsl(var(--chart-5))",
}

// ─── DATA (replace with actual research data) ────────────────────────────────

const performanceData = [
  { metric: "Throughput", optionA: 95, optionB: 78, optionC: 85 },
  { metric: "Latency", optionA: 72, optionB: 92, optionC: 68 },
  // ... add all comparison metrics
]

// ─── MAIN APP ────────────────────────────────────────────────────────────────

export default function ResearchDashboard() {
  const [darkMode, setDarkMode] = useState(false)

  const toggleDark = () => {
    setDarkMode(!darkMode)
    document.documentElement.classList.toggle("dark")
  }

  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Header with badges */}
      <header className="border-b bg-card">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-start justify-between">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <Badge>R&D Report</Badge>
                <Badge variant="secondary">Domain</Badge>
                <Badge variant="outline">Confidence: 0.XX</Badge>
              </div>
              <h1 className="text-3xl font-bold tracking-tight text-foreground">
                Research Title
              </h1>
              <p className="text-lg text-muted-foreground mt-1">Subtitle</p>
              <div className="flex items-center gap-4 mt-3 text-sm text-muted-foreground">
                <span>Generated: YYYY-MM-DD</span>
                <span>Sources: N papers, M benchmarks</span>
              </div>
            </div>
            <button
              onClick={toggleDark}
              className="px-3 py-1.5 rounded-md border bg-secondary text-secondary-foreground text-sm"
            >
              {darkMode ? "Light" : "Dark"}
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 py-8 space-y-10">
        {/* Key metrics cards */}
        <section>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <Card>
              <CardHeader className="pb-2">
                <CardDescription>Metric Name</CardDescription>
                <CardTitle className="text-3xl tabular-nums">Value</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-xs text-muted-foreground">Context</p>
              </CardContent>
            </Card>
            {/* ... more metric cards */}
          </div>
        </section>

        {/* Tabbed analysis — minimum 5 tabs */}
        <Tabs defaultValue="overview">
          <TabsList className="flex flex-wrap gap-1">
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="performance">Performance</TabsTrigger>
            <TabsTrigger value="cost">Cost Analysis</TabsTrigger>
            <TabsTrigger value="radar">Capability Radar</TabsTrigger>
            <TabsTrigger value="decision">Decision Matrix</TabsTrigger>
          </TabsList>

          <TabsContent value="overview">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-4">
              <Card className="lg:col-span-2">
                <CardHeader>
                  <CardTitle className="text-lg">Chart Title</CardTitle>
                  <CardDescription>Chart description</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={380}>
                    <BarChart data={performanceData}>
                      <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                      <XAxis dataKey="metric" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="optionA" name="Option A" fill={chartColors.c1} radius={[4,4,0,0]} />
                      <Bar dataKey="optionB" name="Option B" fill={chartColors.c2} radius={[4,4,0,0]} />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
              <Card>
                <CardHeader><CardTitle className="text-lg">Analysis</CardTitle></CardHeader>
                <CardContent className="space-y-4 text-sm text-muted-foreground">
                  <div>
                    <h4 className="font-medium text-foreground mb-1">Key Finding</h4>
                    <p>Analysis text with formulas:</p>
                    <code className="block mt-2 p-2 bg-muted rounded-md text-xs font-mono">
                      formula = here
                    </code>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
          {/* ... more TabsContent for each tab */}
        </Tabs>

        {/* Methodology */}
        <Card>
          <CardContent className="p-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 text-sm">
              <div>
                <h4 className="font-medium text-foreground mb-2">Literature Review</h4>
                <p className="text-muted-foreground">Description of sources and search strategy</p>
              </div>
              {/* ... more methodology columns */}
            </div>
          </CardContent>
        </Card>

        {/* References */}
        <Card>
          <CardContent className="p-6">
            <div className="space-y-2 text-sm">
              <div className="flex gap-3">
                <span className="text-muted-foreground font-mono text-xs w-6 shrink-0">[1]</span>
                <p className="text-muted-foreground">
                  <span className="text-foreground">Author(s)</span> (Year). "Title." <em>Venue</em>.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Footer */}
        <footer className="border-t pt-6 pb-8 text-center text-sm text-muted-foreground">
          <p>Generated by tech-rd plugin | Report ID: TRD-YYYY-MMDD-XX</p>
        </footer>
      </main>
    </div>
  )
}
