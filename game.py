# set up s container with our choices inside, and let the AI pick one randomly
from random import randint
from gameComponents import gameVars, chooseWinner

while gameVars.player == False:
	print("=============*/ RPS GAME */==============")
	print("Computer Lives:", gameVars.ai_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("==================================")

	print("Choose your weapon! or type quit to exit\n") # /n means new line
	# give the user some weapon options
	gameVars.player = input("Pick rock, paper or scissors: \n")

	# if player chooses to quit, then exit the game
	if gameVars.player == "quit":
			print("you chose to quit")
			exit()

	# player = True -> it has a value (rock, paper or scissors)

	# computer is our AI opponent - let it make a choice
	computer = gameVars.choices[randint(0, 2)]

	# validate that the input worked
	print("Player chose " + gameVars.player)
	print("AI chose: " + computer)

	# check to see who won or if it is a tie
	if (computer == gameVars.player):
		print("tie")
		#reset the game loop and have the user choose again

	# --------- MOVE THIS CHUNK OF CODE TO A PACKAGE - START HERE

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose!")
			#take a life away from the player
			gameVars.player_lives -= 1
		else:
			print("you win!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose!")
			#take a life away from the player
			gameVars.player_lives -=1
		else:
			print("you win!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose!")
			#take a life away from the player
			gameVars.player_lives -= 1
		else:
			print("you win!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	# ---------- STOP HERE - ALL ABOVE NEEDS TO BE MOVED

	if gameVars.player_lives == 0:
		chooseWinner.winorlose("lost")
		# package - method - argument 

	if gameVars.ai_lives == 0:
		chooseWinner.winorlose("won")

	print("player lives:", gameVars.player_lives, "lives left")
	print("ai lives", gameVars.ai_lives, "lives left")

	# make the loop keep running by setting player back to False
	# unset, so that our loop condition above will evaluate to True
	gameVars.player = False
