# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

"""
Assignment: Strings
part 1
"""
# Variables for every player that scored
scorer_name_1 = "Ruud Gullit"
scorer_name_2 = "Marco van Basten"

# Variables for each time that a goal was scored
goal_0 = 32
goal_1 = 54

# Variables to report who scored when
# scorer_name_and_time_1 = scorer_name_1 + " " + str(goal_0)
# scorer_name_and_time_2 = scorer_name_2 + " " + str(goal_1)

# Variable to store the result
scorers = scorer_name_1 + " " + str(goal_0) + ", " + scorer_name_2 + " " + str(goal_1)

print(scorers)

# Variables to report Who scored when in a sentence using f-strings
# report_scorer_and_time_1 = f"{scorer_name_1} scored in the {goal_0}nd minute"
# report_scorer_and_time_2 = f"{scorer_name_2} scored in the {goal_1}th minute"

# Variable to store the report
report = f"{scorer_name_1} scored in the {goal_0}nd minute" + "\n" + f"{scorer_name_2} scored in the {goal_1}th minute"

print(report)


"""
Assignment: Strings
Part 2
"""

# Variable for the player's name
player = "Ronald Koeman"

# Finding the space between first and last name of the player
space_first_last_name = player.find(" ")

# Slicing the first name
first_name = player[:space_first_last_name]
# Length of the first name
first_name_len = len(first_name)

print(first_name)
print(first_name_len)

# Slicing the last name
last_name = player[space_first_last_name + 1:]
# Length of the last name
last_name_len = len(last_name)

print(last_name)
print(last_name_len)

# Indexing the first letter of the first name
first_letter_fisrt_name = first_name[0]
# Using the first letter of the first name with whole last name
name_short = first_letter_fisrt_name + ". " + last_name

print(name_short)

# Chanting by the crowd
chant = ((first_name + "! ") * first_name_len).strip()

print(chant)

# Indexing the last character in chant to make sure it is not a space
good_chant = chant[-1] != " "
good_chant_alternative = chant[-1] == "!"

print(good_chant)
print(good_chant_alternative)

