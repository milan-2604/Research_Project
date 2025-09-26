import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import os

# --- Setup ---
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'ecommerce_customer_data.csv')

# --- Load data ---
df = pd.read_csv(csv_path)

# --- Part 1: Inspect data types ---
print("Data types before conversion:")
print(df.dtypes)

# Convert date columns to datetime
df['SignupDate'] = pd.to_datetime(df['SignupDate'])
df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])

print("\nData types after conversion:")
print(df.dtypes)

# --- Part 2: Handle missing data ---

# Numeric columns: fill NaNs with mean
for col in ['Age', 'AnnualIncome', 'TotalSpent']:
    df[col] = df[col].fillna(df[col].mean())

# Categorical columns: standardize and fill missing
df['Gender'] = df['Gender'].str.capitalize()
df['Gender'] = df['Gender'].replace(['Unknown', 'unknown', 'nan', 'None'], 'Unknown')
df['Gender'] = df['Gender'].fillna('Unknown')

df['Country'] = df['Country'].str.replace('.', '', regex=False).str.upper()
df['Country'] = df['Country'].fillna('UNKNOWN')

# --- Part 3: Handle duplicates ---
duplicate_count = df.duplicated(subset='CustomerID').sum()
print(f"\nNumber of duplicate CustomerID rows: {duplicate_count}")
df = df.drop_duplicates(subset='CustomerID', keep='first')

# --- Part 4: Handle outliers with capping ---
def cap_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
    df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])

for col in ['Age', 'AnnualIncome', 'TotalSpent']:
    cap_outliers(col)

# --- Part 5: Feature engineering ---

# Days since last purchase (relative to today)
df['DaysSinceLastPurchase'] = (pd.Timestamp.today() - df['LastPurchaseDate']).dt.days

# Signup year extraction
df['SignupYear'] = df['SignupDate'].dt.year

# --- Part 6: Encoding categorical data ---

# Label encode Gender
le_gender = LabelEncoder()
df['Gender'] = le_gender.fit_transform(df['Gender'])

# One-hot encode Country
df = pd.get_dummies(df, columns=['Country'], drop_first=True)

# --- Part 7: Exploratory plots ---

plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.tight_layout()
plt.savefig('gender_distribution.png')


plt.figure(figsize=(8,4))
country_cols = [col for col in df.columns if col.startswith('Country_')]
country_counts = df[country_cols].sum().sort_values(ascending=False)
sns.barplot(x=country_counts.index.str.replace('Country_', ''), y=country_counts.values)
plt.title('Country Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('country_distribution.png')


plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=15, kde=True)
plt.title('Age Distribution')
plt.tight_layout()
plt.savefig('age_distribution.png')


plt.figure(figsize=(6,4))
sns.scatterplot(x='AnnualIncome', y='TotalSpent', data=df)
plt.title('Annual Income vs Total Spent')
plt.tight_layout()
plt.savefig('income_vs_spent.png')

plt.show()
# --- Part 8: Machine Learning Model ---

# Target: High spender if TotalSpent > median
median_spent = df['TotalSpent'].median()
df['HighSpender'] = (df['TotalSpent'] > median_spent).astype(int)

feature_cols = ['Age', 'Gender', 'AnnualIncome', 'DaysSinceLastPurchase', 'SignupYear'] + country_cols
X = df[feature_cols]
y = df['HighSpender']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# --- Part 9: Final inspection and save ---

print(f"\nCleaned dataset shape: {df.shape}")
print(df.describe(include='all'))

cleaned_csv_path = os.path.join(script_dir, 'cleaned_ecommerce_customer_data.csv')
df.to_csv(cleaned_csv_path, index=False)
print(f"\n✅ Cleaned dataset saved to {cleaned_csv_path}")
print("Handled duplicates.")
print("Starting outlier capping...")
print("Generating plots...")
print("Training model...")
print("Saving cleaned data...")

