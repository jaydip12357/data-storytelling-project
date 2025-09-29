import pandas as pd
from src.variable_relationships_src import *

# Store the general_patients_stats.csv data as a pandas DataFrame.
general_patients_stats = pd.read_csv("data/cleaned/general_patients_stats.csv", low_memory=False)
general_patients_corr_matrix = get_corr_matrix(general_patients_stats)

# Store the patients_alive_both_times_stats.csv data as a pandas DataFrame.
patients_alive_both_times_stats = pd.read_csv("data/cleaned/patients_alive_both_times_stats.csv", low_memory=False)
patients_alive_both_times_corr_matrix = get_corr_matrix(patients_alive_both_times_stats)

# Store the patients_dead_first_time_stats.csv data as a pandas DataFrame.
patients_dead_first_time_stats = pd.read_csv("data/cleaned/patients_dead_first_time_stats.csv", low_memory=False)
patients_dead_first_time_stats_corr_matrix = get_corr_matrix(patients_dead_first_time_stats)

# Store the patients_dead_second_time_stats.csv data as a pandas DataFrame.
patients_dead_second_time_stats = pd.read_csv("data/cleaned/patients_dead_second_time_stats.csv", low_memory=False)
patients_dead_second_time_stats_corr_matrix = get_corr_matrix(patients_dead_second_time_stats)