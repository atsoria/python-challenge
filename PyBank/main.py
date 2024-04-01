#Always begin by importing to get the pathways correct
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
outputpath = os.path.join('Analysis', 'results.txt')
# Lists to store data

with open(csvpath,"r") as csvfile: #3.2 activity 05  also see activity 08/09
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#Variables
    TotalMonths = 0

    for row in csvreader:
        TotalMonths += 1 


output = "Financial Analysis\n"
output += "----------------------------\n"
#The total number of months included in the dataset
output += f"Total Months: {TotalMonths}\n"
#The net total amount of "Profit/Losses" over the entire period
 # print(f"Total: "{Total})
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
 # print(f"Average Cahnge: "{AverageChange})
#The greatest increase in profits (date and amount) over the entire period
 # print(f"Greatest Increase in Profits: "{Date} {ProfitIncrease})
#The greatest decrease in profits (date and amount) over the entire period
 #print(f"Greatest Decrease in Profits: "{Date2} {ProfitDecrease})
print(output)
with open(outputpath, "w") as txtfile:
    txtfile.write(output)
