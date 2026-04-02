---
name: Graphics, 3D, and XR Research
description: >
  Rendering engines, game engines (Unity, Unreal), AR/VR, spatial computing, WebGPU, Vulkan, ray tracing.
  Address "game engine for", "3D rendering approach", "AR/VR platform", "spatial computing", "graphics API" questions.
  Evaluate performance, platform support, asset pipeline, developer tools, and content creation workflow.
  Essential for gaming, XR applications, and real-time 3D experiences.
---

# Graphics, 3D, and XR Research Domain

## Overview

Graphics and 3D research synthesizes rendering technologies, game engine capabilities, and immersive computing platforms to enable real-time 3D experiences from games to enterprise applications. This domain spans traditional rendering (rasterization, ray tracing), game engines (Unity, Unreal), and emerging spatial computing (AR/VR/MR).

Effective research here means understanding: which engine meets your performance and workflow requirements? How do different graphics APIs (Vulkan, Metal, WebGPU) affect portability? What's the real cost of shipping on multiple platforms?

## Key Research Dimensions

**Rendering Techniques & Performance**
- Rasterization: traditional real-time graphics pipeline
- Ray tracing: photo-realistic rendering (expensive, improving)
- Path tracing: global illumination simulation (slow but accurate)
- Deferred rendering: handling many lights efficiently
- Procedural generation: creating assets algorithmically
- Level of detail (LOD): reducing geometry at distance
- Performance targets: frame rates (60/120/144 fps), resolution, visual quality

**Game Engine Capabilities**
- **Unity**: C#, cross-platform, asset store, mobile/console support
- **Unreal Engine**: C++, console-focused, visual scripting (Blueprints)
- **Godot**: Open source, lighter weight, growing community
- **Proprietary engines**: Used by AAA studios for maximum control
- **Web engines**: Babylon.js, Three.js for browser-based 3D
- Feature set: physics, networking, UI, sound, animation

**Platform & Deployment Targets**
- **PC**: Windows/Mac/Linux, highest performance and flexibility
- **Console**: PlayStation, Xbox, Nintendo (certification requirements)
- **Mobile**: iOS/Android, performance constraints, power management
- **Web**: WebGL, WebGPU, Wasm for browser-based experiences
- **AR/VR**: Standalone (Meta Quest) vs tethered (SteamVR) vs mobile VR
- **Spatial computing**: Apple Vision Pro and emerging platforms

**Asset Creation & Pipeline**
- 3D modeling tools: Blender, Maya, 3DS Max
- Texture creation: Substance Painter, Marmoset Toolbag
- Animation: bone rigging, motion capture integration
- Shader development: HLSL, GLSL, custom shader languages
- Build times: asset preprocessing, baking, compression
- Streaming: loading assets dynamically for large worlds

**Graphics APIs & Standards**
- **Vulkan**: Modern, low-level, best performance but complex
- **DirectX 12**: Windows/Xbox exclusive, mature tooling
- **Metal**: Apple exclusive, optimized for Apple hardware
- **OpenGL**: Cross-platform legacy, simpler but less performant
- **WebGPU**: Emerging standard for web graphics, future-focused
- **OptiX**: NVIDIA ray tracing API

## Data Sources & Query Methods

**Engine Benchmarking & Comparison**
- GFXBench: GPU benchmarks across engines and platforms
- FrameView: Frame rate analysis and performance profiling
- UE5 Nanite/Lumen benchmark results
- Unity benchmarking guides and community benchmarks
- Console manufacturer optimization guides
- Query pattern: "game engine performance", "ray tracing benchmark"

**Platform & Market Data**
- StatCounter: Gaming platform market share (PC/console/mobile)
- Newzoo/GamesBeat reports on platform trends
- App Store/Play Store download statistics
- Console generation lifecycles and install bases
- Query pattern: "gaming platform trends", "console market share"

