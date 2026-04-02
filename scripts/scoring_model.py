#!/usr/bin/env python3
"""
Weighted multi-criteria scoring model.

Evaluates options against weighted criteria, performs sensitivity analysis
to test robustness of rankings under weight variations (+/-20%).

Input: Criteria with weights, scores per option
Output: Ranked results with sensitivity analysis
"""

import pandas as pd
import numpy as np


def score_options(criteria_weights, option_scores):
    """
    Calculate weighted scores and perform sensitivity analysis.

    Args:
        criteria_weights: Dict mapping criteria names to weights (should sum to 1)
        option_scores: Dict mapping option names to dict of criteria scores

    Returns:
        Tuple of (results_df, sensitivity_analysis_df)
    """
    results = []

    for option_name, scores in option_scores.items():
        weighted_score = sum(
            scores[criterion] * criteria_weights[criterion]
            for criterion in criteria_weights
        )
        results.append({
            'option': option_name,
            'weighted_score': weighted_score,
            'rank': 0
        })

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('weighted_score', ascending=False)
    results_df['rank'] = range(1, len(results_df) + 1)

    sensitivity = []
    for criterion in criteria_weights:
        for delta in [-0.2, 0.2]:
            adjusted_weights = criteria_weights.copy()
            original = adjusted_weights[criterion]
            adjusted_weights[criterion] = max(0, original * (1 + delta))

            norm_sum = sum(adjusted_weights.values())
            adjusted_weights = {k: v/norm_sum for k, v in adjusted_weights.items()}

            for option_name, scores in option_scores.items():
                new_score = sum(
                    scores[c] * adjusted_weights[c]
                    for c in adjusted_weights
                )
                sensitivity.append({
                    'criterion': criterion,
                    'delta': delta,
                    'option': option_name,
                    'score': new_score
                })

    sensitivity_df = pd.DataFrame(sensitivity)
    return results_df, sensitivity_df


if __name__ == "__main__":
    criteria_weights = {
        'scalability': 0.30,
        'cost': 0.25,
        'ease_of_use': 0.20,
        'security': 0.15,
        'community': 0.10
    }

    option_scores = {
        'Solution A': {'scalability': 8, 'cost': 7, 'ease_of_use': 9,
                       'security': 8, 'community': 7},
        'Solution B': {'scalability': 9, 'cost': 5, 'ease_of_use': 7,
                       'security': 9, 'community': 8},
        'Solution C': {'scalability': 7, 'cost': 9, 'ease_of_use': 8,
                       'security': 7, 'community': 6}
    }

    results, sensitivity = score_options(criteria_weights, option_scores)

    print("Multi-Criteria Scoring Model Results")
    print("="*50)
    print(results[['option', 'weighted_score', 'rank']].to_string(index=False))
    print("\nSensitivity Analysis (weight changes of +/-20%)")
    print("-"*50)
    print("Showing variance in scores when individual weights change:")
    for option in results['option']:
        sens_subset = sensitivity[sensitivity['option'] == option]
        score_range = (sens_subset['score'].min(), sens_subset['score'].max())
        print("  {}: {:.2f} - {:.2f}".format(option, score_range[0], score_range[1]))
