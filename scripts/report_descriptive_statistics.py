import pandas as pd
from src.descriptive_statistics_src import *

# Store the raw International Stroke Trial (IST) data as a pandas dataframe.
raw_data_df = pd.read_csv("data/raw/ist_corrected.csv")

# Report the central tendency measures (mean, median, mode) for each of the numerical variables.
report_central_tendency_measures(raw_data_df)
print("\n")

# Report the measures of dispersion (range, variance, standard deviation) for each of the numerical variables.
report_measures_of_dispersion(raw_data_df)
print("\n")

# Describe the distribution of the numeric columns of the passed in pandas DataFrame.
describe_distribution(raw_data_df)
print("\n")