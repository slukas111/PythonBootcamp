dad_1_income = int(input("how much does dad 1 make a month?: "))
dad_2_income = int(input("how much does dad 2 make a month?: "))
dad_3_income = int(input("how much does dad 3 make a month?: "))

# if dad_1_income > dad_2_income and dad_1_income > dad_3_income:
#     print(f"dad 1 is the richest and makes: {dad_1_income}")
# elif dad_2_income > dad_1_income and dad_2_income > dad_3_income:
#     print(f"dad 2 is the richest and makes: {dad_2_income}")
# else:
#     print(f"dad 3 is the richest and makes: {dad_3_income}")

richest = max(dad_1_income, dad_2_income, dad_3_income)
print(f"{richest} is the most earned")

