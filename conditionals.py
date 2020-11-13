# set up a variable, check its value, and then do something different depending on the outcome

# cast our user input - which by default will be text - to a number using int()

temperture = int(input("input a value between 0 and 100: "))

# compare user input with some conditions
if (temperture <= 4):
	#water is frozen
	print("water is sold - frozen!")
elif (temperture < 100):
	#water is liquid
	print("liquid!")
else:
	#water is boiling (above 100 degrees)
	print("water is vapor")
