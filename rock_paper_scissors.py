# rock/paper/scissors
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
	user_input = input("Write your choice rock/paper/scissors or Q to quit: ").lower()
	if user_input == "q":
		break

	if user_input not in options:
		continue

	random_number = random.randint(0, 2)
	# rock: 0 / paper: 1 / scissors: 3
	computer_choice = options[random_number]
	print(f"Computer picked {computer_choice}.")

	if user_input == "rock" and computer_choice == "scissors":
		print("You won!")
		user_wins += 1
	elif user_input == "paper" and computer_choice == "rock":
		print("You won!")
		user_wins += 1
	elif user_input == "scissors" and computer_choice == "paper":
		print("You won!")
		user_wins += 1
	elif user_input == computer_choice:
		print("Tie!")
	else:
		print("You lost!")
		computer_wins +=1

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Goodbye!")

# Hi, I'm Nikita. I am from a small town in Ukraine. Eventually moving to France began
# in-depth study programming and even more in-depth backend development. At the moment I am 16 years old, I am engaged
# sports and actively participate in international handball competitions.
# The purpose of creating this account is the accumulation of my work for the future and also. would be to hear the opinions of others to improve their skills.
# Good viewing and thanks for the thoughtful criticism!