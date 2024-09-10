import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel('Serve_Cleaned.xlsx')

# Display first 5 rows of data
print(df.head())

# Histograms for numerical columns (Amount, Tip, Partysize)
numerical_cols = ['Amount', 'Tip', 'Partysize']
df[numerical_cols].hist(bins=10, figsize=(10, 6))
plt.tight_layout()
plt.show()
# Define numerical columns

# Bar plots for categorical columns (Gender, Smoker, Day, Time)
categorical_cols = ['Gender', 'Smoker', 'Day', 'Time']

for col in categorical_cols:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.ylabel('Count')
    plt.show()

# Scatterplot for Tip vs. Amount
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Amount', y='Tip', data=df)
plt.title('Scatterplot of Tip vs. Amount')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Smoker', y='Amount', data=df)
plt.title('Bill Amount Distribution by Smoker Status')
plt.show()
# Descriptive statistics
print(df.describe())
# Display unique values of categorical columns
for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")

# make boxplot for Amount vs. Time
plt.figure(figsize=(6, 4))
sns.boxplot(x='Time', y='Amount', data=df)
plt.title('Bill Amount Distribution by Time of Day')
plt.show()

# make boxplot for Amount vs. Day
plt.figure(figsize=(6, 4))
sns.boxplot(x='Day', y='Amount', data=df)
plt.title('Bill Amount Distribution by Day of the Week')
plt.show()
