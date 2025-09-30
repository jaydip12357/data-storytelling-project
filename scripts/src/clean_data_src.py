import pandas as pd

def report_cols_with_missing_vals(df):
    """Report the columns with missing values along with their corresponding counts of missing values."""
    print("Columns With Missing Values:")
    print(df.isnull().sum()[df.isnull().sum() > 0].to_string())

def get_cols_with_low_missing_vals(df, threshold):
    """Get the columns of the DataFrame whose numbers of missing values are less than threshold% of the total sample size."""
    return df.isnull().sum()[df.isnull().sum() < threshold*df.shape[0]].index

def get_cols_with_high_missing_vals(df, threshold):
    """Get the columns of the DataFrame whose numbers of missing values are greater than threshold% of the total sample size."""
    return df.isnull().sum()[df.isnull().sum() > threshold*df.shape[0]].index

def print_dimensions(df):
    """Print the dimensions of the passed in pandas DataFrame."""
    print("Dimensions:")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

def clean_rows(df, row_threshold=0.05):
    """
    Keep removing rows until there are no columns whose numbers of missing values are less than row_threshold% of the 
    total sample size.
    """
    rows_cleaned_df = df
    while True:
        rows_to_remove = get_cols_with_low_missing_vals(rows_cleaned_df, threshold=row_threshold)

        rows_cleaned_df_candid = rows_cleaned_df.dropna(subset=rows_to_remove)

        # If no extra rows were removed, exit. Otherwise, alter the raw data DataFrame.
        if rows_cleaned_df.shape[0] == rows_cleaned_df_candid.shape[0]:
            return rows_cleaned_df
        else:
            rows_cleaned_df = rows_cleaned_df_candid

def clean_cols(df, col_threshold=0.20):
    """Remove columns whose has greater than col_threshold% missingness."""
    cols_to_remove = get_cols_with_high_missing_vals(df, col_threshold)
    cols_cleaned_df = df.drop(columns=cols_to_remove)
    return cols_cleaned_df

def clean_df(df, df_name, row_threshold=0.10, col_threshold=0.20):
    # Print the columns with missing values for the initial data DataFrame
    print(df_name + " Data Missing Columns")
    report_cols_with_missing_vals(df)

    # Keep removing rows until there are no columns whose numbers of missing values are less than row_threshold% of the total sample size.
    rows_cleaned_df = clean_rows(df, row_threshold)

    # Print the columns with missing values for this rows-cleaned version of the DataFrame along with its dimensions.
    print(df_name + " Data Missing Columns (Post Row Cleaning)")
    report_cols_with_missing_vals(rows_cleaned_df)
    print_dimensions(rows_cleaned_df)

    # Remove columns whose has greater than col_threshold% missingness.
    cols_cleaned_df = clean_cols(rows_cleaned_df, col_threshold)

    # Print the columns with missing values for this columns-cleaned version of the rows-cleaned DataFrame along with its dimensions.
    print(df_name + " Data Missing Columns (Post Column Cleaning)")
    report_cols_with_missing_vals(cols_cleaned_df)
    print_dimensions(cols_cleaned_df)

    print("Data Cleaning Complete!")
    
    return cols_cleaned_df

def retrieve_general_patient_stats(raw_data_df):
    """Return a fully cleaned version of the raw data DataFrame (which will effectively serve as the general patient stats)."""
    return clean_df(raw_data_df, "General Patients Stats")

def retrieve_patients_alive_both_times_stats(raw_data_df):
    """
    Get a DataFrame with statistics specific to patients who were alive during both the first outcome assessment point 
    and the second outcome assessment point and save it as a csv.
    """
    patients_alive_both_times_stats = raw_data_df[(raw_data_df["DALIVE"] == "Y") & (raw_data_df["FDEAD"] == "N")] # Masking logic taken from ChatGPT 5 on 9/29/25 at 3:27 pm
    return clean_df(patients_alive_both_times_stats, "Patients Alive Both Times Stats")

def retrieve_patients_dead_first_time_stats(raw_data_df):
    """
    Get a DataFrame with statistics specific to patients who died during the first outcome assessment point 
    and save it as a csv.
    """
    patients_dead_first_time_stats = raw_data_df[(raw_data_df["DDEAD"] == "Y")]
    return clean_df(patients_dead_first_time_stats, "Patients Dead After First Time Stats")

def retrieve_patients_dead_second_time_stats(raw_data_df):
    """
    Get a DataFrame with statistics specific to patients who were alive during the first outcome assessment point, but died
    during the second outcome assessment point and save it as a csv.
    """
    patients_dead_second_time_stats = raw_data_df[(raw_data_df["DALIVE"] == "Y") & (raw_data_df["FDEAD"] == "Y")] # Modified version of masking logic taken from ChatGPT 5 on 9/29/25 at 3:27 pm
    return clean_df(patients_dead_second_time_stats, "Patients Dead Only After Second Time")