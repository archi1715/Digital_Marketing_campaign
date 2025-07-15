import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_marketing_campaign_data.csv")

# Basic Overview
print("Total Campaigns:", df['Campaign_ID'].nunique())
print("Total Companies:", df['Company'].nunique())
print("Channels Used:", df['Channel_Used'].unique())
print("Date Range:", df['Date'].min(), "to", df['Date'].max())

# Histograms of key metrics
metrics = ['Impressions', 'Clicks', 'Estimated_Conversions', 'Acquisition_Cost', 'ROI']
df[metrics].hist(bins=30, figsize=(12, 8))
plt.tight_layout()
plt.show()

# ROI Distribution by Channel
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Channel_Used', y='ROI')
plt.title("ROI Distribution by Channel")
plt.xticks(rotation=45)
plt.show()

# Average ROI by Company
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Company', y='ROI', estimator='mean', ci=None)
plt.title("Average ROI by Company")
plt.show()

# Conversion Rate vs. Impressions
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Impressions', y='Conversion_Rate', hue='Campaign_Type')
plt.title("Conversion Rate vs. Impressions")
plt.show()

# CTR by Weekday
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Weekday', y='CTR', order=weekday_order)
plt.title("CTR by Weekday")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Impressions', 'Clicks', 'Estimated_Conversions', 'ROI', 'CTR', 'CPC']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Top 10 Campaigns by ROI
top_roi = df[['Campaign_ID', 'ROI']].sort_values(by='ROI', ascending=False).head(10)
print("Top 10 Campaigns by ROI:")
print(top_roi)