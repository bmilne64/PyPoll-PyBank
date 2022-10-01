#modules
import os
import csv
from statistics import mean

#set path for file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    #print heading 
    print('Financial Analysis')
    print('----------------------------')

    #define the values 
    #set to 0 as a starting point 
    total_months = 0 
    profit_losses = 0
    change = 0
    average_change = 0
    profit_increase = 0
    profit_decrease = 0 
    store_profit = 0

    #start loop for csv 
    for row in csvreader:  

        #count the total number of rows/months 
        total_months += 1
        
        #for every row after the first, calacuate the change in value 
        if total_months > 1:

            #the change is the current value - the stored prior value 
            change = (int(row[1]) - store_profit)

        #average change = average change + change 
        average_change += change 

        #define profit_losses
        #profit losses = profit losses + the count of column 2
        profit_losses += int(row[1])

        #define the stored prior value as the count of coulmn 2
        store_profit = int(row[1])

        #if the change is greater than the stroed profit increase value 
        if change > profit_increase:

            #the stored value becomes change 
            profit_increase = change 
            #the date associated with the value change is saved 
            date_increase = row[0]
        
       #if the change is less than the stroed profit increase value 
        if change < profit_decrease:

            #the stored value becomes change 
            profit_decrease = change 
            #the date associated with the value change is saved 
            date_decrease = row[0]

    # average change = the number in average_change divided by the total times of change (85)
    #no change for the first month (total_months - 1)
    average_change = (int(average_change)/int(total_months - 1))

    #round the total change to 2 decimal points 
    average_change = round(average_change, 2)

    #print all statements 
    print('Total Months:' + str(total_months))
    print('Total: $' + str(profit_losses))
    print('Average Change: $' + str(average_change)) 
    print('Greatest Increase in Profits:  ' + str(date_increase) + ' ($' + str(profit_increase) + ')')
    print('Greatest Decrease in Profits:  ' + str(date_decrease) + ' ($' + str(profit_decrease) + ')')

