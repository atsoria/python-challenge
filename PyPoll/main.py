#Import to get the pathways correct
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
outputpath = os.path.join('Analysis', 'results.txt')
# Store the header
csv_header = None
with open(csvpath,"r") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

#Variables
    
    total_votes = 0
    votes_dictionary = {}
    for row in csvreader:
        #Find total votes
        total_votes += 1 
        #Find candidates names
        candidate = row[2]
        #Add candidate to dictionary and add vote count
        if candidate in votes_dictionary:
            votes_dictionary[candidate] = votes_dictionary[candidate]+1 
        else:
            votes_dictionary[candidate] = 1


output = "Election Results\n"
output += "----------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += "----------------------------\n"
winner = ""
winner_votes = 0
#Find results for each candidate
for candidate2 in votes_dictionary:
    the_votes = votes_dictionary[candidate2]
    output += f"{candidate2}: {100*(the_votes/total_votes):.3f}% ({the_votes})\n"
    #Find the winner
    if the_votes > winner_votes:
        winner = candidate2
        winner_votes = the_votes
output += "----------------------------\n"
output += f"Winner: {winner} \n"
output += "----------------------------\n"
#print results
print(output)
#write to text file
with open(outputpath, "w") as txtfile:
    txtfile.write(output)