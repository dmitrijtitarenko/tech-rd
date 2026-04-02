#!/usr/bin/env python3
"""
Risk assessment calculator.

Evaluates risks with likelihood (1-5) and impact (1-5) scores.
Computes composite scores, categorizes risk levels, and calculates portfolio risk.

Input: List of risks with likelihood and impact scores
Output: Risk categorization and aggregate portfolio metrics
"""

import pandas as pd
import numpy as np


def assess_risks(risks):
    """
    Calculate risk scores and portfolio metrics.

    Args:
        risks: List of dicts with keys: name, likelihood (1-5), impact (1-5),
               mitigation_effort (optional, 1-5)

    Returns:
        Tuple of (risks_df, portfolio_summary_dict)
    """
    results = []

    for risk in risks:
        name = risk['name']
        likelihood = risk['likelihood']
        impact = risk['impact']
        score = likelihood * impact

        if score >= 16:
            category = 'High'
        elif score >= 9:
            category = 'Medium'
        else:
            category = 'Low'

        mitigation = risk.get('mitigation_effort', 3)
        priority = score / mitigation

        results.append({
            'risk': name,
            'likelihood': likelihood,
            'impact': impact,
            'score': score,
            'category': category,
            'mitigation_effort': mitigation,
            'priority_index': priority
        })

    df = pd.DataFrame(results)
    df = df.sort_values('score', ascending=False)

    portfolio = {
        'total_risks': len(df),
        'high_risks': len(df[df['category'] == 'High']),
        'medium_risks': len(df[df['category'] == 'Medium']),
        'low_risks': len(df[df['category'] == 'Low']),
        'avg_score': df['score'].mean(),
        'max_score': df['score'].max(),
        'portfolio_risk_index': df['score'].sum() / len(df)
    }

    return df, portfolio


if __name__ == "__main__":
    risks = [
        {'name': 'Database scalability limits', 'likelihood': 4, 'impact': 5,
         'mitigation_effort': 4},
        {'name': 'Key person dependency', 'likelihood': 3, 'impact': 4,
         'mitigation_effort': 3},
        {'name': 'Third-party API outage', 'likelihood': 2, 'impact': 3,
         'mitigation_effort': 2},
        {'name': 'Security vulnerability in dependencies', 'likelihood': 3,
         'impact': 5, 'mitigation_effort': 2},
        {'name': 'Market adoption slower than projected', 'likelihood': 4,
         'impact': 4, 'mitigation_effort': 1}
    ]

    risk_df, portfolio = assess_risks(risks)

    print("Risk Assessment Report")
    print("="*70)
    print(risk_df[['risk', 'likelihood', 'impact', 'score', 'category',
                   'priority_index']].to_string(index=False))
    print("\n" + "="*70)
    print("Portfolio Summary")
    print("-"*70)
    print("Total risks identified: {}".format(portfolio['total_risks']))
    print("High-risk items: {}".format(portfolio['high_risks']))
    print("Medium-risk items: {}".format(portfolio['medium_risks']))
    print("Low-risk items: {}".format(portfolio['low_risks']))
    print("Average risk score: {:.1f}".format(portfolio['avg_score']))
    print("Portfolio risk index: {:.1f}".format(portfolio['portfolio_risk_index']))
