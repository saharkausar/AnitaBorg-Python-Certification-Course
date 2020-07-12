#   SCRIPT: commonNum.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Find common numbers from two lists using list comprehension.

#Accepts an inputted list of numbers from the user and stores them in a list
list_num1 = [int(m) for m in input("Please enter the first list of numbers separated by a space: ").split()]
list_num2 = [int(m) for m in input("Please enter the second list of numbers separated by a space: ").split()]

#Finds the common elements between the two lists
new_list = ([x for x in list_num1 if x in list_num2])

#Prints out the new list
print(new_list)
