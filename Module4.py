# Module 4 assignment 1

for i in range(1, 1000):
    if i % 3 == 0:
        print(i)
print()


# Module 4 assignment 2

inches = 0
while inches >= 0:
    inches = int(input("Enter inches (Negative values will end program)"))
    if inches < 0:
        break
    print(inches, "is in centimeters ", inches*2.54)
print()


# Module 4 assignment 3

numbers = []
while numbers != "":
    uInput = input("Enter number ")
    if uInput == "":
        break
    numbers.append(uInput)

numbers.sort()

print("Smallest number is: ", numbers[0])
print("Largest number is: ", numbers[-1])


# Module 4 assignment 4

import random

number = random.randint(0,10)
guess = 0

while guess != number:
    guess = int(input("Guess the number"))

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct")


# Module 4 assignment 5

i = 0
while i < 5:
    correctUsername = "phyton"
    correctPassword = "rules"

    username = input("Enter username ")
    password = input("Enter password ")

    if username == correctUsername and password == correctPassword:
        print("Welcome")
        break

    i = i + 1

    if i == 5:
        print("Access denied")

# Module 4 assignment 6

