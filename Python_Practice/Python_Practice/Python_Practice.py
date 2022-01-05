print ("Hello World!!!")

skill_1 = 5 + 2 * 3
skill_2 = 8 // 5 - 3
skill_3 = 8 + 22 * 2 - 4
skill_4 = 16 - 3 / 2 + 7 - 1
skill_5 = 3**3 % 5
skill_6 = 5 + 9 * 3 / 2 - 4
print()
print ("Skill Drill #1")
print ("----------------")
print("5 + 2 * 3 = " + str(skill_1))
print("8 // 5 - 3 = " + str(skill_2))
print("8 + 22 * 2 - 4 = " + str(skill_3))
print("16 - 3 / 2 + 7 - 1 = " + str(skill_4))
print("3**3 % 5 = " + str(skill_5))
print("5 + 9 * 3 / 2 - 4 = " + str(skill_6))

skill2_1 = (5 + 2) * 3
skill2_2 = (8 // 5) - 3
skill2_3 = 8 + (22 * (2 - 4))
skill2_4 = 16 - 3 / (2 + 7) - 1
skill2_5 = 3**(3 % 5)
skill2_6a = 5 + (9 * 3 / 2 - 4)
skill2_6b = 5 + (9 * 3 / (2 - 4))

print()
print ("Skill Drill #2 - Parenthesis")
print ("----------------")
print("(5 + 2) * 3 = " + str(skill2_1))
print("(8 // 5) - 3 = " + str(skill2_2))
print("8 + (22 * (2 - 4)) = " + str(skill2_3))
print("16 - 3 / (2 + 7) - 1 = " + str(skill2_4))
print("3**(3 % 5) = " + str(skill2_5))
print("5 + (9 * 3 / 2 - 4) = " + str(skill2_6a))
print("5 + (9 * 3 / (2 - 4)) = " + str(skill2_6b))

counties = ["Arapahoe", "Denver", "Jefferson"]
print()
print ("Skill Drill #3 - Lists")
print ("----------------")
print(counties)
print(counties[0])
print("Length of Counties List = " + str(len(counties)))

print()
print ("Skill Drill #3 - Lists Manipulation")
print ("----------------")
counties.append("El Paso")
print(counties)

counties.insert(2, "El Paso")
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)

counties[2] = "El Paso"
print(counties)

counties = ["Arapahoe", "Denver", "Jefferson"]

counties[1] = "El Paso"
print(counties)

counties.pop(0)
print(counties)

counties.append("Denver")
print(counties)

counties.append("Arapahoe")
print(counties)

print()
print ("Skill Drill #4 - Tuples")
print ("----------------")

counties_tuple = ("Arapahoe","Denver","Jefferson")
print("Length of Counties Tuple = " + str(len(counties_tuple)))

print(counties_tuple[1])

print()
print ("Skill Drill #5 - Dictionary")
print ("----------------")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

print("Length of Counties Dictionary = " + str(len(counties_dict)))

print ("Dictionary List")
print(counties_dict.items())
print ("Dictionary Keys")
print(counties_dict.keys())
print ("Dictionary values")
print(counties_dict.values())

print ("Dictionary values - Denver")
print(counties_dict.get("Denver"))

print()
print ("Skill Drill #6 - List of Dictionaries")
print ("----------------")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

voting_data[1] = {"county":"El Paso", "registered_voters": 461149}
print(voting_data)

voting_data.pop(0)
print(voting_data)

voting_data.append({"county":"Denver", "registered_voters": 463353})
print(voting_data)

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

print()
print ("Skill Drill #7 - Conditional Statement")
print ("----------------")

counties = ["Arapahoe", "Denver", "Jefferson"]

if counties[1] == "Denver":
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature >= 80:
    print("Turn on the AC.")
else:
    if temperature >= 60:
        print("Open the windows.")
    else:
        if temperature <= 40:
            print("Turn on the fireplace!!!!")
        else:
            print("Don't do anything")



