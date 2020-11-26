# set up s container with our choices inside, and let the AI pick one randomly
from random import randint

# an array is a datatype, acts as a container. Arrays are 0-based
# every entry in an array gets an index
choices = ["rock", "paper", "scissors"]


player_lives = 5
ai_lives = 5

total_lives = 5

# True and False are Boolean data types -> they are the equivalent of on or off, 1 or 0
player = False

while player == False:
	# give the user some weapon options
	player = input("Pick rock, paper or scissors: ")

	# player = True -> it has a value (rock, paper or scissors)

	# computer is our AI opponent - let it make a choice
	computer = choices[randint(0, 2)]

	# validate that the input worked
	print("Player chose " + player)
	print("AI chose: " + computer)

	# check to see who won or if it is a tie
	if (computer == player):
		print("tie")
		#reset the game loop and have the user choose again

	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!")
			#take a life away from the player
			player_lives -= 1
		else:
			print("you won!")
			# take a life away from the AI
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			#take a life away from the player
			player_lives -=1
		else:
			print("you won!")
			# take a life away from the AI
			ai_lives -= 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			#take a life away from the player
			player_lives -= 1
		else:
			print("you won!")
			# take a life away from the AI
			ai_lives -= 1

	print("player lives:", player_lives, "lives left")
	print("ai lives", ai_lives, "lives left")

	# make the loop keep running by setting player back to False
	# unset, so that our loop condition above will evaluate to True
	player = False
