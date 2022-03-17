import random

human_number = random.randint(1, 100)
computer_guess = random.randint(1, 100)

if human_number == computer_guess:
    print("You are very good at guessing")
else:
    print("You are terrible at guessing")
print("Your number is", human_number)
print("Computer guessed", computer_guess)
