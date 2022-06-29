# PyBank


# Import Modules
import csv
import os

# Set up file path for csv file
budget_csv_path = os.path.join("Resources", "budget_data.csv")
# print(csv_path) Check path, Path is good to go


# File to hold output of analysis
output_budget_path = os.path.join("budget_analysis.txt")

# Variables to use: 
total_months = 0 
# Accumulator for months


# FIRST: Open csv file so we can search and do analysis
with open(budget_csv_path) as budget_file:

    # Create reader object
    csv_reader = csv.reader(budget_file)

    # If header exists, SKIP
    csv_header = next(csv_reader)

    # Create for loop to read each row
    for row in csv_reader:
        total_months += 1


# Generate the output
output = (
    f"\nBudget Analysis: \n"
    f"------------------------------------\n "
    f"\tTotal Months = {total_months}"
)

# Print output
print(output)

# Export output to .txt file
with open(output_budget_path, 'w') as text_file:
    text_file.write(output)


# Total number of months 
    # Use Running Totals



# Net total amount of Profit/Loss
    # Use runnning totals house of pies activity?