**Developer Tools & Workflow**
- GitHub repositories for engine integrations
- Asset store ecosystems (Unity Asset Store, Unreal Marketplace)
- Developer survey reports (GDC, VRChat, etc.)
- Documentation quality and tutorial availability
- Community size and third-party tool support
- Query pattern: "game engine tools", "asset pipeline workflow"

**AR/VR & Spatial Computing**
- Platform specifications: Meta Quest, Apple Vision Pro, HoloLens
- Development kits and SDKs (Niantic's Lightship, etc.)
- Industry adoption: enterprise vs consumer VR
- Use case effectiveness data (retention, engagement)
- Query pattern: "AR/VR platform comparison", "spatial computing"

**Graphics Technology Trends**
- NVIDIA DLSS vs AMD FSR: upscaling technologies
- Real-time ray tracing adoption and performance
- Procedural generation advances
- Machine learning-based content creation
- Query pattern: "ray tracing implementation", "upscaling technology"

## Analysis Frameworks

**Engine Selection Matrix**
- **Performance**: Target frame rates, geometry complexity, lighting quality
- **Workflow**: Team expertise, asset pipeline, editor familiarity
- **Platforms**: Which platforms must you ship? (PC, console, mobile)
- **Portability**: Ease of exporting to multiple platforms
- **Ecosystem**: Available plugins, tutorials, asset availability
- **Cost**: Licensing (free, percentage royalty, fixed fee)

**Platform Prioritization Strategy**
- **Market size**: How many potential players on each platform?
- **Monetization**: Revenue per user, adoption costs, payment models
- **Development cost**: How much more to support this platform?
- **Time to launch**: Can you meet platform-specific deadlines?
- **Technical risk**: Which platform has performance unknowns?

**Graphics API Selection**
- **Cross-platform target**: Vulkan + Metal or DirectX 12?
- **Performance budget**: How much GPU power available?
- **Shader complexity**: Simple (OpenGL) vs advanced (Vulkan)?
- **Team expertise**: Which API does your team know best?
- **Tool maturity**: Validation layers, debugging, profiling tools available?

**Ray Tracing ROI Assessment**
- **Visual impact**: Does ray tracing improve perceived quality for this game?
- **Performance cost**: FPS loss with ray tracing enabled?
- **Upscaling assistance**: Can DLSS/FSR recover performance?
- **Hardware support**: What % of target platform can run it?
- **Development cost**: Time to implement vs visual gain?

**Mobile Gaming Economics**
- **Device capabilities**: GPU/CPU constraints across target devices
- **Battery impact**: How does this feature affect battery drain?
- **Network**: Is multiplayer possible with network constraints?
- **Monetization model**: Ads, IAP, subscription viability?
- **User acquisition cost**: How much to market this game?

## Output Format Templates

### Game Engine Selection
```
Project: [game concept, scope, platform targets]
Team: [size, expertise, tool familiarity]

Engine A: [pros/cons, learning curve, cost]
Engine B: [pros/cons, learning curve, cost]
Engine C: [pros/cons, learning curve, cost]

Recommendation: [which engine wins and why]
Team Training: [ramp-up time, resources needed]
Asset Pipeline: [workflow from creation to in-game]
Performance Targets: [achievable frame rates on target platforms]
```

### 3D Graphics Architecture
```
Art Direction: [realistic, stylized, mobile-optimized]
Target Platforms: [PC, console, mobile, VR]

Rendering Approach: [rasterization, ray tracing, hybrid]
Resolution & Frame Rate: [target performance]
Shader Complexity: [number of shader variants]
Asset Budget: [polygon count, texture memory]
Lighting: [real-time, baked, mixed approach]

LOD Strategy: [how to optimize for distance]
Streaming: [dynamic loading for large world]
Build Pipeline: [preprocessing, optimization, compression]
```

### Platform Strategy Decision
```
Target Audience: [platform preferences]
Market Analysis: [install base, growth potential]

Platform A: [revenue potential, dev effort, timeline]
Platform B: [revenue potential, dev effort, timeline]
Platform C: [revenue potential, dev effort, timeline]

Launch Priority: [which platform first]
Staggered Timeline: [platform release order]
Technical Challenges: [platform-specific constraints]
Certification Requirements: [approval process, duration]
```

### AR/VR Implementation Guide
```
Use Case: [enterprise training, consumer game, etc.]
Target Platform: [Meta Quest, Apple Vision Pro, etc.]

User Experience: [interaction model, comfort considerations]
Performance Targets: [frame rate, latency for VR sickness]
Content Type: [static, interactive, multiplayer]
Hardware Constraints: [memory, battery, processing]

Development Kit: [platform SDK, middleware]
Testing: [VR testing methodology, user feedback]
Deployment: [app store requirements, distribution]
Success Metrics: [engagement, retention, monetization]
```

## Key Metrics to Always Collect

For graphics/XR decisions, track:
1. **Performance**: Frame rate P99, frame time variance, FPS on target hardware
2. **Quality**: Visual fidelity vs performance tradeoff (measure player perception)
3. **Asset efficiency**: Memory used, load times, draw call count
4. **Platform coverage**: FPS achieved on minimum-spec target hardware
5. **Development velocity**: Asset creation speed, iteration time
6. **User experience**: Motion sickness (VR), input responsiveness, visual clarity

## Computational Workflows

**Pre-built Analysis Scripts**
- `frame_rate_performance_analyzer.py` — Parse profiler data with pandas to compute FPS variance and identify bottlenecks
- `memory_budget_calculator.py` — Model polygon/texture memory allocation across LOD levels using numpy
- `ray_tracing_cost_estimator.py` — Estimate ray-traced frame render time vs quality tradeoff with performance models
- `platform_porting_effort_model.py` — Predict development cost for multi-platform support using complexity matrices

**Dynamic Computation Examples**
- When optimizing graphics, compute frame time budget allocation (rasterization vs ray tracing vs post-effects)
- When planning platform support, run scenario analysis on development cost vs addressable market for each platform
- When assessing ray tracing ROI, model FPS cost vs visual improvement perception scores

**Output Artifacts**
- Frame time breakdown stacked bar chart (rendering/physics/AI/overhead per frame)
- FPS target feasibility chart (line: target platform, bar: achieved fps at different quality levels)
- Asset memory heatmap (texture resolution vs mesh complexity, color: memory used)
- Mermaid diagram showing rendering pipeline and optimization stages
- LaTeX formula: Frame_Time_Budget (ms) = 1000 / Target_FPS; e.g., 60fps = 16.67ms budget per frame

## References

Load from `references/` directory:
- `game-engine-comparison-2024.md` — detailed feature and cost analysis
- `graphics-api-guide.md` — Vulkan vs DirectX vs Metal technical comparison
- `ray-tracing-implementation.md` — performance, quality, upscaling tradeoffs
- `mobile-optimization-guide.md` — mobile GPU constraints and best practices
- `vr-performance-guidelines.md` — frame rate, latency, motion sickness prevention
- `asset-pipeline-workflow.md` — from creation to game integration
- `platform-porting-costs.md` — effort to port between PC/console/mobile/VR

## Common Pitfalls to Avoid

- **Engine hyperbole**: Latest engine features don't matter if they kill performance
- **Platform underestimation**: Console certification takes longer than expected
- **Asset bloat**: 4K textures look great until game won't fit on storage
- **VR sickness**: Frame rate/latency misses cause user discomfort; test early
- **Cross-platform woes**: "It works on PC" doesn't mean it works on console
- **Shader complexity**: Fancy visual effects don't matter if game runs at 30fps
- **Mobile amnesia**: Targeting mobile late in development costs months
- **Ray tracing waste**: Expensive technique on hardware that doesn't support it well
