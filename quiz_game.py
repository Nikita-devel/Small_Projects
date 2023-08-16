# quiz game
Playing = input("Hello, do you want to play a quiz game? ")
if Playing.lower() != "yes":
	quit()

print("Okay, let's go!")
score = 0

answer = input("30*11=")
if answer == "330":
	print("Correct")
	score += 1
else:
	print("Incorrect")

answer = input("10*11=")
if answer == "110":
	print("Correct")
	score += 1
else:
	print("Incorrect")

answer = input("11*11=")
if answer == "121":
	print("Correct")
	score += 1
else:
	print("Incorrect")

answer = input("30*10=")
if answer == "300":
	print("Correct")
	score += 1
else:
	print("Incorrect")

print(f"You got {str(score)} question correct!")
print(f"You got {str((score / 4) * 100) } %.")
