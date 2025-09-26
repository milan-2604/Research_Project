import csv

filename = '../ecommerce_customer_data.csv'
  # Replace with your actual CSV filename

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    row_count = sum(1 for row in reader)

print(f"The CSV file has {row_count} rows.")
