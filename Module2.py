# Module 2 assignment 1
name = input("Enter your name: ")
print("Hello ", name,"!")
print()


# Module 2 assignment 2
import math

radius = float(input("Enter the radius: "))
areaCircle = math.pi *radius ** 2
print("Area of the circle is {:.2f}".format(areaCircle))
print()


# Module 2 assignment 3
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))

perimeter = length * 2 + width * 2
areaOfRectangle = length * width
print("perimeter of rectangle is: ", perimeter)
print("Area of rectangle is: ", areaOfRectangle)
print()


# Module 2 assignment 4
num1 = int(input("Enter integer number one: "))
num2 = int(input("Enter integer number two: "))
num3 = int(input("Enter integer number three: "))

sum = num1 + num2 + num3
product = num1 * num2 * num3
average = (num1 + num2 + num3) / 3

print("Sum of the numbers is ", sum, "product of the numbers is ", product, "average of the numbers is ", average)
print()


# Module 2 assignment 5
talents = int(input("Enter talents:\n"))
print()
pounds = int(input("Enter pounds:\n"))
print()
lots = float(input("Enter lots:\n "))
print()

talentToPounds = talents * 20
poundToLots = (talentToPounds + pounds) * 32
lotToGrams = (poundToLots + lots) * 13.3

kilogram = lotToGrams / 1000
rndKilogram = int(kilogram)
grams = float(kilogram - rndKilogram) * 1000

print("The weight in modern units: \n", rndKilogram, "kilograms and {:.2f}".format(grams), "grams.")
print()


# Module 2 assignment 6
import random

randomList3 = random.sample(range(0, 9), 3)
print("Your 3-digit code is: ", randomList3)

randomList4 = random.sample(range(1, 6), 4)
print("Your 4-digit code is : ", randomList4)
