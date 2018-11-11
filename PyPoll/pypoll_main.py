import os 
import csv 

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = csvreader.fieldnames

    

    row_count = sum(1 for row in csvfile) 



    

print("Election Results")
print("--------------------")
print("Total Votes: " + str(row_count))
print("--------------------")

print("--------------------")

print("--------------------")

