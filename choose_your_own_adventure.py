# choose your own adventure

name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

print("You are on a dirt road, it has come to an end and you can go left or right.")
answer = input("Which way would you like to go? ").lower()

if answer == "left":
	print("You come to a river, you can walk around it or swim accross?")
	answer = input("Type walk to walk and swim to swim accross: ").lower()
	if answer == "swim":
		print("You swim accross and were eaten by an aliigator...")
	elif answer == "walk":
		print("You walked for many miles, ran out of water and you lost the game.")
	else:
		print("Not a valid option. You lose.")

elif answer == "right":
	print("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)?")
	answer = input("Your choice: ").lower()
	if answer == "cross":
		print("You cross the bridge and met a stranger. Do you talk them (yes/no)")
		answer = input("Your choice: ").lower()
		if answer == "yes":
			print("'You're never chased back 'After that he pointed to his left.")
			answer = input("Type your choice(left/back)").lower()
			if answer == "left":
					print("You were deceived, you were caught...")
			elif answer == "back":
					print("He told you not to go back. You were killed by unfamiliar people")
			else:
				print("Not a valid option. You lose.")
		elif answer == "no":
			print("He began to fight you, but because of your weak body, he easily removed you and threw you from the bridge...")
		else:
			print("Not a valid option. You lose.")

	elif answer == "back":
		print("You go back and You was killed...")
	else:
		print("Not a valid option. You lose.")
else:
	print("Not a valid option. You lose.")

print(f"Thank you for trying {name}")
print("See you next time...")