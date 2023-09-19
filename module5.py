# Module 5 assignment 1

import random

dices = []
howMany = int(input("How many dice to roll? "))

for x in range(howMany):
    randomList = random.randint(1, 6)
    dices.append(randomList)

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

number = int(input("Enter number: "))

fulfills = 0
for x in range(number):
    if x != 0 and number % x == 0 and x != number:
        fulfills = fulfills + 1

if fulfills == 1 and number != 1:
    print("Its a prime number")
else:
    print("Its not a prime number")


# Module 5 assignment 4

cities = []

for x in range(5):
    uInput = input("Enter city name: ")
    cities.append(uInput)

for citie in cities:
    print(citie)