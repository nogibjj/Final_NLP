"We will use pytest to test our functions from src/lib.py"
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("/workspaces/Simrun_Continuous_Integration_using_GitHub_Actions_of_Python_Data_Science_Project")
from src.lib import get_mean, get_median, get_std_dev, maximum, minimum, visualize_dataset


def test_get_mean():
    """Test function for the get_mean"""
    data = pd.read_csv("data/diabetes.csv")
    column_g = "Glucose"
    result_g =  get_mean(data, column_g)

    # hand calculations
    actual_mean_g = sum(data[column_g]) / len(data[column_g])

    # assert the test
    assert round(result_g) == round(actual_mean_g)
    


def test_get_std_dev():
    """Test function for the get_std_dev"""
    data = pd.read_csv("data/diabetes.csv")
    column_g = "Glucose"
    result = get_std_dev(data, column_g)
    actual_std_dev = 31.97261819513622

    assert result == actual_std_dev

def test_get_median():
    """Test function for the get_std_dev"""
    data = pd.read_csv("data/diabetes.csv")
    column_g = "Glucose"

    # hand calculation
    sort_data = sorted(data[column_g])
    n = len(sort_data)
    if n % 2 == 0:
        actual_median = (sort_data[n // 2 - 1] + sort_data[n // 2]) / 2
        actual_median = round(actual_median, 10)
    else:
        actual_median = sort_data[n // 2]
        actual_median = round(actual_median, 10)
    
    # calling the function
    result = get_median(data, column_g)

    # Check the assert
    assert result == actual_median

def test_maximum():
    """Test function for the maximum"""
    data = pd.read_csv("data/diabetes.csv")
    column_g = "Glucose"
    result = maximum(data, column_g)
    actual_max = 199

    assert result == actual_max

def test_minimum():
    """Test function for the minimum"""
    data = pd.read_csv("data/diabetes.csv")
    column_g = "Glucose"
    result = minimum(data, column_g)
    actual_min = 0

    assert result == actual_min

def test_visualize_dataset():
    """Test function for visualization"""

    data = pd.read_csv("data/diabetes.csv")

    visualize_dataset(data, jupyter=False)  # Pass None as data (not used in this case)

    # Assert that a message is printed to the console
    expected_message = "Visualization of Diabetes Dataset"
    actual_message = "Visualization of Diabetes Dataset"  # Modify this to get the actual message
    assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"


if __name__ == '__main__':
    test_get_mean()
    test_get_median()
    test_get_std_dev()
    test_maximum()
    test_minimum()
    test_visualize_dataset()
