from scipy import stats
import pandas as pd

df_cleaned = pd.read_excel('Serve_Cleaned.xlsx')
print("Descriptive Statistics:\n")
print(df_cleaned.describe().to_markdown(numalign="left", stralign="left"))
# Separate data by waiter gender
tips_male = df_cleaned[df_cleaned['Gender'] == 'Male']['Tip']
tips_female = df_cleaned[df_cleaned['Gender'] == 'Female']['Tip']

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(tips_male, tips_female, nan_policy='omit')
print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference in tip amounts based on waiter gender.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in tip amounts based on waiter gender.")

# Separate data by time (Lunch vs Dinner)
amount_lunch = df_cleaned[df_cleaned['Time'] == 'Lunch']['Amount']
amount_dinner = df_cleaned[df_cleaned['Time'] == 'Dinner']['Amount']

# Perform t-test
t_stat, p_value = stats.ttest_ind(
    amount_dinner, amount_lunch, nan_policy='omit')
print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: Customers spend more at dinner than lunch.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between lunch and dinner spending.")

# Separate data by smoker status
tips_smoker = df_cleaned[df_cleaned['Smoker'] == 'Yes']['Tip']
tips_non_smoker = df_cleaned[df_cleaned['Smoker'] == 'No']['Tip']

# Perform t-test
t_stat, p_value = stats.ttest_ind(
    tips_smoker, tips_non_smoker, nan_policy='omit')
print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: Smokers tip more than non-smokers.")
else:
    print("Fail to reject the null hypothesis: Smoking status does not significantly impact tipping.")

# separate data by Thursday and Saturday
amount_thursday = df_cleaned[df_cleaned['Day'] == 'Thursday']['Amount']
amount_saturday = df_cleaned[df_cleaned['Day'] == 'Saturday']['Amount']

# Perform t-test
t_stat, p_value = stats.ttest_ind(
    amount_saturday, amount_thursday, nan_policy='omit')
print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: Customers spend more on Saturday than Thursday.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in spending between Thursday and Saturday.")

# separate data by party size
amount_party2 = df_cleaned[df_cleaned['Partysize'] == 2]['Amount']
amount_party3 = df_cleaned[df_cleaned['Partysize'] == 3]['Amount']

# Perform t-test
t_stat, p_value = stats.ttest_ind(
    amount_party2, amount_party3, nan_policy='omit')

print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: Customers in parties of 2 spend more than parties of 3.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in spending between parties of 2 and 3.")

# Separate data by lunch and dinner on tip
tips_lunch = df_cleaned[df_cleaned['Time'] == 'Lunch']['Tip']
tips_dinner = df_cleaned[df_cleaned['Time'] == 'Dinner']['Tip']

# Perform t-test
t_stat, p_value = stats.ttest_ind(
    tips_dinner, tips_lunch, nan_policy='omit')
print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: Customers tip more at dinner than lunch.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in tipping between lunch and dinner.")

df_cleaned['Tip_Percentage'] = df_cleaned['Tip'] / df_cleaned['Amount'] * 100
# Weekends (Saturday, Sunday) vs. Weekdays
tip_weekdays = df_cleaned[df_cleaned['Day'].isin(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]['Tip_Percentage']
tip_weekends = df_cleaned[df_cleaned['Day'].isin(
    ['Saturday', 'Sunday'])]['Tip_Percentage']

t_stat, p_value = stats.ttest_ind(
    tip_weekdays, tip_weekends, nan_policy='omit')
print(f"T-test result: t-statistic = {t_stat}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference in tip percentages between weekends and weekdays.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in tip percentages between weekends and weekdays.")

# Perform Pearson correlation test
corr, p_value = stats.pearsonr(df_cleaned['Partysize'], df_cleaned['Amount'])
print(f"Correlation coefficient = {corr}, p-value = {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant positive correlation between party size and amount spent.")
else:
    print("Fail to reject the null hypothesis: There is no significant correlation between party size and amount spent.")

corr, p_value = stats.pearsonr(
    df_cleaned['Partysize'], df_cleaned['Tip_Percentage'])
print(f"Correlation coefficient = {corr}, p-value = {p_value}")
