"""This Script is used to deploy descriptive statistics
on the diabetes dataset using functions already
defined by the lib.py"""
import lib
import pandas as pd


def run_statistics(data, column):
    """Statistics for Diabetes dataset"""

    result = {
        "Maximum": lib.maximum(data, column),
        "Minimum": lib.minimum(data, column),
        "Mean": lib.get_mean(data, column),
        "Median": lib.get_median(data, column),
        "Standard Deviation": lib.get_std_dev(data, column),
    }

    return result


def run_visualizations(data, column):
    "Runs visualizations on the passed dataset"
    lib.display_statistics(data)
    lib.visualize_dataset(data, jupyter=False)


if __name__ == "__main__":
    data = pd.read_csv("data/diabetes.csv")
    column = "Glucose"
    print("run")
    results = run_statistics(data, column)
    run_visualizations(data, column)
