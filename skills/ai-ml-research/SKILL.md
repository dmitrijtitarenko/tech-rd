---
name: AI/ML Research
description: >
  Deep analysis of AI/ML papers, models, benchmarks, datasets, and training infrastructure.
  Answer "ML model for", "AI research on", "best LLM for", "training infrastructure" questions.
  Evaluate benchmark scores, parameter efficiency, inference costs, and dataset coverage.
  Critical for selecting models, understanding research directions, and assessing production readiness.
---

# AI/ML Research Domain

## Overview

The AI/ML research domain bridges cutting-edge academic research with practical deployment constraints. This skill synthesizes paper analysis, benchmark interpretation, and infrastructure evaluation to surface the most suitable models and training approaches for specific problems.

The space moves rapidly: a state-of-the-art model from last year may be obsolete today, replaced by something smaller and faster. Effective research here means separating genuine advances from incremental improvements, understanding benchmark construction (to avoid false comparisons), and quantifying real-world performance gaps between academic metrics and production constraints.

## Key Research Dimensions

**Model Performance & Accuracy**
- Benchmark performance (ImageNet, SQuAD, MMLU, GLUE, etc.)
- Downstream task transfer performance
- Few-shot and zero-shot capabilities
- Robustness to distribution shift and adversarial inputs
- Fairness and bias analysis across subgroups

**Efficiency & Scalability**
- Parameter count and model size in memory
- Inference latency and throughput (tokens/sec for LLMs)
- Training time and data requirements
- Quantization and pruning effectiveness
- Batching and hardware utilization patterns

**Data & Pretraining**
- Training dataset composition and size
- Data quality issues and contamination analysis
- Pretraining objectives (next-token prediction, masked language model, contrastive)
- Instruction-tuning datasets and alignment approaches
- Copyright and licensing implications

**Infrastructure & Reproducibility**
- Hardware requirements (GPU/TPU count, memory, compute)
- Training cost and scalability curves
- Code availability and reproducibility ratings
- Checkpoints and model weights distribution
- Fine-tuning stability and convergence properties

## Data Sources & Query Methods

**Benchmark Databases**
- Papers with Code (paperswithcode.com) — benchmark results linked to implementations
- Hugging Face Model Hub — performance metrics, model cards, inference API
- OpenCompass (AI benchmarking) — systematic evaluation across models
- HELM (Holistic Evaluation of Language Models) — comprehensive LLM testing
- Query pattern: "benchmark results [model/task]", "SOTA [domain]"

**Research Papers & Preprints**
- arXiv filtered by cs.AI, cs.CV, cs.CL for latest papers
- Papers with Code searches for methods and datasets
- Google Scholar for citation counts and related work
- Semantic Scholar API for paper relationships and influence
- Query pattern: "recent research [topic]", "breakthrough [area]"

**Model Availability & Licensing**
- Hugging Face Model Hub (license filtering, model cards)
- Model Zoo repositories for each domain
- GitHub releases for open-source implementations
- Commercial API pricing (OpenAI, Anthropic, Mistral, etc.)
- Query pattern: "open-source models [task]", "model weights [architecture]"

**Infrastructure & Efficiency**
- MLPerf benchmarks for training efficiency and inference latency
- Scaling laws papers and trend analysis
- GPU pricing and availability (Lambda Labs, Lambda Cloud, AWS pricing)
- Energy consumption studies and carbon footprint data
- Query pattern: "training infrastructure [model size]", "inference cost [model]"

**Datasets & Licensing**
- Hugging Face Datasets library (with licensing info)
- Papers with Code datasets section (links to downloads and papers)
- Dataset documentation for train/test split and benchmark details
- Licensing tools (SPDX, Creative Commons, research-only restrictions)
- Query pattern: "dataset for [task]", "benchmark construction [metric]"

## Analysis Frameworks

**Model Suitability Matrix**
- **Accuracy**: Benchmark performance on target task (% improvement over baseline)
- **Efficiency**: Inference latency + memory footprint vs accuracy (Pareto frontier)
- **Data Requirements**: Labeled data needed for fine-tuning (learning curve analysis)
- **Implementation Difficulty**: Tokenization, preprocessing, inference framework support
- **Cost**: Hardware + inference API costs at expected volume

**Benchmark Credibility Assessment**
- Is the benchmark widely adopted by other researchers? (citation count, multiple papers)
- Does it test the claimed capability? (feature collapse, distribution shift)
- Are train/test splits public and non-overlapping?
- Have models been evaluated by independent researchers?
- Are failure modes documented?

**Scaling Analysis**
- Compute-optimal allocation: balance model size vs training tokens
- Double descent phenomena: when does adding capacity hurt generalization?
- Transfer learning effectiveness: how much data needed for target task?
- Diminishing returns curves: when does further scaling stop helping?
- Extrapolation reliability: can we predict performance beyond current scale?

