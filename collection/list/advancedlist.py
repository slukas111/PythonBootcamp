numbers_list = [0.5, 13, 56, 20, 1]
print(len(numbers_list))
print("original list: " + str(numbers_list))
numbers_list[1] = 10
print("new num list: " + str(numbers_list))

numbers_list.append(15)
print("add a new value append: " + str(numbers_list))

numbers_list.insert(2, 1005)
print("add a specific position: " + str(numbers_list))

numbers_list.remove(1005)
print("remove from list: " + str(numbers_list))

numbers_list.pop()
print("remove last of the list: " +str(numbers_list))

numbers_list.pop(0)
print("remove by cell position: " + str(numbers_list))