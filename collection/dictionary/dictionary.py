# dictionary_example = {'name': 'Rachel', 'test_grade': 98}

# print(dictionary_example['name'])
# print(dictionary_example['test_grade'])
# print(dictionary_example.get('name'))

new_employee = {'first_name': 'David', 'salary': 10000, 'company': 'Google'}
#print dictionary
print("print the dictionary: " + str(new_employee))

# get value 
print("get value of first key: " +str(new_employee['first_name']))
print("get the second way: " + str(new_employee.get('salary')))

new_employee.pop('salary')
print(new_employee)

print(new_employee.keys())
print(new_employee.values())

job_title_value = "Developer"

new_dictionary = {"job_title": job_title_value}

print("print the new dictionary" + str(new_dictionary))