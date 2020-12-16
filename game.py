# set up s container with our choices inside, and let the AI pick one randomly
from random import randint
from gameComponents import gameVars, chooseWinner, comparison

while gameVars.player == False:
	print("==========/*** RPS GAME ***/==========")
	print("Computer Lives:", gameVars.ai_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("++++++++++++++++++++++++++++++++++++++")

	print("Choose your weapon! or type quit to exit\n") # /n means new line
	# give the user some weapon options
	gameVars.player = input("Pick rock, paper or scissors: \n")

	# if player chooses to quit, then exit the game
	if gameVars.player == "quit":
			print("*****you chose to quit*****")
			exit()

	# player = True -> it has a value (rock, paper or scissors)

	# computer is our AI opponent - let it make a choice
	status = gameVars.choices[randint(0, 2)]



	

	# validate that the input worked
	print("Player chose " + gameVars.player)
	
	print("AI chose: " + status)




	# here
	comparison.comparison(status)
	


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
