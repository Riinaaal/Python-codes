# Module 3 assignment 1

zanderSize = int(input("How long is zander in centimeters?"))

if zanderSize < 42:
    print("Release Zander back into lake as it is ", 42 - zanderSize, "centimeters under size limit.")
print()


# Module 3 assignment 2
whatCabin = input("Enter the cabin class: ")

if whatCabin == "LUX" or whatCabin == "lux":
    print("LUX: upper-deck cabin with a balcony.")
elif whatCabin == "A" or whatCabin == "a":
    print("A: above the car deck, equipped with a window.")
elif whatCabin == "B" or whatCabin == "b":
    print("B: windowless cabin above the car deck.")
elif whatCabin == "C" or whatCabin == "c":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
print()


# Module 3 assignment 3

gender = input("What is your biological gender?")
hemoglobin = int(input("What is your hemoglobin in (g/l)?"))

if gender == "Female" or gender == "female" and hemoglobin < 117:
    print("Hemoglobin is low")
elif gender == "Female" or gender == "female" and hemoglobin > 155:
    print("Hemoglobin is high")
elif gender == "Male" or gender == "male" and hemoglobin < 134:
    print("Hemoglobin is low")
elif gender == "Male" or gender == "male" and hemoglobin > 167:
    print("Hemoglobin is high")
else:
    print("Hemoglobin is normal")
print()


# Module 3 assignment 4

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")