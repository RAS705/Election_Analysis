# The data we need to retrieve
#
#
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
#
#


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the csv module.
import csv
print(dir(csv))

# Import the os module.
import os
print(dir(os))


# Check of data types

print()
print ("Check out Int data type")
print ("----------------")
print(dir(int))

print()
print ("Check out Float data type")
print ("----------------")
print(dir(float))

print()
print ("Check out Bool data type")
print ("----------------")
print(dir(bool))

print()
print ("Check out List data type")
print ("----------------")
print(dir(list))

print()
print ("Check out Tuple data type")
print ("----------------")
print(dir(tuple))

print()
print ("Check out Dict data type")
print ("----------------")
print(dir(dict))

print()
print ("Check out DateTime data type")
print ("----------------")
print(dir(dt.datetime))

print()
print ("Check out Random module")
print ("----------------")
# Import the random module.
import random as rd
print(dir(rd))

print()
print ("Check out Numpy module")
print ("----------------")
# Import the random module.
import numpy as np
print(dir(np))



# Assign a variable for the file to load and the path.
file_to_load = '..\..\Resources\election_results.csv'
# file_to_load = 'Resources\election_results.csv'
#file_to_load = os.path.join("Resoures", "election_results.csv")

# Open the election results and read the file.
election_data = open(file_to_load, 'r')
print(election_data)

# Assign a variable for the file to write output to.
file_to_save = '..\..\Analysis\election_analysis.txt'

# Open the election analysis and read the file.
election_analysis = open(file_to_save, 'w')
print(election_analysis)


# declare list of candidates
candidates_options = []

# declare candidates votes dictionary
candidates_votes = {}

# 1. Initialize a total vote counter.
total_votes = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# To do: read and perform analysis.

# Read the file object with the reader function.
file_reader = csv.reader(election_data)

# Read and print the header row.
headers = next(file_reader)
print(headers)



for row in file_reader:
     # 2. Add to the total vote count.
     total_votes += 1
     
     # Print the candidate name from each row.
     candidate_name = row[2]

     if candidate_name not in candidates_options:
        # Add the candidate name to the candidate list.
        candidates_options.append(candidate_name)
        # Add the candidate name to the candidate vote dictionary
        candidates_votes[candidate_name] = 0
     
     # Increment candidate vote dictionary
     candidates_votes[candidate_name] += 1

# 3. Print the total votes.
print(total_votes)

# Print the candidate votes.
print(candidates_votes)


# Print the list of candidates.
print(candidates_options)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidates_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidates_votes[candidate_name]

    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")


print()

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# write a line of text to the analysis file
#election_analysis.write("Hello World!!!!")

# Write three counties to the file.
#election_analysis.write("Arapahoe, Denver, Jefferson")
election_analysis.write("Counties in the Election\n")
election_analysis.write("------------------------\n")
election_analysis.write("Arapahoe\nDenver\nJefferson")

# Print the final vote count to the terminal.
election_results = (
        f"\n\n\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

print(election_results, end="")
# Save the final vote count to the text file.
election_analysis.write(election_results)

for candidate_name in candidates_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidates_votes[candidate_name]

    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # 4b. Print the candidate name and percentage of votes to the analysis report
    election_analysis.write(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,}).\n")

# Save the winner to the text file.
election_analysis.write("\n\n\n")
election_analysis.write(winning_candidate_summary)

# Close the file.
election_data.close()
# Close the file.
election_analysis.close()

