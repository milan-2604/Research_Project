import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Get current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct full path to the CSV in same folder
csv_path = os.path.join(script_dir, 'ecommerce_customer_data.csv')

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Fill missing values in 'Age' column with the mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing values in 'AnnualIncome' column with the mean annual income
df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].mean())

# Fill missing values in 'TotalSpent' column with the mean total spent
df['TotalSpent'] = df['TotalSpent'].fillna(df['TotalSpent'].mean())

# Standardize 'Gender' values by capitalizing the first letter
df['Gender'] = df['Gender'].str.capitalize()

# Replace various unknown or invalid gender strings with a single 'Unknown' label
df['Gender'] = df['Gender'].replace(['Unknown', 'unknown', 'nan', 'None'], 'Unknown')

# Fill any remaining missing 'Gender' values (like actual NaNs) with 'Unknown'
df['Gender'] = df['Gender'].fillna('Unknown')

# Clean 'Country' column by removing periods, converting to uppercase, and filling missing with 'UNKNOWN'
df['Country'] = df['Country'].str.replace('.', '', regex=False).str.upper().fillna('UNKNOWN')

# Create all plots first

# Plot 1: Gender distribution countplot
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df, order=df['Gender'].value_counts().index)
plt.title('Gender Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gender_distribution.png')

# Plot 2: Country distribution countplot
plt.figure(figsize=(8,4))
sns.countplot(x='Country', data=df, order=df['Country'].value_counts().index)
plt.title('Country Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('country_distribution.png')


# Plot 3: Age distribution histogram with KDE curve
plt.figure(figsize=(6,4))
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # convert to numbers, invalid to NaN
df['Age'] = df['Age'].fillna(df['Age'].mean())

sns.histplot(df['Age'], bins=15, kde=True) 
plt.title('Age Distribution')
plt.tight_layout()
plt.savefig('age_distribution.png')

# Plot 4: Scatterplot of Annual Income vs Total Spent
plt.figure(figsize=(6,4))
sns.scatterplot(x='AnnualIncome', y='TotalSpent', data=df)
plt.title('Annual Income vs Total Spent')
plt.tight_layout()
plt.savefig('income_vs_spent.png')

# Show all plots at once
plt.show()
