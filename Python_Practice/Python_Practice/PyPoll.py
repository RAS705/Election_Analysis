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

# To do: read and perform analysis.

# Read the file object with the reader function.
file_reader = csv.reader(election_data)

# Read and print the header row.
headers = next(file_reader)
print(headers)



for row in file_reader:
     print(row)

# write a line of text to the analysis file
#election_analysis.write("Hello World!!!!")

# Write three counties to the file.
#election_analysis.write("Arapahoe, Denver, Jefferson")
election_analysis.write("Counties in the Election\n")
election_analysis.write("------------------------\n")
election_analysis.write("Arapahoe\nDenver\nJefferson")

# Close the file.
election_data.close()
# Close the file.
election_analysis.close()

