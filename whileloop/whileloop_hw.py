ages = [5, 6, 24, 32, 21, 70]

counter = 0

while ages[counter] < 30:
    print(f"the ages is {ages[counter]}")
    counter +=1
print(f"the ages is over thirty {ages[counter]}")

counter = 0

while ages[counter] < 30:
    if ages[counter] > 20:
        print(f"the ages is stopped the loop {ages[counter]}")
        break
    counter += 1


counter = 0

while ages[counter] < 70:
    ages[counter] = ages[counter] + 2
    print(f"{ages[counter]} cell new value")

    counter += 1
else:
    print(f"{ages[counter]} something else")



# for age in ages:
#     if age >= 30:
#         print(age)

# thirty_plus = []

# for age in ages:
#     while age <= 30:
#         print(f"{age} 30 and under")
#     else:
#         print(f"{age} 30 and over")
#         # age.append(thirty_plus)
