#connection to election results file
from ast import With
from importlib import resources
from importlib.resources import Resource
import datetime

import csv
from wsgiref import headers
dir(csv)
import os
import csv
#KEEP CODE

file_to_load='C:/Users/sean4/Election_Analysis/Resources/election_results.csv'

file_to_save='C:/Users/sean4/Election_Analysis/Resources/election_analysis.txt'

#1. Initialize a total vote counter.
total_votes = 0

#Candidate options and candidate votes
candidate_options = []

#Declare an empty dictionary
candidate_votes={}

#open election results and read the file

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

        #Read the Header Row
    headers = next(file_reader)

#Printing each row into the CSV file
    for row in file_reader:
        total_votes += 1

#printing the candidate name in each row
        candidate_name = row[2]

        if  candidate_name not in candidate_options:

#adding candidate name to the list
            candidate_options.append(candidate_name)

#Begin tracking each candidates vote count
            candidate_votes[candidate_name] = 0

#INcrement the vote counts
            candidate_votes[candidate_name] +=1

#Iterate through the candidate list
for candidate_name in candidate_votes:

    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    #3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if(votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    #4. Print the candidate name and % of votes
        #print(f"{candidate_name}:   Received {vote_percentage:.2f} % of the vote.")

winning_candidate_summary = (
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count:   {winning_count:,}\n"
    f"Winning Percentage:   {winning_percentage:.1f}%\n"
    f"--------------------------------\n"
)

print(winning_candidate_summary)

#3. Print the total votes
print(candidate_votes)


