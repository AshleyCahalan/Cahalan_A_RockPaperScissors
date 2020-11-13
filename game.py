# set up s container with our choices inside, and let the AI pick one randomly
from random import randint

# an array is a datatype, acts as a container. Arrays are 0-based
# every entry in an array gets an index
choices = ["rock", "paper", "scissors"]

# computer is our AI ipponent - let it make a choice
computer = choices[randint(0, 2)]


# give the user some weapon options
my_choice = input("Pick rock, paper or scissors: ")

# validate that the input worked
print("Player chose " + my_choice)
print("AI chose: " + computer)

if (computer == player):
	print("tie")
	#reset the game loop and have the user choose again

elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose!")
		#take a life away from the player
	else:
		print("you won!")
		# take a life away from the AI

elif (computer == "paper"):
	if (player == "rock"):
		print("you lose!")
		#take a life away from the player
	else:
		print("you won!")
		# take a life away from the AI

elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose!")
		#take a life away from the player
	else:
		print("you won!")
		# take a life away from the AI