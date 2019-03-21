#BRR
#MSAW


***
Later on, you may consider to amend the code, because on while part "yes" and "no" are defined, but other than those two is defined as no. Need to be changed.
***

# TODO Create an empty list to maintain the player names
roster = []


# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
team_players=input("Would you like to add players to the list? (Yes/No)")
team_players=team_players.lower()
while team_players.lower()== "yes":
	roster.append(input("What is the name of the player?  "))
	team_players=input("Would you like to add players to the list? (Yes/No)")

# TODO print the number of players on the team
print("Now there are {} players on the team".format(len(roster)))

# TODO Print the player number and the player name
# The player number should start at the number one
number_of_player=1
for player in roster:
	
	print("Number {} is {}".format(number_of_player, player))
	number_of_player+=1
	  

# TODO Select a goalkeeper from the above roster

goal_keeper_number =int(input("Please select a goal keeper from the roster. Enter the number  "))
# TODO Print the goal keeper's name
# Remember that lists use a zero based index
goal_keeper=roster[goal_keeper_number-1]
print("Great! Goal keeper for the game will be {}".format(goal_keeper))
