
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
