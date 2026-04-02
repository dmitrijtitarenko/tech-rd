---
name: Quantum Computing Research
description: >
  Quantum hardware, quantum algorithms, error correction, NISQ era, quantum ML, quantum chemistry.
  Address "quantum computing for", "quantum algorithm", "qubit technology", "quantum advantage" questions.
  Evaluate qubit count, gate fidelity, coherence time, algorithm applicability, and near-term viability.
  Critical for understanding quantum opportunity and hype separation.
---

# Quantum Computing Research Domain

## Overview

Quantum computing research synthesizes quantum physics, algorithms, and hardware engineering to assess when and where quantum computers provide advantage over classical systems. This domain encompasses quantum hardware platforms (superconducting qubits, trapped ions, photonic), the NISQ (Noisy Intermediate-Scale Quantum) era, and emerging applications.

Effective research here means understanding: which problems can quantum computers actually solve? How do quantum errors limit current systems? What does "quantum advantage" really mean for specific applications?

## Key Research Dimensions

**Quantum Hardware & Platforms**
- Superconducting qubits: IBM, Google approach; coherence times microseconds
- Trapped ions: IonQ approach; longer coherence, lower gate speeds
- Photonic qubits: Xanadu approach; room temperature operation
- Topological qubits: Microsoft approach; theoretical error resistance
- Neutral atom qubits: QuEra approach; flexible qubit count
- Hybrid classical-quantum: Current practical approach

**Quantum Performance Metrics**
- Qubit count: Number of qubits (but quality matters more than count)
- Gate fidelity: Error rate per quantum gate (99% fidelity = 1 error per 100 gates)
- Coherence time: How long qubits maintain quantum state (T1 and T2 times)
- Two-qubit gate time: Speed to entangle qubits (impacts algorithm duration)
- Error mitigation techniques: Recovering accuracy despite noise
- Circuit depth: How many gate operations needed (limited by coherence time)

**Quantum Algorithms & Applications**
- Shor's algorithm: Factoring (breaks RSA encryption at scale)
- Grover's algorithm: Unstructured search (quadratic speedup)
- VQE (Variational Quantum Eigensolver): Finding ground states
- QAOA (Quantum Approximate Optimization): Solving optimization problems
- Quantum simulation: Simulating quantum systems (chemistry, materials)
- Machine learning: Quantum ML remains largely theoretical

**Error Correction & Fault Tolerance**
- Quantum error correction codes: Spread logical qubits across many physical qubits
- Overhead: Number of physical qubits per logical qubit (potentially thousands)
- Threshold: Gate fidelity required for error correction to work
- Practical timeline: Fault-tolerant quantum computer estimated 10-20+ years
- NISQ advantage: Exploiting current noisy systems without error correction

**Near-Term Applications (NISQ Era)**
- Drug discovery: Molecular simulation (though small molecules only currently)
- Optimization: Solving constrained optimization problems
- Finance: Portfolio optimization, pricing models
- Materials science: Finding new materials with desired properties
- Chemistry: Simulating chemical reactions at scale
- Proof of concept: Most applications still in research phase

## Data Sources & Query Methods

**Quantum Hardware Benchmarking**
- IBM Quantum Experience: Open access to IBM quantum computers, benchmark results
- Google Quantum AI: Papers on quantum advantage claims and limitations
- IonQ benchmarks: Trapped ion performance metrics
- Xanadu PennyLane: Quantum ML framework with benchmark results
- Query pattern: "quantum hardware comparison", "qubit fidelity benchmarks"

**Quantum Algorithm Research**
- arXiv cs.QA (quantum algorithms): Latest algorithm papers
- Qiskit, Cirq, PennyLane documentation: Algorithm implementations
- Papers with Code: Quantum algorithm implementations with benchmarks
- Query pattern: "quantum algorithm for [problem]", "quantum speedup"

**Quantum Error Correction & Fault Tolerance**
- Theoretical papers on error correction codes (surface code, toric code)
- Google/IBM roadmaps: Path to fault-tolerant quantum computing
- Research papers: Error correction overhead estimates
- Query pattern: "quantum error correction", "fault-tolerant quantum"

