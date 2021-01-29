#part one
windows_serial_number = "abc-def-ghi-jkl"
print(windows_serial_number)

#part two
range_of_indexes_one = windows_serial_number[0:3]
print(range_of_indexes_one)
range_of_indexes_two = windows_serial_number[4:7]
print(range_of_indexes_two)
range_of_indexes_three = windows_serial_number[8:11]
print(range_of_indexes_three)
range_of_indexes_four = windows_serial_number[12:15]
print(range_of_indexes_four)

#part three
range_of_indexes_one = range_of_indexes_one.replace("abc","aaa")
range_of_indexes_two = range_of_indexes_two.replace("def", "bbb")
range_of_indexes_three = range_of_indexes_three.replace("ghi", "ccc")
range_of_indexes_four = range_of_indexes_four.replace("jkl", "ddd")

#part four
print("Here is the output: " + range_of_indexes_one+ " " + range_of_indexes_two + 
" " + range_of_indexes_three + " " + range_of_indexes_four)

#part five
encoded_serial_number = range_of_indexes_one + "-" + range_of_indexes_two + "-" +  range_of_indexes_three + "-" + range_of_indexes_four
print("new encoded serial number: " + encoded_serial_number)

#got 100% on homework! great JOB!!