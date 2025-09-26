import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Load data and clean it (same as before)
# Get current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct full path to the CSV in same folder
csv_path = os.path.join(script_dir, 'ecommerce_customer_data.csv')

df = pd.read_csv(csv_path)


df['Age'] = df['Age'].fillna(df['Age'].mean())
df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].mean())
df['TotalSpent'] = df['TotalSpent'].fillna(df['TotalSpent'].mean())
df['Gender'] = df['Gender'].str.capitalize()
df['Gender'] = df['Gender'].replace(['Unknown', 'unknown', 'nan', 'None'], 'Unknown')
df['Gender'] = df['Gender'].fillna('Unknown')  # handles actual None/NaN values

df['Country'] = df['Country'].str.replace('.', '', regex=False).str.upper().fillna('UNKNOWN')

# Create all plots first

plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df, order=df['Gender'].value_counts().index)
plt.title('Gender Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gender_distribution.png')

plt.figure(figsize=(8,4))
sns.countplot(x='Country', data=df, order=df['Country'].value_counts().index)
plt.title('Country Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('country_distribution.png')

plt.figure(figsize=(6,4))
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # convert to numbers, invalid to NaN
df['Age'] = df['Age'].fillna(df['Age'].mean())

plt.title('Age Distribution')
plt.tight_layout()
plt.savefig('age_distribution.png')

plt.figure(figsize=(6,4))
sns.scatterplot(x='AnnualIncome', y='TotalSpent', data=df)
plt.title('Annual Income vs Total Spent')
plt.tight_layout()
plt.savefig('income_vs_spent.png')

# Show all plots at once
plt.show()
