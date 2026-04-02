#!/usr/bin/env python3
"""
Statistical comparison of benchmark results.

Compares two or more sets of measurements and performs statistical analysis
including descriptive statistics and Mann-Whitney U test for significance.

Input: Multiple arrays of benchmark measurements
Output: Comparison table and p-value from significance test
"""

import pandas as pd
import numpy as np
try:
    from scipy import stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


def compare_benchmarks(benchmark_groups):
    """
    Compare multiple sets of benchmark measurements.

    Args:
        benchmark_groups: Dict with names as keys and arrays of measurements as values

    Returns:
        Tuple of (comparison_df, significance_results_dict)
    """
    results = []

    for name, measurements in benchmark_groups.items():
        measurements = np.array(measurements)
        results.append({
            'name': name,
            'count': len(measurements),
            'mean': np.mean(measurements),
            'median': np.median(measurements),
            'std_dev': np.std(measurements),
            'p95': np.percentile(measurements, 95),
            'p99': np.percentile(measurements, 99),
            'min': np.min(measurements),
            'max': np.max(measurements)
        })

    df = pd.DataFrame(results)

    significance = {}
    names = list(benchmark_groups.keys())
    if len(names) >= 2:
        stat, p_value = stats.mannwhitneyu(
            benchmark_groups[names[0]],
            benchmark_groups[names[1]]
        )
        significance = {
            'comparison': f"{names[0]} vs {names[1]}",
            'statistic': stat,
            'p_value': p_value,
            'significant_at_0.05': p_value < 0.05
        }

    return df, significance


if __name__ == "__main__":
    benchmarks = {
        'Algorithm A': np.random.normal(100, 15, 50),
        'Algorithm B': np.random.normal(95, 12, 50),
        'Algorithm C': np.random.normal(110, 20, 50)
    }

    comparison_df, sig_results = compare_benchmarks(benchmarks)

    print("Benchmark Comparison Summary")
    print(comparison_df.to_string(index=False))
    print("\n" + "="*60)
    print("Statistical Significance Test (Mann-Whitney U)")
    print("="*60)
    if sig_results:
        print("Comparing: {}".format(sig_results['comparison']))
        print("p-value: {:.4f}".format(sig_results['p_value']))
        print("Significant at 0.05 level: {}".format(sig_results['significant_at_0.05']))
    else:
        print("Need at least 2 benchmark groups for significance testing")
