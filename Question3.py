import random

number = random.randint(1, 40)
count = 0
flag = 0

while count < 5:
    i = int(input("Pick a Number"))
    if i == number:
        print("You are correct")
        break
    elif i < number:
        print("Your pick is higher")
        count = count + 1
    elif i > number:
        print("Your pick is lesser")
        count = count + 1
print('The correct number is:', number)
