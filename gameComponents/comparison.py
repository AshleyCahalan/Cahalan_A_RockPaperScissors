from gameComponents import gameVars
#from game import computer

def comparison(status):

	

	# check to see who won or if it is a tie
	if (status == gameVars.player):
		print("well well, it's a tie")
		#reset the game loop and have the user choose again
	# move code
	elif (status == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose!")
			#take a life away from the player
			gameVars.player_lives -= 1
		else:
			print("you win!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	elif (status == "paper"):
		if (gameVars.player == "rock"):
			print("you lose!")
			#take a life away from the player
			gameVars.player_lives -=1
		else:
			print("you win!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	elif (status == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose!")
			#take a life away from the player
			gameVars.player_lives -= 1
		else:
			print("you win!")
			# take a life away from the AI
			gameVars.ai_lives -= 1
	# end of moving code