**Real-World Readiness Assessment**
- Latency requirements: batch size 1 inference time under SLA?
- Throughput capacity: tokens/sec at expected QPS?
- Memory constraints: model + KV cache + batch memory?
- Hardware availability: can you acquire the GPUs/TPUs needed?
- Operational complexity: monitoring, updates, A/B testing infrastructure?

## Output Format Templates

### Model Selection Report
```
Task: [classification/segmentation/generation/etc.]
Recommended Model: [name, version]
Key Metrics: [accuracy, latency, memory]

Performance: [vs alternatives, benchmark scores]
Efficiency: [inference cost breakdown]
Data Requirements: [labeled examples needed for fine-tuning]
Implementation: [framework support, tokenization notes]
Risks: [benchmark specificity, distribution shift, fairness gaps]
```

### Research Trend Analysis
```
Topic: [area of research]
Key Developments: [recent papers, benchmark improvements]
Momentum: [publication rate, citation velocity, industry adoption]
Inflection Points: [when did scaling become dominant? etc.]
Open Questions: [what remains unsolved]
Investment Implications: [which approaches likely to succeed]
```

### Training Infrastructure Recommendation
```
Model Size: [parameter count, context length]
Compute Budget: [hours, GPU-hours, cost]
Data Preparation: [preprocessing steps, quality filtering]
Training Strategy: [distributed approach, precision, optimization]
Estimated Duration: [wall-clock time]
Reproducibility Notes: [seeds, numerical stability issues]
```

### Benchmark Interpretation Brief
```
Benchmark: [name]
Measured Capability: [what it actually tests]
Limitations: [what it doesn't test, potential artifacts]
Comparison Validity: [is comparing models X vs Y on this metric valid?]
Real-World Correlation: [does benchmark score predict production performance?]
Cautions: [common misinterpretations, gotchas]
```

## Key Metrics to Always Extract

For any model evaluation, collect:
1. **Performance**: Exact benchmark scores with confidence intervals
2. **Efficiency**: Latency (ms) at batch size 1 and typical batch size; memory (GB)
3. **Scale**: Parameter count, training data size (tokens/examples), compute cost
4. **Reproducibility**: Seed stability, convergence issues, hardware dependencies
5. **Ablation**: What design choices matter most? (layer count, attention heads, etc.)
6. **Failure modes**: Where does the model struggle? (edge cases, distribution shift)

## Computational Workflows

**Pre-built Analysis Scripts**
- `benchmark_pareto_frontier.py` — Plot accuracy vs latency vs model size using pandas/matplotlib to identify efficiency frontier
- `scaling_law_analyzer.py` — Fit compute-optimal curves using numpy/scipy (loss vs parameter count, FLOPs) for predictive scaling
- `inference_cost_calculator.py` — Compute per-token costs across models with different quantization and batch sizes using pandas
- `training_cost_projector.py` — Model GPU-hour requirements from published papers with statistical confidence intervals

**Dynamic Computation Examples**
- When selecting models, compute Pareto frontier from benchmark matrix (accuracy, latency, memory) to eliminate dominated options
- When estimating training cost, run Monte Carlo simulation on compute requirements with parameter uncertainties
- When analyzing scaling laws, fit exponential models to benchmark results to project performance at larger scales

**Output Artifacts**
- Pareto frontier visualization (scatter: accuracy vs latency with dominance highlighting)
- Benchmark comparison tables with computed scores and ranking
- Training cost projection charts (line/area: GPU-hours vs model size with confidence bands)
- Mermaid flowchart showing model selection decision path based on performance requirements
- LaTeX formula: Chinchilla scaling law: D = 20 * C^0.75, N = 0.5 * C^0.75 (optimal data/parameter ratios)

## References

Load from `references/` directory:
- `benchmark-methodology.md` — how to interpret benchmark results critically
- `llm-scaling-laws.md` — compute-optimal training and inference efficiency
- `model-licensing-landscape.md` — open vs proprietary tradeoffs
- `fine-tuning-strategies.md` — best practices for adaptation to downstream tasks
- `inference-optimization-techniques.md` — quantization, distillation, serving patterns

## Common Pitfalls to Avoid

- **Benchmark overfitting**: Models improve on published benchmarks faster than on new tasks
- **Publication bias**: Successful approaches published; failure cases hidden
- **Hardware specificity**: Model fast on A100s may be slow on consumer GPUs
- **Transfer learning assumptions**: Domain shift is subtle; test on your actual data
- **Cost underestimation**: Inference API costs compound at scale; factor in per-token fees
- **Reproducibility failure**: Old code doesn't run on new frameworks; verify before committing

## Data Sources

This skill is enhanced by the following connected data sources:

- **~~ml platform**: Access Hugging Face model hub, Weights & Biases experiment tracking, MLflow model registry
- **~~research**: Paper access via Semantic Scholar, arXiv preprints, research trend signals
- **~~source control**: GitHub repositories for open-source implementations, model weights, benchmark code
- **~~web research**: Real-time benchmark results, latest model announcements, performance comparisons

Replace `~~category` with your configured MCP server (see CONNECTORS.md).
