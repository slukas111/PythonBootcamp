
building_attendents = {'Floor_one': {'first_apartment': 'Rachel', 'second_apartment': 'Jeen'},
                       'Floor_two': {'third_apartment': 'Jack'}}

ba = building_attendents
print(ba)

print("First Floor Attendants: ", ba['Floor_one'])
print("Occupant of Second Apartment: ", ba['Floor_one']['second_apartment'])

ba['Floor_two']['fourth_apartment'] = 'Carroll'
print("added a new attendant in floor 2, fourth aparment", ba)


ba['Floor_one'].pop("first_apartment")
print("removed the first apartment", ba)
# del ba['Floor_one']['first_apartment']
# print(ba)
