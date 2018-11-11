import os 
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    month_count = sum(1 for row in csvfile)
    total = 0
    for row in csvreader:  
        total += int(row[1])


print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(month_count))
print("Total: " + str(total))
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")