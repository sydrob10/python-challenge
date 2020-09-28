#import os module
import os

#import csv module for opening csv files, set path for csv file
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#open csv file and tell python to read data in file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip the header row and go straight to the data
    header = next(csvreader)

    #set initial values for variables
    vote_count = 0
    candidate_list = []
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
                    
    #read each value in the row and calculate the following
    for row in csvreader:        
        #calculate the number of votes by adding one for each iteration
        vote_count += 1
        #set last column = candidate name
        candidate_name = row[2]
        #make a list of candidate names
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
        #add one vote to each vote counter when candidate's name appears
        if candidate_name == "Khan":
            Khan_votes +=1
        if candidate_name == "Correy":
            Correy_votes +=1
        if candidate_name == "Li":
            Li_votes +=1
        if candidate_name == "O'Tooley":
            OTooley_votes +=1
    #calculate total votes
    total_votes = Khan_votes + Correy_votes + Li_votes + OTooley_votes
    #calculate each candidate's percentage of votes
    Khan_percent = "{:.3f}".format((Khan_votes/total_votes)*100)
    Correy_percent = "{:.3f}".format((Correy_votes/total_votes)*100)
    Li_percent = "{:.3f}".format((Li_votes/total_votes)*100)
    OTooley_percent = "{:.3f}".format((OTooley_votes/total_votes)*100)

    #see who is the winner by checking if their percent is greater than each candidate
    if Khan_percent > Correy_percent and Khan_percent > Li_percent and Khan_percent > OTooley_percent:
        winner_name = "Khan"
    if Correy_percent > Khan_percent and Correy_percent > Li_percent and Correy_percent > OTooley_percent:
        winner_name = "Correy"
    if Li_percent > Khan_percent and Li_percent > Correy_percent and Li_percent > OTooley_percent:
        winner_name = "Li"
    if OTooley_percent > Khan_percent and OTooley_percent > Li_percent and OTooley_percent > Correy_percent:
        winner_name = "OTooley"
    
    #print the final values for the user to see
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {vote_count}")
    print("--------------------------")
    #print a list of candidate names
    #print(candidate_list)
    print(f'Khan: {Khan_percent}% ({Khan_votes})')
    print(f'Correy: {Correy_percent}% ({Correy_votes})')
    print(f'Li: {Li_percent}% ({Li_votes})')
    print(f"O'Tooley: {OTooley_percent}% ({OTooley_votes})")
    print("--------------------------")
    print(f'Winner: {winner_name}')
    print("--------------------------")
    
    #export same results to text file
    import sys
    file = open('results.txt', 'a')
    sys.stdout = file
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {vote_count}")
    print("--------------------------")
    #print a list of candidate names
    #print(candidate_list)
    print(f'Khan: {Khan_percent}% ({Khan_votes})')
    print(f'Correy: {Correy_percent}% ({Correy_votes})')
    print(f'Li: {Li_percent}% ({Li_votes})')
    print(f"O'Tooley: {OTooley_percent}% ({OTooley_votes})")
    print("--------------------------")
    print(f'Winner: {winner_name}')
    print("--------------------------")
    file.close()
    
     