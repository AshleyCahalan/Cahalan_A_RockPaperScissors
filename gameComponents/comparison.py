from gameComponents import gameVars
from game import computer

def comparison(status):

	# check to see who won or if it is a tie
	if (computer == gameVars.player):
		print("well well, it's a tie")
		#reset the game loop and have the user choose again

	# move code
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
	# end of moving code



