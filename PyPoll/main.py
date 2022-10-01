#modules
import os
import csv
import sys 

#open file for results 
sys.stdout = open("results.txt", "a")

#set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #don't include the header 
    next(csvreader, None)
    
    #print the heading 
    print('Election Results')
    print('----------------------------')

    #define the values 
    total_votes = 0 
    votes_list = []
    store_cand = ''
    win_votes = 0
    win_cand = ""

    #start the loop for the csv
    for row in csvreader:   
        
        #define which column you want to look at 
        cands = (row[2])

        #append the list to include all the values 
        votes_list.append(cands)
    
    #sort the list to put the names in order 
    votes_list.sort()

    #print the length of the list to get the total number of votes 
    print('Total Votes:' + str(len(votes_list)))
    print('----------------------------')
    
    #start the loop for the list 
    for cand in votes_list:

        #if each name do not equal the prior stored name then 
        if cand != store_cand:

            #count the number of times the name appears in the list to calculate amount of votes 
            votes = votes_list.count(cand)

            #calculate the percetage of votes each candidate got 
            perc_votes = votes/len(votes_list)

            #format the numbers as a percent 
            perc_votes = "{:.3%}".format(perc_votes)

            #print the candidtae name, vote percentage and number of votes received 
            print(str(cand) +': ' + str(perc_votes) + ' (' + str(votes) + ')')
            
            # to find who got the highest number of votes 
            #if the current votes are greater than the stored votes per candidate then 
            if votes > win_votes:

                #the current votes become the stored winning votes 
                win_votes = votes 
                #the current candiate becomes the stored winning candidate 
                win_cand = cand 
            #reset the stored candidate to coutn the next candidate's votes 
            store_cand = cand 

print('----------------------------')

#print the candidate with the most votes after the loop 
print('Winner: ' + str(win_cand))
print('----------------------------')

#close the results file 
sys.stdout.close()

#revert back to the terminal window 
sys.stdout = sys.__stdout__

#open the results file 
with open('../PyPoll/results.txt') as file:

    #read the results file 
    terminal = file.read()

    #print the results to terminal 
    print(terminal)
