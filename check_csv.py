import csv
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the CSV file assuming it's in the same folder as this script
csv_path = os.path.join(script_dir, 'ecommerce_customer_data.csv')

# Open the CSV file for reading
with open(csv_path, newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Count the number of rows by iterating through the reader
    row_count = sum(1 for row in reader)

# Print the total number of rows found in the CSV file
print(f"The CSV file has {row_count} rows.")