**Industry Commercialization Progress**
- Company blogs: IBM, Google, IonQ, Rigetti progress updates
- Gartner reports on quantum computing hype cycle positioning
- Job market: Quantum computing roles available
- Startup funding: VC investment in quantum companies
- Query pattern: "quantum computing commercialization", "quantum startup"

**Quantum Applications & Use Cases**
- Research papers on quantum applications in specific domains
- Company partnerships: Which companies running quantum pilots?
- Case studies: Real-world quantum computing projects and results
- Query pattern: "quantum computing application [domain]", "quantum chemistry"

## Analysis Frameworks

**Quantum Advantage Assessment** (for specific problem)
- **Problem characteristics**: Is this an optimization, simulation, or search problem?
- **Classical baseline**: How does best classical algorithm perform?
- **Quantum advantage**: Can quantum be faster even accounting for overhead?
- **Practical advantage**: Considering current noise, can we achieve advantage today?
- **Scaling**: As problem size grows, does quantum advantage improve or diminish?
- **Implementation**: Can we actually implement the quantum algorithm?

**Quantum Hardware Evaluation**
- **Qubit quality**: Gate fidelity and coherence times vs competitors
- **Scalability**: Can architecture scale to needed number of qubits?
- **Architecture**: Linear, grid, or all-to-all connectivity?
- **Available operations**: Which gates can be implemented natively?
- **Access model**: Cloud access, private systems, lease options
- **Cost**: Per-job pricing, reserved time costs
- **Supplier credibility**: How many research papers from this platform?

**NISQ Application Fit Assessment**
- **Circuit depth**: Can algorithm fit within coherence time?
- **Noise resilience**: Is algorithm robust to gate errors?
- **Error mitigation**: Can error mitigation recover accuracy?
- **Hybrid approach**: Can classical preprocessing reduce quantum circuit?
- **Proof of concept value**: Even if not faster, does it demonstrate technology?
- **Data availability**: Do you have real data to test on?

**Quantum ML Feasibility** (for specific use case)
- **Problem suitability**: Are quantum ML algorithms actually applicable?
- **Advantage mechanism**: Where does quantum speedup come from?
- **Current maturity**: Are algorithms beyond proof-of-concept?
- **Data encoding**: Converting classical data to quantum state efficiently?
- **Readout overhead**: Can you efficiently extract answer from quantum state?
- **Realistic timeline**: When might this be practically viable?

**Quantum-Ready Planning** (for organizations planning future adoption)
- **Skill development**: Training team on quantum algorithms and hardware
- **Problem identification**: Identifying candidate problems for quantum computing
- **Simulation**: Using classical simulators to prototype quantum algorithms
- **Cloud access**: Setting up access to cloud quantum computers for testing
- **Partnerships**: Collaborating with quantum research institutions
- **Monitoring progress**: Tracking quantum hardware advancement

## Output Format Templates

### Quantum Hardware Comparison
```
Use Case: [optimization/simulation/search]
Problem Size: [number of variables, circuit depth needed]

Hardware Candidates: [IBM, Google, IonQ, etc.]

IBM Quantum: [qubit count, fidelity, coherence, availability]
Google Quantum: [qubit count, fidelity, coherence, availability]
IonQ: [qubit count, fidelity, coherence, availability]

Recommendation: [which hardware best matches use case]
Algorithm Fit: [can algorithm run with current noise levels?]
Cost: [per-job pricing, expected costs]
Timeline: [when will hardware reach production-grade?]
```

### Quantum Algorithm Analysis
```
Problem: [specific optimization or simulation challenge]
Problem Size: [scale of problem]

Classical Baseline: [best known classical algorithm, runtime]
Quantum Approach: [quantum algorithm, expected speedup]

Complexity Analysis: [theoretical speedup in big-O notation]
Implementation Status: [research only, prototype, production-ready?]
Error Mitigation: [techniques to recover from noise]
Practical Viability: [can current hardware run it well?]

Recommendation: [pursue further or not worth now]
Research Timeline: [when might become practical]
```

### Quantum ML Feasibility Study
```
ML Task: [classification, clustering, optimization, regression]
Problem Scale: [number of features, samples]

Quantum ML Approach: [VQE, QAOA, quantum kernel, etc.]
Advantage Claim: [what speedup is claimed?]
Current Status: [research papers? commercial implementations?]

Complexity Analysis: [quantum circuit depth, gate count]
Noise Resilience: [sensitivity to errors]
Hardware Requirements: [qubit count, fidelity needed]
Timeline to Viability: [when realistically practical]

Recommendation: [classical vs quantum approach]
```

