
def salary_calculation(salary, tax_reduction):
    salary_of_employee = salary * tax_reduction
    salary_of_employee = salary - salary_of_employee
    print(f"the salary is: {salary_of_employee}")

salary_calculation(1000, .02)