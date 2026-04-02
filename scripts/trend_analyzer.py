#!/usr/bin/env python3
"""
Technology adoption trend analyzer.

Analyzes adoption trends over time (GitHub stars, npm downloads, job postings).
Computes growth rate, acceleration, moving average, and projects future values.

Input: Time series data (date, value pairs)
Output: Trend summary with projections
"""

import pandas as pd
import numpy as np
try:
    from scipy import stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


def analyze_trend(dates, values, projection_months=6):
    """
    Analyze adoption trend and project future values.

    Args:
        dates: List of dates or time periods
        values: List of metric values
        projection_months: Months to project forward

    Returns:
        Dict with trend metrics and projections
    """
    df = pd.DataFrame({'date': dates, 'value': values})
    df['time_idx'] = np.arange(len(df))

    df['growth_rate'] = df['value'].pct_change() * 100
    df['ma_3'] = df['value'].rolling(window=3, min_periods=1).mean()

    acceleration = df['growth_rate'].diff().mean()

    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df['time_idx'], df['value']
    )

    last_value = df['value'].iloc[-1]
    last_idx = len(df)
    future_values = [last_value * (1 + slope/100) ** i
                     for i in range(1, projection_months + 1)]

    result = {
        'latest_value': last_value,
        'avg_growth_rate': df['growth_rate'].mean(),
        'acceleration': acceleration,
        'r_squared': r_value ** 2,
        'trend_slope': slope,
        'projected_values_6mo': future_values,
        'data': df
    }

    return result


if __name__ == "__main__":
    dates = pd.date_range('2020-01', periods=24, freq='M')
    values = [100 + i**1.3 * 20 + np.random.normal(0, 10) for i in range(24)]

    trend = analyze_trend(dates, values, projection_months=6)

    print("Technology Adoption Trend Analysis")
    print("="*50)
    print("Latest value: {:.0f}".format(trend['latest_value']))
    print("Average growth rate: {:.2f}%".format(trend['avg_growth_rate']))
    print("Acceleration: {:.2f}".format(trend['acceleration']))
    print("R-squared (fit quality): {:.3f}".format(trend['r_squared']))
    print("\n6-Month Projection (exponential smoothing):")
    for i, val in enumerate(trend['projected_values_6mo'], 1):
        print("  Month {}: {:.0f}".format(i, val))
