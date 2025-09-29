"""
Author: Ethan Dominic
"""

import pandas as pd
from src.data_structure_src import *

# Store the raw International Stroke Trial (IST) data as a pandas dataframe.
raw_data_df = pd.read_csv("data/raw/ist_corrected.csv")

# Print the dimensions of the raw IST data.
print_dimensions(raw_data_df)
print("\n")

# Report the different data types that exist in the IST data.
report_data_types(raw_data_df)
print("\n")

# Report the columns with missing values along with their corresponding counts of missing values.
report_cols_with_missing_vals(raw_data_df)
print("\n")