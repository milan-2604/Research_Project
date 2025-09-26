Research Project/
├── analyze.py                 # Main analysis and visualization script
├── check_csv.py               # Quick script to count CSV rows
├── ecommerce_customer_data.csv # Dataset CSV file
├── gender_distribution.png    # Output plot images
├── country_distribution.png
├── age_distribution.png
├── income_vs_spent.png
└── README.md                  # This documentation file

# Research Project: E-commerce Customer Data Analysis

## Overview
This project simulates, cleans, and analyzes e-commerce customer data to uncover patterns and insights.

## Files Description

### generate_data.py
- Generates a synthetic dataset with 200 customers.
- Introduces missing data and duplicates for realistic testing.
- Outputs a CSV file named `ecommerce_customer_data.csv`.

### check_csv.py
- Counts and prints the number of rows in the CSV file.
- Useful for quick verification of data presence and size.

### analyze.py
- Loads the CSV file and cleans missing or inconsistent data.
- Standardizes categorical columns for consistency.
- Creates multiple visualizations to explore gender, country distribution, age, and spending behavior.
- Saves visualizations as PNG files and displays them.

## How to Run
1. Run `generate_data.py` to create the raw dataset.
2. (Optional) Run `check_csv.py` to verify row count.
3. Run `analyze.py` to clean the data and generate visual insights.

## Notes
- The cleaning logic is done in `analyze.py`.
- Data generation mimics real-world data with noise for robust testing.
