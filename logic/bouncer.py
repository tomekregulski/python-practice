age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 21:
		print("You are good to enter and you can drink!")
	elif age >= 18:
		print("You can entger, but you need a wristband!")
	else:
		print("Sorry, you can't come in :(")
else:
	print("Please enter an age!")