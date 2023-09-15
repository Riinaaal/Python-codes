# Module 5 assignment 1

import random

dices = []
howMany = int(input("How many dice to roll? "))

i = 0
for i in range(howMany):
    randomList = random.randint(1, 6)
    dices.append(randomList)
    i = i + 1

print("Sum of dices is ", sum(dices))


# Module 5 assignment 2

numberList = []

while numberList != "":
    uInput = input("Enter numbers (To stop enter blank)")

    if uInput == "":
        break

    numberList.append(uInput)

NumberListInteger = [int(x) for x in numberList]
sorted_numberList = sorted(NumberListInteger, reverse=True)
print(sorted_numberList[0:5])


# Module 5 assignment 3


# Module 5 assignment 4

cities = []

for i in range(5):
    uInput = input("Enter city name: ")
    cities.append(uInput)

    i = i + 1

for citie in cities:
    print(citie)