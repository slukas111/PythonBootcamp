alex = {"Age": 32, "Married": "Yes", "Kids": 3}
print("(1)- this is the dictionary: ", alex)

#extract the values of dictionary
age = alex["Age"]
status = alex["Married"]
dependents = alex["Kids"]

print(age)
print(status)
print(dependents)

# print("print the value of age: " + str(alex["Age"]))
# print("print the value of status: " + str(alex["Married"]))
# print("print the value of kids: " + str(alex.get('Kids')))

#change dictionary value 

up_alex = {"Age": 28}

alex.update(up_alex)

print("diction after update", alex)

up_alex = {"Kids": 4}
alex.update(up_alex)
print("child was born: ", alex)

#print all the keys of alex
print("the keys of alex ", alex.keys())
#print all the values
print("all the values ", alex.values())