import pandas as pd
from src.transform_data_src import *

# Store the general_patients_stats.csv data as a pandas DataFrame.
general_patients_stats = pd.read_csv("data/cleaned/general_patients_stats.csv", low_memory=False)
# One-hot encode the categorical columns and save the new DataFrame as a csv.
general_patients_stats_encoded = encode_categorical_cols(general_patients_stats)
general_patients_stats_encoded.to_csv("data/transformed/general_patients_stats_encoded.csv")

# Store the patients_alive_both_times_stats.csv data as a pandas DataFrame.
patients_alive_both_times_stats = pd.read_csv("data/cleaned/patients_alive_both_times_stats.csv", low_memory=False)
# One-hot encode the categorical columns and save the new DataFrame as a csv.
patients_alive_both_times_stats_encoded = encode_categorical_cols(patients_alive_both_times_stats)
patients_alive_both_times_stats_encoded.to_csv("data/transformed/patients_alive_both_times_stats_encoded.csv")

# Store the patients_dead_first_time_stats.csv data as a pandas DataFrame.
patients_dead_first_time_stats = pd.read_csv("data/cleaned/patients_dead_first_time_stats.csv", low_memory=False)
# One-hot encode the categorical columns and save the new DataFrame as a csv.
patients_dead_first_time_stats_encoded = encode_categorical_cols(patients_dead_first_time_stats)
patients_dead_first_time_stats_encoded.to_csv("data/transformed/patients_dead_first_time_stats_encoded.csv")

# Store the patients_dead_second_time_stats.csv data as a pandas DataFrame.
patients_dead_second_time_stats = pd.read_csv("data/cleaned/patients_dead_second_time_stats.csv", low_memory=False)
# One-hot encode the categorical columns and save the new DataFrame as a csv.
patients_dead_second_time_stats_encoded = encode_categorical_cols(patients_dead_second_time_stats)
patients_dead_second_time_stats_encoded.to_csv("data/transformed/patients_dead_second_time_stats_encoded.csv")