import pandas as pd
import re

file_path = "Serve.xlsx"
df = pd.read_excel(file_path)

df_cleaned = df.dropna(axis=1, how='all')
df_cleaned = df_cleaned.drop(columns=['Unnamed: 10'])


def clean_amount(amount_series):

    def is_valid_amount(x):
        if pd.isna(x):
            return None
        x = re.sub(r'[^0-9.]', '.', str(x))
        try:
            return float(x) if float(x) > 0 else None
        except ValueError:
            return None
    amount_series = amount_series.apply(is_valid_amount)
    return amount_series.astype(float)


def clean_gender(gender_series):
    gender_series = gender_series.astype(str).str.lower()

    gender_series = gender_series.replace(
        to_replace=r'\bm.*', value="Male", regex=True
    )
    gender_series = gender_series.replace(
        to_replace=r'\bf.*', value="Female", regex=True
    )

    return gender_series.astype(str)


def clean_smoker(smoker_series):
    smoker_series = smoker_series.astype(str).str.lower()

    smoker_series = smoker_series.replace(
        to_replace=r'\bn.*', value="No", regex=True
    )
    smoker_series = smoker_series.replace(
        to_replace=r'\by.*', value="Yes", regex=True
    )
    # Calculating the mode of Gender column and replacing the invalid values with the mode
    mode_value = smoker_series[smoker_series.isin(['Yes', 'No'])].mode()[0]
    print(f"Mode value for Smoke col: {mode_value}")

    def assign_mode(x):
        if x in ['Yes', 'No']:
            return x
        return mode_value

    smoker_series = smoker_series.apply(assign_mode)
    return smoker_series.astype(str)


def clean_day(day_series):
    day_series = day_series.astype(str).str.lower()

    day_series = day_series.replace(
        to_replace=r'\bthu.*', value="Thursday", regex=True
    )
    day_series = day_series.replace(
        to_replace=r'\bfri.*', value="Friday", regex=True
    )
    day_series = day_series.replace(
        to_replace=r'\bsat.*', value="Saturday", regex=True
    )
    day_series = day_series.replace(
        to_replace=r'\bsun.*', value="Sunday", regex=True
    )
    # Calculating the mode of Day column and replacing the invalid values with the mode
    mode_value = day_series[day_series.isin(
        ['Thursday', 'Friday', 'Saturday', 'Sunday'])].mode()[0]
    print(f"Mode value for Day col: {mode_value}")

    def assign_mode(x):
        if x in ['Thursday', 'Friday', 'Saturday', 'Sunday']:
            return x
        return mode_value

    day_series = day_series.apply(assign_mode)

    return day_series.astype(str)


def clean_time(time_series):
    time_series = time_series.astype(str).str.lower()

    time_series = time_series.replace(
        to_replace=r'\b.*l.*', value="Lunch", regex=True
    )
    time_series = time_series.replace(
        to_replace=r'\b.*d.*', value="Dinner", regex=True
    )
    # Calculating the mode of Time column and replacing the invalid values with the mode
    mode_value = time_series[time_series.isin(
        ['Lunch', 'Dinner'])].mode()[0]
    print(f"Mode value for Time col: {mode_value}")

    def assign_mode(x):
        if x in ['Lunch', 'Dinner']:
            return x
        return mode_value

    time_series = time_series.apply(assign_mode)

    return time_series.astype(str)


def clean_partysize(df):
    # Defining abnormal values: null, zero, negative, or decimal Partysize
    abnormal_mask = (df['Partysize'].isnull()) | (
        df['Partysize'] <= 0) | (df['Partysize'] % 1 != 0)

    # Get valid rows
    valid_data = df.loc[~abnormal_mask]

    # Get the average ratio of Amount to Partysize
    valid_data['Ratio'] = valid_data['Amount'] / valid_data['Partysize']
    avg_ratio = valid_data['Ratio'].mean()

    # Strategy to fill abnormal values
    # For abnormal rows, calculate the estimated Partysize using the avg_ratio
    df.loc[abnormal_mask, 'Partysize'] = (
        df.loc[abnormal_mask, 'Amount'] / avg_ratio).round()

    df['Partysize'] = df['Partysize'].astype(int)

    return df


# Clean the Amount column
df_cleaned['Amount'] = clean_amount(df_cleaned['Amount'])
df_cleaned = df_cleaned.dropna(subset=['Amount'])
# Clean the Gender column
df_cleaned['Gender'] = clean_gender(df_cleaned['Gender'])
# Clean the Smoker column
df_cleaned['Smoker'] = clean_smoker(df_cleaned['Smoker'])
# Clean the Day column
df_cleaned['Day'] = clean_day(df_cleaned['Day'])
# Clean the Time column
df_cleaned['Time'] = clean_time(df_cleaned['Time'])
# Clean the Partysize column
df_cleaned = clean_partysize(df_cleaned)
# Calculate the number of rows removed
rows_removed = len(df) - len(df_cleaned)
# print(df_cleaned.head(20))
print(df_cleaned.iloc[170:180])
print(f"Rows removed: {rows_removed}")

output_file_path = "Serve_Cleaned.xlsx"
df_cleaned.to_excel(output_file_path, index=False)
print(f"Cleaned data saved to: {output_file_path}")
