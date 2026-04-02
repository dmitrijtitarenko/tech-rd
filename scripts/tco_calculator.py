#!/usr/bin/env python3
"""
Total Cost of Ownership (TCO) Calculator for cloud services.

Calculates 12-month and 36-month projections for services with pricing tiers,
compute costs, storage costs, and scaling by team size.

Input: List of services with pricing structure
Output: Pandas DataFrame with monthly and annual projections
"""

import pandas as pd
import numpy as np


def calculate_tco(services, team_size, months=12):
    """
    Calculate TCO for multiple services.

    Args:
        services: List of dicts with keys: name, tier, base_cost, compute_cost,
                  storage_cost, storage_gb, monthly_growth_rate
        team_size: Number of team members
        months: Number of months to project

    Returns:
        DataFrame with monthly costs and cumulative totals
    """
    results = []

    for month in range(1, months + 1):
        month_costs = {'month': month}
        total = 0

        for service in services:
            name = service['name']
            base = service['base_cost']
            compute = service['compute_cost'] * team_size
            storage = service['storage_cost'] * service['storage_gb']

            growth = (1 + service.get('monthly_growth_rate', 0)) ** (month - 1)
            monthly_cost = (base + compute + storage) * growth

            month_costs[name] = monthly_cost
            total += monthly_cost

        month_costs['total_monthly'] = total
        month_costs['cumulative'] = sum([r.get('total_monthly', 0)
                                         for r in results]) + total
        results.append(month_costs)

    return pd.DataFrame(results)


if __name__ == "__main__":
    services = [
        {
            'name': 'PostgreSQL (RDS)',
            'tier': 'pro',
            'base_cost': 150,
            'compute_cost': 25,
            'storage_cost': 0.1,
            'storage_gb': 500,
            'monthly_growth_rate': 0.05
        },
        {
            'name': 'MongoDB Atlas',
            'tier': 'enterprise',
            'base_cost': 200,
            'compute_cost': 40,
            'storage_cost': 0.15,
            'storage_gb': 1000,
            'monthly_growth_rate': 0.08
        },
        {
            'name': 'DynamoDB',
            'tier': 'pro',
            'base_cost': 100,
            'compute_cost': 30,
            'storage_cost': 0.25,
            'storage_gb': 200,
            'monthly_growth_rate': 0.03
        }
    ]

    team_size = 8
    df_12 = calculate_tco(services, team_size, months=12)
    df_36 = calculate_tco(services, team_size, months=36)

    print("12-Month TCO Projection (Team Size: {})".format(team_size))
    print(df_12.tail(3).to_string(index=False))
    print("\nTotal 12-month cost: ${:.2f}".format(df_12['cumulative'].iloc[-1]))
    print("\nTotal 36-month cost: ${:.2f}".format(df_36['cumulative'].iloc[-1]))
