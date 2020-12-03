from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	print("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice =="n":
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice == "Y" or choice =="y":
		# reset he player lives and the AI loves
		# and set player to False so that our loop will restart

		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False

	else:
		print("Make a valid choice - Y or N ")
		# this will generate a bug that we need to fix later
		choice = input("Y or N: ")