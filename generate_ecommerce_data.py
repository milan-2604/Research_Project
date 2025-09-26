import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n = 200  # number of rows
customer_ids = range(1000, 1000 + n)
names = [f"Customer_{i}" for i in range(n)]

# ✅ Keep ages as float to allow np.nan
ages = np.random.normal(loc=35, scale=10, size=n)

genders = np.random.choice(['Male', 'Female', 'Other', 'unknown', 'FEMALE', 'male'], size=n)
emails = [f"customer{i}@example.com" for i in range(n)]
signup_dates = [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1000)) for _ in range(n)]
last_purchase_dates = [signup + timedelta(days=np.random.randint(10, 900)) for signup in signup_dates]
annual_incomes = np.random.normal(loc=60000, scale=15000, size=n).round(2)
total_spent = (annual_incomes * np.random.uniform(0.05, 0.5, size=n)).round(2)
countries = np.random.choice(['USA', 'India', 'Canada', 'UK', 'usa', 'U.K.', 'Unknown'], size=n)

# ✅ Introduce some missing values
for i in np.random.choice(n, size=10, replace=False):
    ages[i] = np.nan
for i in np.random.choice(n, size=5, replace=False):
    annual_incomes[i] = np.nan
for i in np.random.choice(n, size=5, replace=False):
    total_spent[i] = np.nan
for i in np.random.choice(n, size=5, replace=False):
    genders[i] = np.nan
for i in np.random.choice(n, size=5, replace=False):
    countries[i] = np.nan

# ✅ Create DataFrame
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

# ✅ Add a few duplicate rows for testing
df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)

# ✅ Save to CSV
df.to_csv("ecommerce_customer_data.csv", index=False)
print("✅ CSV file 'ecommerce_customer_data.csv' has been created successfully!")
