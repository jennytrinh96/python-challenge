# PyBank

# Import Modules
import csv
from distutils.command.build_scripts import first_line_re
import os

# Set up file path for csv file
budget_csv_path = os.path.join("Resources", "budget_data.csv")
# print(csv_path) Check path, Path is good to go

# File to hold output of analysis
analysis_path = os.path.join("Analysis", "budget_analysis.txt")


# Variables to use:

# Accumulator for months  
total_months = 0 

# Accumulator for Profit/Loss
total_profit_loss = 0

# List of monthly net changes
monthly_changes = []

#List of Months
months = []

# FIRST: Open csv file so we can search and do analysis
with open(budget_csv_path) as budget_file:

    # Create reader object
    csv_reader = csv.reader(budget_file)

    # If header exists, SKIP
    csv_header = next(csv_reader)

    # Move to the first row
    first_row = next(csv_reader)

    # Increment count of total months
    total_months += 1

    # Increment Profit/Loss to find net total
    total_profit_loss += float(first_row[1])

    # Establish previous row change
    previous_amount = float(first_row[1])

    # Create for loop to read each row
    for row in csv_reader:
        # Increment count of total months
        total_months += 1

        # Increment Profit/Loss to find net total
        total_profit_loss += float(row[1])

        # Calculate net change 
        net_change = float(row[1]) - previous_amount

        # Append net change to monthly changes
        monthly_changes.append(net_change)

        # Add the first month when a change occurs month = index[0]
        months.append(row[0])

        # Update previous revenue
        previous_amount = float(row[1])

# Calculate the average new change per month
# sum of all the months changes / the number of months
avg_netchange = sum(monthly_changes) / len(monthly_changes)

# List greatest profit increase with appropriate month
max_increase = [months[0], monthly_changes[0]]

# List greatest profit decrease with appropriate month
max_decrease = [months[0], monthly_changes[0]]

# Use this loop to calculate index of greatest and least monthly change
# Loop means, for each row in in the range of monthly changes, do...
for m in range(len(monthly_changes)):

    # Calculate max_increase
    if monthly_changes[m] > max_increase[1]:
        
        # Whenever statement becomes true, a greatest value is replaced
        max_increase[1] = monthly_changes[m]

        # Update month
        max_increase[0] = months[m]

    # Calculate max_decrease
    if monthly_changes[m] < max_decrease[1]:
        
        # Whenever statement becomes true, a greatest value is replaced
        max_decrease[1] = monthly_changes[m]

        # Update month
        max_decrease[0] = months[m]

# Generate the output
output = (
    f"\nBudget Analysis: \n"
    f"------------------------------------\n "
    f"\tTotal Months = {total_months} \n"
    f"\t Net total of Profit/Losses = ${total_profit_loss:,.2f}\n "
    f"\t Average Monthly Change = ${avg_netchange:,.2f}\n "
    f"\t Greatest Increase in Profits = {max_increase[0]} ($ {max_increase[1]:,.2f})\n "
    f"\t Greatest Decrease in Profits = {max_decrease[0]} ($ {max_decrease[1]:,.2f})\n "
    f"------------------------------------\n "
)

# Print output
print(output)

# Export output to .txt file
with open(analysis_path, 'w') as text_file:
    text_file.write(output)
