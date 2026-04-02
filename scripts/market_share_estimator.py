#!/usr/bin/env python3
"""
Market share estimator from proxy signals.

Estimates relative market share from multiple signals (GitHub stars,
npm downloads, Stack Overflow questions, job postings). Normalizes and weights
signals to produce market position estimates.

Input: Technology names with metric values
Output: Market share estimates and ranking
"""

import pandas as pd
import numpy as np


def estimate_market_share(technologies, weights=None):
    """
    Estimate market share from proxy signals.

    Args:
        technologies: List of dicts with keys: name, github_stars, npm_downloads,
                     stackoverflow_questions, job_postings
        weights: Dict of signal weights (defaults to equal weights)

    Returns:
        DataFrame with normalized scores and market share estimates
    """
    if weights is None:
        weights = {
            'github_stars': 0.25,
            'npm_downloads': 0.30,
            'stackoverflow_questions': 0.20,
            'job_postings': 0.25
        }

    results = []
    signals = ['github_stars', 'npm_downloads', 'stackoverflow_questions',
               'job_postings']

    for signal in signals:
        values = [t[signal] for t in technologies]
        max_val = max(values) if max(values) > 0 else 1
        for t in technologies:
            t[f'{signal}_normalized'] = t[signal] / max_val

    for tech in technologies:
        weighted_score = sum(
            tech[f'{signal}_normalized'] * weights[signal]
            for signal in signals
        )
        results.append({
            'technology': tech['name'],
            'github_stars': tech['github_stars'],
            'npm_downloads': tech['npm_downloads'],
            'stackoverflow_qs': tech['stackoverflow_questions'],
            'job_postings': tech['job_postings'],
            'market_position_score': weighted_score
        })

    df = pd.DataFrame(results)
    df = df.sort_values('market_position_score', ascending=False)
    df['market_share_estimate'] = (df['market_position_score'] /
                                   df['market_position_score'].sum()) * 100
    df['rank'] = range(1, len(df) + 1)

    return df


if __name__ == "__main__":
    technologies = [
        {
            'name': 'React',
            'github_stars': 215000,
            'npm_downloads': 25000000,
            'stackoverflow_questions': 380000,
            'job_postings': 45000
        },
        {
            'name': 'Vue',
            'github_stars': 207000,
            'npm_downloads': 8000000,
            'stackoverflow_questions': 200000,
            'job_postings': 12000
        },
        {
            'name': 'Angular',
            'github_stars': 95000,
            'npm_downloads': 3500000,
            'stackoverflow_questions': 280000,
            'job_postings': 18000
        },
        {
            'name': 'Svelte',
            'github_stars': 78000,
            'npm_downloads': 500000,
            'stackoverflow_questions': 8000,
            'job_postings': 1500
        }
    ]

    market_df = estimate_market_share(technologies)

    print("Technology Market Share Estimation")
    print("="*70)
    print(market_df[['rank', 'technology', 'market_position_score',
                     'market_share_estimate']].to_string(index=False))
    print("\nDetailed Metrics:")
    print(market_df[['technology', 'github_stars', 'npm_downloads',
                     'stackoverflow_qs', 'job_postings']].to_string(index=False))
