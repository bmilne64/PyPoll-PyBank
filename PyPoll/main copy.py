#modules
import os
import csv

#set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    print('Election Results')
    print('----------------------------')

    set() 
    total_votes = 0
    candidate_1 = 0
    candidate_2 = 0
    candidate_3 = 0
    for row in csvreader:   
       total_votes += 1

        if row[2] == str('Charles Casper Stockham'):
            candidate_1 += 1
        elif row[2] == str('Diana DeGette'):
            candidate_2 += 1
        elif row[2] == str('Raymon Anthony Doane'):
            candidate_3 += 1

        can1_percent = candidate_1/total_votes
        can1_percent = "{:.3%}".format(can1_percent)
        can2_percent = candidate_2/total_votes
        can2_percent = "{:.3%}".format(can2_percent)
        can3_percent = candidate_3/total_votes
        can3_percent = "{:.3%}".format(can3_percent)


print('Total Votes:' + str(total_votes))
print('----------------------------')

print('Charles Casper Stockham:' + str(can1_percent) + ' ('+ str(candidate_1) + ')')
print('Diana DeGette:' + str(can2_percent) + ' ('+ str(candidate_2) + ')')
print('Raymon Anthony Doane:' + str(can3_percent) + ' ('+ str(candidate_3) + ')')
print('----------------------------')



print('Winner')
print('----------------------------')