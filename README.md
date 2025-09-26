# Ecommerce Customer Data Analysis

## Project Overview

This project analyzes ecommerce customer data to extract insights about customer demographics, spending patterns, and behavior. The workflow covers everything from initial dataset generation to cleaning, feature engineering, exploratory analysis, and predictive modeling.

---

## Project Workflow

### Step 1: Generating the Initial Dataset

- Created a synthetic ecommerce customer dataset (`ecommerce_customer_data.csv`) with features like CustomerID, Name, Age, Gender, Email, SignupDate, LastPurchaseDate, AnnualIncome, TotalSpent, and Country.
- This CSV file forms the base data for all subsequent analysis.

### Step 2: Data Cleaning and Preprocessing

- Loaded the dataset into a pandas DataFrame.
- Converted date columns (`SignupDate`, `LastPurchaseDate`) to datetime format.
- Filled missing numeric values (Age, AnnualIncome, TotalSpent) with column means.
- Standardized categorical columns such as Gender and Country, handling inconsistencies and missing values.
- Detected and removed duplicate entries based on `CustomerID`.
- Applied outlier capping on numeric columns to reduce the effect of extreme values.

### Step 3: Feature Engineering

- Calculated `DaysSinceLastPurchase` to quantify customer recency.
- Extracted `SignupYear` from the signup date to capture temporal trends.
- Encoded categorical variables:
  - Label Encoding for Gender.
  - One-Hot Encoding for Country.

### Step 4: Exploratory Data Analysis (EDA)

- Generated visualizations to understand data distributions and relationships:
  - Gender distribution count plot.
  - Country distribution bar plot.
  - Age distribution histogram with KDE.
  - Scatter plot showing the relationship between Annual Income and Total Spent.
- Saved all plots as PNG files in the project directory.

### Step 5: Machine Learning Modeling

- Created a binary target variable `HighSpender`, where customers spending above the median `TotalSpent` are labeled as high spenders.
- Selected relevant features for modeling.
- Split the dataset into training and testing sets.
- Trained a Random Forest classifier.
- Evaluated the model using classification report and confusion matrix, achieving reasonable accuracy in predicting high spenders.

### Step 6: Saving Outputs

- Saved the cleaned and processed dataset as `cleaned_ecommerce_customer_data.csv`.
- Visualization images are saved automatically.
- Printed summaries and model evaluation metrics to the console.

---

## How to Run

1. Ensure Python 3.x is installed along with required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn

Project Structure
Research Project/
├── analyze.py
├── ecommerce_customer_data.csv
├── cleaned_ecommerce_customer_data.csv
├── gender_distribution.png
├── country_distribution.png
├── age_distribution.png
├── income_vs_spent.png
└── README.md
