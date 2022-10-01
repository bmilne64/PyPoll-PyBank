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

    print('Financial Analysis')
    print('----------------------------')

    total_months = 0 
    profit_losses = 0
    change = 0
    average_change = 0
    profit_increase = 0
    profit_decrease = 0 
    store_profit = 0

    for row in csvreader:  

        total_months += 1
        
        if total_months > 1:
            change = (int(row[1]) - store_profit)

        average_change += change 

        profit_losses += int(row[1])

        store_profit = int(row[1])

        if change > profit_increase:
            profit_increase = change 
            date_increase = row[0]
        
        if change < profit_decrease:
            profit_decrease = change 
            date_decrease = row[0]

    average_change = (int(average_change)/int(total_months - 1))
    average_change = round(average_change, 2)

    
    print('Total Months:' + str(total_months))
    print('Total: $' + str(profit_losses))
    print('Average Change: $' + str(average_change)) 
    print('Greatest Increase in Profits:  ' + str(date_increase) + ' ($' + str(profit_increase) + ')')
    print('Greatest Decrease in Profits:  ' + str(date_decrease) + ' ($' + str(profit_decrease) + ')')

