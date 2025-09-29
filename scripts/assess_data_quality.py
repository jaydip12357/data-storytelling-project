import pandas as pd
from src.data_quality_src import *

# Store the raw International Stroke Trial (IST) data as a pandas dataframe.
raw_data_df = pd.read_csv("data/raw/ist_corrected.csv", low_memory=False)

# Detect outliers/extreme values.
detect_outliers_extreme_vals(raw_data_df)
print("\n")

# Detect duplicated rows.
detect_duplicated_rows(raw_data_df)
print("\n")