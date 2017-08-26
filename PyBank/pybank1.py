# ## Option 1: PyBank
# ![Revenue](Images/revenue-per-lead.jpg)
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The total amount of revenue gained over the entire period
# * The average change in revenue between months over the entire period
# * The greatest increase in revenue (date and amount) over the entire period
# * The greatest decrease in revenue (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:
# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```
# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Dependencies
import csv

# Files to Load
file_to_load = "data/budget_data_1.csv"
file_to_output = "analysis/budget_analysis_1.txt"

# Variables to Track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

# Read Files
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        # print(row)

        # Keep track of changes
        revenue_change = int(row["Revenue"]) - prev_revenue
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row["Revenue"])
        # print(prev_revenue)

        # Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        # Add to the revenue_changes list
        revenue_changes.append(int(row["Revenue"]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output (Terminal)
    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Revenue Change: $" + str(int((sum(revenue_changes) / len(revenue_changes)))))
    print("Greatest Increase in Revenue: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease in Revenue: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

# Output Files (Txt File)
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: $" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Revenue Change: $" + str(int((sum(revenue_changes) / len(revenue_changes)))))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Revenue: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Revenue: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")