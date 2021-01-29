drink_set = {"Cola", "Sprite", "Beer", "Water", "Soda"}

print(f"current drinks offered: {drink_set}")

drink_set.add("Soda")
print(f"with soda added: {drink_set}")
drink_set.remove("Soda")

print(f"drink soda deleted: {drink_set}")

drinks_2 = drink_set.copy()

print(f"copy of drink order: {drinks_2}")

print("how many items checkout 1: " + str(len(drink_set)))
print("how many items checkout 2: " + str(len(drinks_2)))
num_count = len(drink_set)
print(f"here is f string version: {len(drink_set)}")
# print("how many items checkout 2: " + num_count)