joe = {'Age': 35, 'Kids': {'David': 'Boy', 'Lisa': 'Girl'}}

print(joe['Age'])
print(joe['Kids'])

print(joe['Kids']['David'])

joe_new = joe.copy()
print(joe_new)

joe.pop('Age')
print(joe)

joe['apartment_number'] = 6

print(joe)

joe.clear()
print(joe)