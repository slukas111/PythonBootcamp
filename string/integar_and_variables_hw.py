#integar and float homework

gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = float(400.5)
salary_tax = 0.2
donation_to_the_poor = 0.1

print(f"gross salary: {gross_salary}")

# Calculate net salary
tax = gross_salary * salary_tax
net_salary = gross_salary - tax

print(f"net salary after taxes: {net_salary} and deducted tax: {tax}")

disposable_income = net_salary - health_insurance - rent - food


print(f"amount after living expenses: {disposable_income}")

donation = disposable_income * donation_to_the_poor

# #make 2 demical places
print(donation)
print(f"the amount donated to poor this month: {donation:.2f} out of {net_salary:.2f}")
print(round(donation, 2))