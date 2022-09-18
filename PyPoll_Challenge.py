# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.

# file_to_load = os.path.join(".", "Resources", "election_results.csv")
# (Resources\election_analysis.txt
file_to_load = "C:/Users/sean4/Election_Analysis/Resources/election_results.csv"
##file_to_load = "C:\Users\sean4\Election_Analysis\election_results.csv"

# Add a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = "C:/Users/sean4/Election_Analysis/Resources/election_analysis.txt"

# Initialize a total vote counter.
total_votes = 0
total_county_votes = 0
votes       = 0
total_people_votes = 0
people_votes = 0

# Candidate Options and candidate votes.
candidate_options   = []
candidate_votes     = {}
candidate_name      = []

county_name         = []
county_options      = []

# 1: Create a county list and county votes dictionary.
counties = ["Arapahoe","Denver","Jefferson"]

#county votes dictionary.
county_votes={}
# county_votes["Denver"]      = 463353
# county_votes["Jefferson"]   = 432438
# county_votes["Arapahoe"]    = 422829

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
candidate_name = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]

# Track the winning candidate, vote count and percentage
winning_candidate   = ""
winning_count       = 0
winning_percentage  = 0
vote_percentage     = 0


# 2: Track the largest county and county voter turnout.
county_vote_percentage = 0
county_winning_count = 0
county_winning_percentage = 0
winning_county = ""

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
        
        # Get the candidate name from each row.
        candidate_name  = row[2]
        
        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add to the total vote count
        total_county_votes = total_county_votes + 1
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        people_votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(people_votes) / float(total_county_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results =(
            f"{county_name}:    {county_vote_percentage:.1f}% ({people_votes:,})\n")
            # f"{candidate_name}: {vote_percentage:.1f}%     ({votes:,})\n")

         # 6e: Save the county votes to a text file.
        print(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        txt_file.write(county_results)

    # 7: Print the county with the largest turnout to the terminal.
    if (people_votes > county_winning_count) and (county_vote_percentage > county_winning_percentage):
            county_winning_count = county_votes
            winning_county = county_name
            county_winning_percentage = county_vote_percentage

    # 8: Save the county with the largest turnout to a text file.
        #Print the winning county results
    # winning_county_summary = (
    #     f"Election Results\n"
    #     f"-------------------------\n"
    #     f"Total Votes:{county_votes}\n"
    #     f"--------------------------\n"
    #     f"\n"
    #     f"County Votes:\n"

    # )
    # print(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
