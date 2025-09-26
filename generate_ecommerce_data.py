import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility of results
np.random.seed(42)

# Number of sample rows to generate
n = 200  

# Generate unique Customer IDs
customer_ids = range(1000, 1000 + n)

# Generate fake customer names
names = [f"Customer_{i}" for i in range(n)]

# Generate normally distributed ages (floats) centered around 35 with std dev 10
ages = np.random.normal(loc=35, scale=10, size=n)

# Randomly assign gender values (including inconsistent cases and 'unknown')
genders = np.random.choice(['Male', 'Female', 'Other', 'unknown', 'FEMALE', 'male'], size=n)

# Create fake emails based on customer index
emails = [f"customer{i}@example.com" for i in range(n)]

# Generate signup dates randomly within ~3 years from Jan 1, 2020
signup_dates = [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1000)) for _ in range(n)]

# Generate last purchase dates randomly after signup date (between 10 and 900 days later)
last_purchase_dates = [signup + timedelta(days=np.random.randint(10, 900)) for signup in signup_dates]

# Generate annual incomes normally distributed around $60,000 with std dev $15,000
annual_incomes = np.random.normal(loc=60000, scale=15000, size=n).round(2)

# Generate total spent as a random percentage (5%-50%) of annual income
total_spent = (annual_incomes * np.random.uniform(0.05, 0.5, size=n)).round(2)

# Randomly assign countries, including inconsistent formats and 'Unknown'
countries = np.random.choice(['USA', 'India', 'Canada', 'UK', 'usa', 'U.K.', 'Unknown'], size=n)

# Introduce missing values randomly in several columns for realism

# Randomly assign NaN to 10 ages
for i in np.random.choice(n, size=10, replace=False):
    ages[i] = np.nan

# Randomly assign NaN to 5 annual incomes
for i in np.random.choice(n, size=5, replace=False):
    annual_incomes[i] = np.nan

# Randomly assign NaN to 5 total spent values
for i in np.random.choice(n, size=5, replace=False):
    total_spent[i] = np.nan

# Randomly assign NaN to 5 genders
for i in np.random.choice(n, size=5, replace=False):
    genders[i] = np.nan

# Randomly assign NaN to 5 countries
for i in np.random.choice(n, size=5, replace=False):
    countries[i] = np.nan

# Create a pandas DataFrame with all the generated data
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Name': names,
    'Age': ages,
    'Gender': genders,
    'Email': emails,
    'SignupDate': signup_dates,
    'LastPurchaseDate': last_purchase_dates,
    'AnnualIncome': annual_incomes,
    'TotalSpent': total_spent,
    'Country': countries
})

# Add a couple of duplicate rows for testing duplicate handling if needed
df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)

# Save the DataFrame to a CSV file without the index column
df.to_csv("ecommerce_customer_data.csv", index=False)

print("✅ CSV file 'ecommerce_customer_data.csv' has been created successfully!")