### Quantum-Ready Organizational Strategy
```
Current State: [no quantum expertise, want to prepare]
Target Opportunity: [specific problem domain]

Skill Development: [training programs, hiring, partnerships]
Problem Pipeline: [candidate problems for quantum computing]
Experimentation: [cloud quantum access, simulators]

Year 1: [foundational work, learning]
Year 2-3: [algorithm development, pilot projects]
Year 5+: [production quantum systems expected]

Success Criteria: [what does success look like?]
Budget: [training, partnerships, compute access]
```

## Key Metrics to Always Collect

For quantum decisions, track:
1. **Hardware metrics**: Qubit count, gate fidelity, coherence times, error rates
2. **Algorithm efficiency**: Circuit depth, gate count, algorithm runtime
3. **Noise impact**: Error mitigation effectiveness, final answer accuracy
4. **Scaling**: How do metrics change with problem size?
5. **Advantage timeline**: When might quantum be faster than classical?
6. **Cost**: Per-job pricing, total cost for research program
7. **Progress rate**: How fast are fidelity/coherence improving?

## Computational Workflows

**Pre-built Analysis Scripts**
- `quantum_advantage_analyzer.py` — Compare classical vs quantum complexity (algorithm runtime, circuit depth) with numpy
- `error_mitigation_effectiveness_calculator.py` — Model accuracy recovery from error mitigation techniques using scipy
- `hardware_roadmap_projector.py` — Forecast qubit quality (fidelity, coherence) improvements with trend fitting
- `fault_tolerance_overhead_estimator.py` — Calculate physical qubits needed for logical qubits given error thresholds

**Dynamic Computation Examples**
- When assessing quantum advantage, compute speedup accounting for circuit depth constraints from current coherence times
- When planning quantum research, run timeline simulation on fidelity improvement needed to reach practical advantage
- When evaluating algorithms, calculate circuit depth and gate count to assess feasibility on current NISQ hardware

**Output Artifacts**
- Complexity comparison chart (classical vs quantum algorithm scaling with problem size)
- Hardware fidelity roadmap (line chart: gate fidelity trend with milestones to fault tolerance)
- Circuit depth vs coherence time scatter plot (feasible region highlighted)
- Mermaid flowchart showing problem suitability assessment for quantum computing
- LaTeX formula: Quantum_Advantage = Classical_Ops / (Circuit_Depth * Error_Rate^Depth) > 1; break-even speedup threshold

## References

Load from `references/` directory:
- `quantum-hardware-roadmap-2024.md` — IBM, Google, IonQ progress and timelines
- `quantum-algorithm-zoo.md` — catalog of quantum algorithms and complexity analysis
- `quantum-error-correction-explained.md` — error correction codes and overhead
- `nisq-applications.md` — near-term quantum computing applications
- `quantum-ml-survey.md` — quantum ML approaches and current limitations
- `quantum-advantage-assessment.md` — framework for evaluating quantum speedup claims
- `quantum-cloud-platforms.md` — IBM Quantum, Google, Azure Quantum comparison

## Common Pitfalls to Avoid

- **Qubit count mythology**: More qubits don't matter if fidelity is poor (quality over quantity)
- **Quantum supremacy confusion**: Google's quantum advantage on synthetic problem ≠ useful quantum computer
- **Hype belief**: Quantum ML is mostly hype; classical ML still wins most real problems
- **Hardware maturity underestimation**: 10-20 year timeline for fault-tolerant systems is realistic
- **Circuit depth ignorance**: Algorithms need too many gates for current decoherence times
- **Error correction costs**: Fault tolerance requires thousands of physical qubits per logical qubit
- **Advantage miscalculation**: Quantum faster on paper but slower including overhead
- **Timeline optimism**: "Quantum advantage in 5 years" has been claimed since 2010

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~research**: Academic papers on quantum algorithms, error correction, hardware benchmarks
- **~~web research**: Hardware announcements, progress updates, benchmark results
- **~~source control**: Quantum software implementations, algorithm libraries, simulators

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
