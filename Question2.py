import random

tail = 0
head = 0
count = 1

while count <= 100:
    choice = random.randint(1, 2)
    if choice == 1:
        tail = tail + 1
    elif choice == 2:
        head = head + 1
    count = count + 1
print("No of head is", head)
print("No of tail is", tail)
