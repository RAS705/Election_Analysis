x = 0
while x <= 5:
    print(x)
    x = x + 1

print()
print ("Skill Drill #1 - List of Values of Dictionaries")
print ("----------------")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

for voters in counties_dict.values():
    print(voters)

for county in counties_dict.keys():
    print(county)

for county, voters in counties_dict.items():
    print(county, voters)

print()
print ("Skill Drill #2 - List of Values of Dictionaries")
print ("----------------")

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")

# Same output but with a formatted string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Same output but with a formatted string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


print()
print ("Skill Drill #3 - List of Values of List of Dictionaries")
print ("----------------")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

print()
print ("Skill Drill #4 - List of Values of List of Dictionaries")
print ("----------------")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

print()
print ("Skill Drill #5 - Format print strings")
print ("----------------")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
