TECH R&D ANALYSIS SCRIPTS
==========================

8 pre-built Python analysis templates for research and evaluation tasks.
All scripts are executable and include example data for immediate use.

SCRIPTS:
--------

1. tco_calculator.py
   Total Cost of Ownership calculator for cloud services
   - Pricing tiers, compute, storage costs
   - 12-month and 36-month projections
   - Team size scaling
   - Example: PostgreSQL, MongoDB, DynamoDB pricing

2. benchmark_comparison.py
   Statistical comparison of benchmark results
   - Mean, median, p95, p99, standard deviation
   - Mann-Whitney U significance testing
   - Scipy.stats integration
   - Example: Algorithm performance comparison

3. trend_analyzer.py
   Adoption trend analysis over time
   - Growth rate and acceleration computation
   - Moving averages and exponential smoothing
   - Linear regression fit quality (R-squared)
   - Future value projections
   - Example: GitHub stars, npm downloads trends

4. scoring_model.py
   Multi-criteria weighted scoring system
   - Weighted score calculation
   - Ranking and normalization
   - Sensitivity analysis (weight changes +/-20%)
   - Example: Technology solution evaluation

5. risk_scorer.py
   Risk assessment and portfolio analysis
   - Likelihood (1-5) and impact (1-5) scoring
   - Composite risk calculation
   - High/Medium/Low categorization
   - Portfolio risk aggregation
   - Example: Technical and organizational risks

6. market_share_estimator.py
   Market position estimation from proxy signals
   - Normalized GitHub stars, npm downloads
   - Stack Overflow questions, job postings
   - Configurable signal weights
   - Market share percentages
   - Example: JavaScript framework comparison

7. scaling_simulator.py
   Scaling behavior simulation and projection
   - Linear, logarithmic, polynomial models
   - Curve fitting with R-squared validation
   - Projections to target scales
   - Growth factor calculation
   - Example: Latency vs dataset size

8. radar_generator.py
   Tech radar generation (ThoughtWorks compatible)
   - Quadrant and ring assignments
   - JSON and CSV output formats
   - New/established technology marking
   - Ready for build-your-own-radar tool
   - Example: 8-technology radar with 4 quadrants

DEPENDENCIES:
--------------
Required: pandas, numpy, scipy

Install with: pip install pandas numpy scipy

USAGE:
------
Each script has example data in the if __name__ == "__main__" block.
Run any script directly: python3 <script_name>.py

All scripts are parameterized for custom data inputs.
See function docstrings for detailed parameter specifications.

