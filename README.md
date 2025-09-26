# E-commerce Customer Data Analysis

## 📊 Project Overview

This project analyzes synthetic e-commerce customer data to uncover insights about customer demographics, behavior, and spending patterns. It includes data generation, cleaning, feature engineering, visualization, and predictive modeling to identify high-value customers.

---

## 🗂️ Project Structure

```
Research_Project/
├── generate_ecommerce_data.py              # Script to generate synthetic e-commerce data
├── ecommerce_customer_data.csv             # Raw dataset generated
├── check_csv.py                            # Utility to check number of rows in the CSV
├── analyze.py                              # Main script: cleaning, analysis, visualization, modeling
├── gender_distribution.png                 # Gender distribution plot
├── country_distribution.png                # Country distribution plot
├── age_distribution.png                    # Age distribution histogram
├── income_vs_spent.png                     # Annual Income vs Total Spent scatter plot
├── cleaned_ecommerce_customer_data.csv     # Cleaned dataset after preprocessing
├── requirements.txt                        # Required Python dependencies
└── README.md                               # Project documentation (this file)
```




---

## 🔁 Project Workflow

### ✅ Step 1: Generating the Initial Dataset
- Generated a synthetic dataset `ecommerce_customer_data.csv` with:
  - `CustomerID`, `Name`, `Age`, `Gender`, `Email`, `SignupDate`, `LastPurchaseDate`, `AnnualIncome`, `TotalSpent`, and `Country`

---

### 🧹 Step 2: Data Cleaning & Preprocessing
- Loaded data using **pandas**
- Converted `SignupDate` and `LastPurchaseDate` to `datetime`
- Filled missing numeric values (`Age`, `AnnualIncome`, `TotalSpent`) with column means
- Standardized `Gender` and `Country` entries
- Removed duplicates based on `CustomerID`
- Applied outlier capping to reduce skew in numeric features

---

### 🛠️ Step 3: Feature Engineering
- Created `DaysSinceLastPurchase` to quantify recency
- Extracted `SignupYear` to capture temporal patterns
- Encoded categorical variables:
  - Label Encoding for `Gender`
  - One-Hot Encoding for `Country`

---

### 📈 Step 4: Exploratory Data Analysis (EDA)
- Generated visualizations to explore key distributions and relationships:
  - `gender_distribution.png`: Gender distribution count plot
  - `country_distribution.png`: Country-wise customer count
  - `age_distribution.png`: Age histogram with KDE
  - `income_vs_spent.png`: Scatter plot of Annual Income vs Total Spent

---

### 🤖 Step 5: Machine Learning Modeling
- Created binary target variable `HighSpender` (1 = above median `TotalSpent`)
- Selected features and split dataset into training and test sets
- Trained a **Random Forest Classifier**
- Evaluated model using:
  - Classification Report
  - Confusion Matrix

---

### 💾 Step 6: Outputs
- Cleaned dataset saved as `cleaned_ecommerce_customer_data.csv`
- Visualizations saved as PNGs
- Printed summaries and evaluation metrics in the console

---

## ▶️ How to Run

### 1. Install Requirements

Ensure Python 3.x is installed. Then install dependencies:

```bash
pip install -r requirements.txt
