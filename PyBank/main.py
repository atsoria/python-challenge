#Import to get the pathways correct
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
outputpath = os.path.join('Analysis', 'results.txt')
#store the header
csv_header = None
with open(csvpath,"r") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#Variables
    changes = []
    total_months = 0
    net_total = 0
    previous_profit = None
    max_change = -999999999
    min_change = 999999999
    max_date = ""
    min_date = ""


    for row in csvreader:
        #Find total months
        total_months += 1 
        #Find net total of profit and losses
        profit_loss = int(row[1])
        net_total += profit_loss
    
        change = 0
        if previous_profit is not None:
            change = profit_loss - previous_profit
            changes.append(change)
        previous_profit = profit_loss
        #Find greatest increase in profits and print the corresponding date
        if max_change < change:
            max_change = change
            max_date = row[0]
        #Find greatest decrease in profits and print the corresponding date
        if min_change > change:
            min_change = change
            min_date = row[0]
#Find avg change of profit and losses
average_change = sum(changes)/len(changes)


output = "Financial Analysis\n"
output += "----------------------------\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${net_total}\n"
output += f"Average Change: ${average_change:.2f}\n"
output += f"Greatest Increase in Profits: {max_date} (${max_change})\n"
output += f"Greatest Decrease in Profits: {min_date} (${min_change})\n"
#Print the results 
print(output)
#Write to text file
with open(outputpath, "w") as txtfile:
    txtfile.write(output)
