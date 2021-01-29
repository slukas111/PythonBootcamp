
active_employees = ["Adam", "John", "Greg", "Danna", "Ashley"]

print(f"(1) - list of current employees: {active_employees} ")
print(f"(2) - number of current employees: {len(active_employees)}")

active_employees[1] = "Jack"
print("(3) - replace employee: " + str(active_employees))

active_employees.insert(3, "Mark")
print("(4) - new hire to cell 3: " + str(active_employees))

active_employees.remove("Mark")
# print(active_employees)

active_employees.append("Mark")
print("(5) - new position for employee : " + str(active_employees))

active_employees.pop()
print("(6) - employee fired: " + str(active_employees))

active_employees.sort()
print("(7) - alphabetize employees: " + str(active_employees))