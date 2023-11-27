import sys
sys.path.append("/workspaces/Simrun_Continuous_Integration_using_GitHub_Actions_of_Python_Data_Science_Project")
sys.path.append("/workspaces/Simrun_Continuous_Integration_using_GitHub_Actions_of_Python_Data_Science_Project/src")
from src.python_script import run_statistics
import pandas as pd


def test_descriptive_stats():
    "Test the descriptive stats function in python script"
    data = pd.read_csv("data/diabetes.csv")
    column = "Glucose"

    results = run_statistics(data, column)
    
    assert 'Maximum' in results
    assert 'Minimum' in results
    assert 'Mean' in results
    assert 'Median' in results
    assert 'Standard Deviation' in results