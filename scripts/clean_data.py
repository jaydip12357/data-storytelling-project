import pandas as pd
from src.clean_data_src import *

# Store the raw International Stroke Trial (IST) data as a pandas dataframe.
raw_data_df = pd.read_csv("data/raw/ist_corrected.csv", low_memory=False)

# Get a DataFrame with general statistics about most of the patients and save it as a csv.
general_patient_stats = retrieve_general_patient_stats(raw_data_df)
general_patient_stats.to_csv("data/cleaned/general_patients_stats.csv")

"""
Get a DataFrame with statistics specific to patients who were alive during both the first outcome assessment point 
and the second outcome assessment point and save it as a csv.
"""
patients_alive_both_times_stats = retrieve_patients_alive_both_times_stats(raw_data_df)
patients_alive_both_times_stats.to_csv("data/cleaned/patients_alive_both_times_stats.csv")

"""
Get a DataFrame with statistics specific to patients who died during the first outcome assessment point 
and save it as a csv.
"""
patients_dead_first_time_stats = retrieve_patients_dead_first_time_stats(raw_data_df)
patients_dead_first_time_stats.to_csv("data/cleaned/patients_dead_first_time_stats.csv")

"""
Get a DataFrame with statistics specific to patients who were alive during the first outcome assessment point, but died
during the second outcome assessment point and save it as a csv.
"""
patients_dead_second_time_stats = retrieve_patients_dead_second_time_stats(raw_data_df)
patients_dead_second_time_stats.to_csv("data/cleaned/patients_dead_second_time_stats.csv")