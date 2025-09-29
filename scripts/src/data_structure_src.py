import pandas as pd

def print_dimensions(df):
    """Print the dimensions of the passed in pandas DataFrame."""
    print("Dimensions:")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

def report_data_types(df):
    """Report the different data types that exist in the pandas DataFrame."""
    print("Data Types:")
    data_types = df.dtypes
    print(data_types.to_string())

def report_cols_with_missing_vals(df):
    """Report the columns with missing values along with their corresponding counts of missing values."""
    print("Columns With Missing Values:")
    print(df.isnull().sum()[df.isnull().sum() > 0].to_string())