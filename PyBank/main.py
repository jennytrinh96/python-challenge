# PyBank


# Import Modules
import csv
import os

# Set up file path for csv file
budget_csv_path = os.path.join("Resources", "budget_data.csv")
# print(csv_path) Check path, Path is good to go


# Variables to use: 
total_months = 0 
# Accumulator for months


# FIRST: Open csv file so we can search and do analysis
with open(budget_csv_path) as budget_file:

    # Create reader object
    csv_reader = csv.reader(budget_file)

    # If header exists, SKIP
    csv_header = next(csv_reader)

    # Increment the count of total months
    total_months += 1

    # Create for loop to read each row
    for row in csv_reader:
        total_months += 1


# Generate the output
output = f"Total Months = {total_months}"
print(output)











# Total number of months 
    # Use Running Totals



# Net total amount of Profit/Loss
    # Use runnning totals house of pies activity?

