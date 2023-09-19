# Module 6 assignment 1
import random
def roll():
    roll = random.randint(1, 6 )
    return roll

diceRoll = 0
while diceRoll != 6:
    diceRoll = roll()

    if diceRoll == 6:
        break

    print(diceRoll)


# Module 6 assignment 2
import random
def roll(a,b):
    roll = random.randint(a, b)
    return roll

diceRoll = 0
howManySides = int(input("How many sided dice? "))
while diceRoll != howManySides:
    diceRoll = roll(1,howManySides)

    if diceRoll == howManySides:
        break

    print(diceRoll)


# Module 6 assignment 3
def converted(gallon):
    liter = 0
    liter = gallon * 3.78541
    return liter

convert = 0
while convert >= 0:
    convert = int(input("Enter gallons to be converted to liters: "))
    if convert < 0:
        break

    result = converted(convert)
    print(f"{convert} gallons is {result} liters")


# Module 6 assignment 4

def sumOfList(list):
    total = 0
    for i in list:
        total = i + total
    return total

numbersList = [1, 5, 6, 7, 8, 23, 56]

sumIs = sumOfList(numbersList)
print(sumIs)


# Module 6 assignment 5

def removeUneven(list):
    evenList = []
    for i in list:
        if i % 2 == 0:
            evenList.append(i)

    return evenList

numbersList = [1, 5, 6, 7, 8, 23, 56]

newList = removeUneven(numbersList)
print(numbersList)
print(newList)

# Module 6 assignment 6

import math
def pricePerSquareMeter(a,b):
    radius = (a / 2) * 0.01
    areaOfPizza = math.pi * (radius*radius)
    calculation = areaOfPizza / b
    return calculation

diameterOfFirstPizza = int(input("Enter diameter of first pizza: "))
priceOfFirstPizza = int(input("Enter price of first pizza: "))
diameterOfSecondPizza = int(input("Enter diameter of second pizza: "))
priceOfSecondPizza = int(input("Enter price of second pizza: "))

first = pricePerSquareMeter(diameterOfFirstPizza, priceOfFirstPizza)
second = pricePerSquareMeter(diameterOfSecondPizza, priceOfSecondPizza)


if first < second:
    print("First pizza provides better value for money")
else:
    print("Second pizza provides better value for money")