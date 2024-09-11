import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the cleaned dataset
file_path = "Serve_Cleaned.xlsx"
df_cleaned = pd.read_excel(file_path)

# Set Seaborn aesthetic styles for the plots
sns.set(style="whitegrid")

# Helper function for saving plots


def save_plot(fig, title):
    fig.savefig(f'{title}.png', dpi=300, bbox_inches='tight')
    plt.show()


# 1. Distribution of Total Amount (Revenue)
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Amount'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Total Bill Amount')
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
save_plot(plt, 'Amount_Distribution')

# 2. Boxplot of Tips by Day to analyze tipping trends across different days
plt.figure(figsize=(10, 6))
sns.boxplot(x='Day', y='Tip', data=df_cleaned, palette="coolwarm")
plt.title('Tipping Trends Across Days')
plt.xlabel('Day of the Week')
plt.ylabel('Tip Amount ($)')
save_plot(plt, 'Tips_By_Day')

# 3. Boxplot of Tips by Time (Lunch vs Dinner) to check if time affects tipping
plt.figure(figsize=(8, 6))
sns.boxplot(x='Time', y='Tip', data=df_cleaned, palette="viridis")
plt.title('Tipping Behavior at Lunch vs Dinner')
plt.xlabel('Time of Day')
plt.ylabel('Tip Amount ($)')
save_plot(plt, 'Tips_By_Time')

# 4. Heatmap to show the correlation between numeric variables
plt.figure(figsize=(8, 6))
corr = df_cleaned[['Amount', 'Tip', 'Partysize']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, linewidths=.5)
plt.title('Correlation Between Amount, Tip, and Partysize')
save_plot(plt, 'Correlation_Heatmap')

# 5. Boxplot of Amount by Waiter's Gender to observe if the waiter's gender impacts spending behavior
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Amount', data=df_cleaned, palette="pastel")
plt.title('Spending Behavior by Waiter\'s Gender')
plt.xlabel('Waiter\'s Gender')
plt.ylabel('Amount Spent ($)')
save_plot(plt, 'Spending_By_Waiter_Gender')

# 6. Bar Plot of Total Revenue by Day (Revenue Trends Across Days)
revenue_by_day = df_cleaned.groupby('Day')['Amount'].sum().sort_index()
plt.figure(figsize=(8, 6))
sns.barplot(x=revenue_by_day.index, y=revenue_by_day.values, palette="rocket")
plt.title('Total Revenue by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Revenue ($)')
save_plot(plt, 'Revenue_By_Day')

# 7. Scatter plot of Amount vs. Partysize to observe the relationship between party size and spending
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Partysize', y='Amount', data=df_cleaned,
                hue='Gender', palette="Set1", s=100, alpha=0.7)
plt.title(
    'Relationship Between Partysize and Amount Spent (Colored by Waiter\'s Gender)')
plt.xlabel('Partysize')
plt.ylabel('Amount Spent ($)')
save_plot(plt, 'Amount_vs_Partysize')

# 8. Percentage of Smokers and Non-Smokers (Pie Chart)
smoker_counts = df_cleaned['Smoker'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(smoker_counts, labels=smoker_counts.index, autopct='%1.1f%%',
        startangle=90, colors=["#ff9999", "#66b3ff"])
plt.title('Percentage of Smokers vs Non-Smokers')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
save_plot(plt, 'Smokers_vs_Non_Smokers')

# 9. Bar Plot of Average Tip by Waiter's Gender to analyze gender-based tipping differences
avg_tip_by_gender = df_cleaned.groupby('Gender')['Tip'].mean()
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_tip_by_gender.index,
            y=avg_tip_by_gender.values, palette="cool")
plt.title('Average Tip by Waiter\'s Gender')
plt.xlabel('Waiter\'s Gender')
plt.ylabel('Average Tip ($)')
save_plot(plt, 'Average_Tip_By_Waiter_Gender')
