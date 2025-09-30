import pandas as pd
import matplotlib.pyplot as plt
import os  # Generated at 9/30/25 9:37 am by ChatGPT 5

# Generated at 9/30/25 9:37 am by ChatGPT 5
# Create output directory (new subfolder under data/visualizations)
_base_dir = os.path.join("data", "visualizations")  # Generated at 9/30/25 9:37 am by ChatGPT 5
_output_dir = os.path.join(_base_dir, "run_2025-09-30_0937am")  # Generated at 9/30/25 9:37 am by ChatGPT 5
os.makedirs(_output_dir, exist_ok=True)  # Generated at 9/30/25 9:37 am by ChatGPT 5

"""
After running variable_relationships.py, it appears that the top 6 most important features
in terms of whether a patient remains alive or dead are AGE, ONDRUG, DASPLT, HOSPNUM, 
RDELAY, and RSBP.

Therefore, we find it best to analyze these variables among the three different groups of patients:
1) Patients who remained alive, 2) Patients who died at the first assessment outcome point, and 3) Patients
who were alive at the first assessment outcome point, but were dead at the second assessment outcome point.
"""

# Load the cleaned datasets.
patients_alive_both_times_stats_encoded = pd.read_csv("data/transformed/patients_alive_both_times_stats_encoded.csv", low_memory=False)
patients_dead_first_time_stats_encoded = pd.read_csv("data/transformed/patients_dead_first_time_stats_encoded.csv", low_memory=False)
patients_dead_second_time_stats_encoded = pd.read_csv("data/transformed/patients_dead_second_time_stats_encoded.csv", low_memory=False)

# Plot the age distributions as histograms.
fig, ax = plt.subplots()
patients_alive_both_times_stats_encoded["AGE"].plot.hist()
ax.set_title("AGE Distribution - AliveBoth")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Age (years)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "AGE_AliveBoth.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_first_time_stats_encoded["AGE"].plot.hist()
ax.set_title("AGE Distribution - DeadFirst")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Age (years)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "AGE_DeadFirst.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_second_time_stats_encoded["AGE"].plot.hist()
ax.set_title("AGE Distribution - DeadSecond")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Age (years)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "AGE_DeadSecond.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

# Plot the trial treatment period distributions as histograms.
fig, ax = plt.subplots()
patients_alive_both_times_stats_encoded["ONDRUG"].plot.hist()
ax.set_title("ONDRUG Distribution - AliveBoth")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("On Drug (0/1)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "ONDRUG_AliveBoth.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_first_time_stats_encoded["ONDRUG"].plot.hist()
ax.set_title("ONDRUG Distribution - DeadFirst")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("On Drug (0/1)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "ONDRUG_DeadFirst.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_second_time_stats_encoded["ONDRUG"].plot.hist()
ax.set_title("ONDRUG Distribution - DeadSecond")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("On Drug (0/1)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "ONDRUG_DeadSecond.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

# Plot the percentages of patients who were discharged on long term aspirin as pie charts.
fig, ax = plt.subplots()
patients_alive_both_times_stats_encoded["DASPLT_Y"].plot.pie()
ax.set_title("DASPLT_Y Proportions - AliveBoth")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "DASPLT_Y_AliveBoth.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_first_time_stats_encoded["DASPLT_Y"].plot.pie()
ax.set_title("DASPLT_Y Proportions - DeadFirst")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "DASPLT_Y_DeadFirst.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_second_time_stats_encoded["DASPLT_Y"].plot.pie()
ax.set_title("DASPLT_Y Proportions - DeadSecond")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "DASPLT_Y_DeadSecond.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

# Plot the percentages of patients who were at different hospitals as pie charts.
fig, ax = plt.subplots()
patients_alive_both_times_stats_encoded["HOSPNUM"].plot.pie()
ax.set_title("HOSPNUM Proportions - AliveBoth")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "HOSPNUM_AliveBoth.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_first_time_stats_encoded["HOSPNUM"].plot.pie()
ax.set_title("HOSPNUM Proportions - DeadFirst")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "HOSPNUM_DeadFirst.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_second_time_stats_encoded["HOSPNUM"].plot.pie()
ax.set_title("HOSPNUM Proportions - DeadSecond")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "HOSPNUM_DeadSecond.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

# Plot the delay between stroke and randomisation distributions as histograms.
fig, ax = plt.subplots()
patients_alive_both_times_stats_encoded["RDELAY"].plot.hist()
ax.set_title("RDELAY Distribution - AliveBoth")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Delay (days)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "RDELAY_AliveBoth.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_first_time_stats_encoded["RDELAY"].plot.hist()
ax.set_title("RDELAY Distribution - DeadFirst")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Delay (days)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "RDELAY_DeadFirst.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_second_time_stats_encoded["RDELAY"].plot.hist()
ax.set_title("RDELAY Distribution - DeadSecond")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Delay (days)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "RDELAY_DeadSecond.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

# Plot the systolic blood pressure at randomisation (mmHg) distributions as histograms.
fig, ax = plt.subplots()
patients_alive_both_times_stats_encoded["RSBP"].plot.hist()
ax.set_title("RSBP Distribution - AliveBoth")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Systolic BP (mmHg)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "RSBP_AliveBoth.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_first_time_stats_encoded["RSBP"].plot.hist()
ax.set_title("RSBP Distribution - DeadFirst")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Systolic BP (mmHg)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "RSBP_DeadFirst.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5

fig, ax = plt.subplots()
patients_dead_second_time_stats_encoded["RSBP"].plot.hist()
ax.set_title("RSBP Distribution - DeadSecond")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_xlabel("Systolic BP (mmHg)")  # Generated at 9/30/25 9:37 am by ChatGPT 5
ax.set_ylabel("Count")  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.tight_layout()  # Generated at 9/30/25 9:37 am by ChatGPT 5
fig.savefig(os.path.join(_output_dir, "RSBP_DeadSecond.png"))  # Generated at 9/30/25 9:37 am by ChatGPT 5