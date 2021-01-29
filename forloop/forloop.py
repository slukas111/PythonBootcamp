# for x in range(6):
#     print(x)

# print()

# for x in range(3, 7):
#     print(x)

# print()

# for x in range(3, 12, 3):
#     print(x)

# print()

salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

for place in range(0, 9, 3):
    if place == 0:
        pass
    else:
        salary_w_bonus = salaries[place] + place * 1000
        print(salary_w_bonus)