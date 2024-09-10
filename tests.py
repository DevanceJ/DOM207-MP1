import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel('Serve_Cleaned.xlsx')


# t-test: Difference in tips based on gender
male_tips = df[df['Gender'] == 'Male']['Tip']
female_tips = df[df['Gender'] == 'Female']['Tip']

t_stat, p_value = stats.ttest_ind(male_tips, female_tips)
print(f't-statistic: {t_stat}, p-value: {p_value}')

if p_value < 0.05:
    print("Statistically significant difference in tips based on gender.")
else:
    print("No statistically significant difference in tips based on gender.")

# t-test: Difference in bill amounts based on smoker status
smoker_amounts = df[df['Smoker'] == 'Yes']['Amount']
non_smoker_amounts = df[df['Smoker'] == 'No']['Amount']

t_stat, p_value = stats.ttest_ind(smoker_amounts, non_smoker_amounts)
print(f'\nt-statistic: {t_stat}, p-value: {p_value}')

if p_value < 0.05:
    print("Statistically significant difference in bill amounts between smokers and non-smokers.")
else:
    print("No statistically significant difference in bill amounts between smokers and non-smokers.")


# t-test: Difference in bill amounts based on time of day
lunch_amounts = df[df['Time'] == 'Lunch']['Amount']
dinner_amounts = df[df['Time'] == 'Dinner']['Amount']

t_stat, p_value = stats.ttest_ind(lunch_amounts, dinner_amounts)
print(f'\nt-statistic: {t_stat}, p-value: {p_value}')

if p_value < 0.05:
    print("Statistically significant difference in bill amounts between lunch and dinner times.")
else:
    print("No statistically significant difference in bill amounts between lunch and dinner times.")

# t-test: Difference in bill amounts based on day of the week
saturday_amounts = df[df['Day'] == 'Saturday']['Amount']
sunday_amounts = df[df['Day'] == 'Thursday']['Amount']

t_stat, p_value = stats.ttest_ind(saturday_amounts, sunday_amounts)
print(f'\nt-statistic: {t_stat}, p-value: {p_value}')

if p_value < 0.05:
    print("Statistically significant difference in bill amounts between Saturday and Sunday.")
else:
    print("No statistically significant difference in bill amounts between Saturday and Sunday.")


# t-test: Difference in tips based on smoker status
smoker_tips = df[df['Smoker'] == 'Yes']['Tip']
non_smoker_tips = df[df['Smoker'] == 'No']['Tip']

t_stat, p_value = stats.ttest_ind(smoker_tips, non_smoker_tips)
print(f'\nt-statistic: {t_stat}, p-value: {p_value}')

if p_value < 0.05:
    print("Statistically significant difference in tips between smokers and non-smokers.")
else:
    print("No statistically significant difference in tips between smokers and non-smokers.")

# print("Descriptive Statistics:\n")
print(df.describe().to_markdown(numalign="left", stralign="left"))

# # Correlation matrix for numerical columns (Amount, Tip, Partysize)
# corr_matrix = df[['Amount', 'Tip', 'Partysize']].corr()
# print("\nCorrelation Matrix:\n")
# print(corr_matrix.to_markdown(numalign="left", stralign="left"))

# # Scatterplot matrix for numerical columns
# sns.pairplot(df[['Amount', 'Tip', 'Partysize']])
# plt.show()
