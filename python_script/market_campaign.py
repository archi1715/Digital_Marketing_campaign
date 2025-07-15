# Step 1: Import Required Libraries
import pandas as pd
import numpy as np

# Step 2: Load Dataset
df = pd.read_csv("marketing_campaign_dataset.csv")
print("Shape:", df.shape)
print(df.head())

# Step 3: Dataset Info
print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())

# Step 4: Missing Value Check
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Handle Missing Values
df.dropna(subset=['Campaign_ID', 'Impressions', 'Clicks'], inplace=True)
df['Location'] = df['Location'].fillna("Unknown")
df['Channel_Used'] = df['Channel_Used'].fillna("Other")
df['Duration'] = df['Duration'].fillna("Unknown")

# Step 6: Feature Engineering - Estimated Conversions
df['Estimated_Conversions'] = (df['Conversion_Rate'] * df['Clicks']).round(0).astype(int)

# Step 7: Remove Duplicates
df.drop_duplicates(inplace=True)

# Step 8: Convert 'Date' Column and Extract Features
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.day_name()
df['Year'] = df['Date'].dt.year

# Step 9: Data Type Optimization
df['Company'] = df['Company'].astype('category')
df['Campaign_Type'] = df['Campaign_Type'].astype('category')
df['Target_Audience'] = df['Target_Audience'].astype('category')
df['Channel_Used'] = df['Channel_Used'].astype('category')
df['Location'] = df['Location'].astype('category')
df['Language'] = df['Language'].astype('category')
df['Customer_Segment'] = df['Customer_Segment'].astype('category')

# Step 10: Clean 'Acquisition_Cost' if it contains strings like '$'
if df['Acquisition_Cost'].dtype == 'object':
    df['Acquisition_Cost'] = df['Acquisition_Cost'].replace('[\$,]', '', regex=True).astype(float)

# Step 11: Add KPIs (optional for EDA/BI)
df['CTR'] = (df['Clicks'] / df['Impressions']).round(4)
df['CPC'] = (df['Acquisition_Cost'] / df['Clicks']).round(2)
df['Engagement_per_Click'] = (df['Engagement_Score'] / df['Clicks']).round(2)

# Replace inf with 0
df.replace([np.inf, -np.inf], 0, inplace=True)

# Step 12: Save Cleaned Data
df.to_csv("cleaned_marketing_campaign_data.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_marketing_campaign_data.csv'")

