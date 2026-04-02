#!/usr/bin/env python3
"""
Scaling simulator for metrics vs. parameters.

Models how a metric (latency, cost, throughput) scales with a parameter
(dataset size, user count, request rate). Supports linear, logarithmic, and
polynomial scaling. Fits to provided data and projects to target scale.

Input: Data points mapping parameter values to metric values, target parameter
Output: Fitted model and projection to target scale
"""

import numpy as np
try:
    from scipy.optimize import curve_fit
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
import pandas as pd


def linear_model(x, a, b):
    return a * x + b


def logarithmic_model(x, a, b):
    return a * np.log(x) + b


def polynomial_model(x, a, b, c):
    return a * x**2 + b * x + c


def fit_and_project(parameter_values, metric_values, target_parameter,
                    model_type='linear'):
    """
    Fit a scaling model and project to target parameter value.

    Args:
        parameter_values: Array of parameter values (e.g., dataset size)
        metric_values: Array of corresponding metric values (e.g., latency)
        target_parameter: Parameter value to project to
        model_type: 'linear', 'logarithmic', or 'polynomial'

    Returns:
        Dict with fitted parameters, R-squared, and projections
    """
    x = np.array(parameter_values)
    y = np.array(metric_values)

    if model_type == 'linear':
        popt, _ = curve_fit(linear_model, x, y)
        y_pred = linear_model(x, *popt)
        target_pred = linear_model(target_parameter, *popt)
        params_dict = {'a': popt[0], 'b': popt[1]}

    elif model_type == 'logarithmic':
        popt, _ = curve_fit(logarithmic_model, x, y)
        y_pred = logarithmic_model(x, *popt)
        target_pred = logarithmic_model(target_parameter, *popt)
        params_dict = {'a': popt[0], 'b': popt[1]}

    elif model_type == 'polynomial':
        popt, _ = curve_fit(polynomial_model, x, y)
        y_pred = polynomial_model(x, *popt)
        target_pred = polynomial_model(target_parameter, *popt)
        params_dict = {'a': popt[0], 'b': popt[1], 'c': popt[2]}

    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    # Clamp projections to non-negative values since metrics like latency,
    # cost, and throughput cannot be negative. Polynomial extrapolation can
    # produce negative values outside the fitted range.
    target_pred_clamped = max(0.0, float(target_pred))
    if target_pred < 0:
        import warnings
        warnings.warn(
            f"{model_type} model projects a negative value ({target_pred:.2f}) "
            f"at target={target_parameter}. Clamped to 0. Consider using a "
            f"different model or a narrower extrapolation range."
        )

    current = metric_values[-1]
    growth_factor = target_pred_clamped / current if current != 0 else float('inf')

    return {
        'model_type': model_type,
        'parameters': params_dict,
        'r_squared': r_squared,
        'current_metric': current,
        'target_metric': target_pred_clamped,
        'growth_factor': growth_factor,
        'extrapolation_warning': target_pred < 0
    }


if __name__ == "__main__":
    dataset_sizes = [100, 500, 1000, 5000, 10000, 50000]
    latencies = [25, 35, 42, 65, 82, 150]

    target_size = 100000

    results = {}
    for model in ['linear', 'logarithmic', 'polynomial']:
        results[model] = fit_and_project(dataset_sizes, latencies,
                                        target_size, model)

    print("Scaling Simulation: Latency vs Dataset Size")
    print("="*60)
    print("Current data range: {} to {} records".format(
        dataset_sizes[0], dataset_sizes[-1]))
    print("Current latency: {} to {} ms".format(latencies[0], latencies[-1]))
    print("Target dataset size: {} records".format(target_size))
    print("\n" + "="*60)

    for model_type, result in results.items():
        print("\n{} Model".format(model_type.capitalize()))
        print("-"*60)
        print("R-squared (fit quality): {:.4f}".format(result['r_squared']))
        print("Projected latency at target size: {:.1f} ms".format(
            result['target_metric']))
        print("Expected growth factor: {:.2f}x".format(result['growth_factor']))
        if result.get('extrapolation_warning'):
            print("WARNING: Model produced negative projection (clamped to 0)."
                  " Consider a different model type.")
