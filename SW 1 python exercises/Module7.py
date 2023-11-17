# Module 7 assignment 1

months = ("winter", "winter", "spring", "spring", "spring","summer",
    "summer", "summer", "autumn", "autumn", "autumn", "winter")
whatMonth = int(input("Enter number of a month: "))
month = months[whatMonth-1]

print(f"Month number {whatMonth} is {month}.")


# Module 7 assignment 2

names = set()
newName = " "
while newName != "":
    newName = input("Enter name: ")

    if newName in names:
        print("Existing name")
    else:
        print("New name")

    if newName != "":
        names.add(newName)

for x in names:
    print(x)


# Module 7 assignment 3

