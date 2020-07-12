#   SCRIPT: findEven.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Find even numbers from a list of lists of integers. Clue: Use nested list comprehension!

#Accepts a list of integers as input from the user
list_num1 = [int(m) for m in input("Please enter the first list of numbers separated by a space: ").split()]
list_num2 = [int(m) for m in input("Please enter the second list of numbers separated by a space: ").split()]
list_num3 = [int(m) for m in input("Please enter the third list of numbers separated by a space: ").split()]

#Stores all the inputted lists into a list of lists!
lists_all = [list_num1, list_num2, list_num3]

#Let's print out the list of lists for reference
print("The list of list of integers are: {}".format(lists_all))

#Nested list that searches for an even x element in a list for each list in list all
even_list = [[x for x in list if x % 2 == 0] for list in lists_all]

#Prints out the even integer lists found
print("The even integers found are: {}".format(even_list))
