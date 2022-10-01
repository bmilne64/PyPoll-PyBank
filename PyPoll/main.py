#modules
import os
import csv
import sys 


sys.stdout = open("results.txt", "a")

#set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Open the CSV

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    print('Election Results')
    print('----------------------------')

    total_votes = 0 
    votes_list = []
    store_cand = ''
    win_votes = 0
    win_cand = ""
    for row in csvreader:   
    
        cands = (row[2])
        votes_list.append(cands)
        
    votes_list.sort()
    print('Total Votes:' + str(len(votes_list)))
    print('----------------------------')
    
    for cand in votes_list:

        if cand != store_cand:
            votes = votes_list.count(cand)
            perc_votes = votes/len(votes_list)
            perc_votes = "{:.3%}".format(perc_votes)
            print(str(cand) +': ' + str(perc_votes) + ' (' + str(votes) + ')')
            if votes > win_votes:
                win_votes = votes 
                win_cand = cand 
            store_cand = cand 

print('----------------------------')

print('Winner: ' + str(win_cand))
print('----------------------------')

sys.stdout.close()
sys.stdout = sys.__stdout__
with open('../PyPoll/results.txt') as file:
    terminal = file.read()
    print(terminal)
