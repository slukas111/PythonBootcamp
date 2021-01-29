#practice for list homework

cars = ["Bmw", "Toyota", "Tesla", "Kia"]
print(f"Cars list:  {cars}")


second_last_value = cars[2]
negative_second_last_value = cars[-2]
print(f"second to last car:  {cars[-2]} ")
print("answer: " + second_last_value)
print("nagative answer: " + negative_second_last_value)

compare = cars[1] == "Toyota"
print("equal to: " + str(compare))
print(f"equal to f string:  {cars[1] == 'Toyota'}")

mixed_values = ["Jim", 3500, "Alex", 2.53, True]
print(mixed_values)
index_zero_three = mixed_values[0:4]
print(index_zero_three)
# print(mixed_values[6])
# print("index of 0 to 3" + str(index_zero_three))
print(cars)
cars.append("Alpha Romeo")
print(cars)
cars.insert(5,"Alpha Beta")
print(cars)