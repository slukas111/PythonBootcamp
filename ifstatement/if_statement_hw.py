employees = {"Jack": 6,
            "Russel": 10,
            "Keren": 2}
print(f"(1) - dictionary of employees: {employees}")


for worker, value in employees.items():
    # print(worker, value)

    if value >= 5 and value <= 8:
        print(f"(2)- this guy can work: {worker, value}")

if value == 2 or value == 4:
    print(f"(3)- this employee for weekend shift: {worker, value}")
else:
    print("default exit point")