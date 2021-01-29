#  Part A

# def sorting(*args):
#     print(f"this needs sorting: {args} ")
#     for language in args:
#         if language == "Java":
#             print("Found Java")
#             for char in language:
#                 print(char)
#         else:
#             print(f"Java was not found: {language}")

# sorting("Python", "Java")
# sorting("Python","Java","Go")
# sorting("Python", "Js", "C++")




def tax_calculation(gross_salary, tax= 0.22):
    net_salary = gross_salary * (1-tax)
    print(f"net salary: {net_salary}")
    return net_salary

def salary_limit_tester(net_salary_variable):
    if net_salary_variable >= 5800:
        print(f"Success! The salary is {net_salary_variable}")
    else:
        print(f"The Salary is under 5800: {net_salary_variable}")

net_salary_1 = tax_calculation(5000, 0.2)
salary_limit_tester(net_salary_1)

net_salary_2 = tax_calculation(6000, 0.2)
salary_limit_tester(net_salary_2)

net_salary_3 = tax_calculation(10000)
salary_limit_tester(net_salary_3)

