# PyBank


# Import Modules
import csv
import os

# Set up file path for csv file
csv_path = os.path.join("..", "Resources", "budget_data.csv")
# print(csv_path) Check path, Path is good to go

# FIRST: Open csv file so we can search and do analysis
with open(csv_path, 'r') as file:

    # Create reader object
    csv_reader = csv.reader(file, delimiter=",")

    # If header exists, SKIP
    csv_header = next(csv_reader)

    








# Total number of months 
    # Use Running Totals



# Net total amount of Profit/Loss
    # Use runnning totals house of pies activity?

