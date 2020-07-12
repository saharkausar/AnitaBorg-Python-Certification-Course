#   SCRIPT: evenOddList.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Make a single list comprehension to return two lists, one for even and another for odd numbers.

#Accepts a list of integers as input from the user
list_num = [int(m) for m in input("Please enter a list of numbers separated by a space: ").split()]

#Creates a list to store even numbers
odd_list = []

#Sorts through the list of numbers and if it is an even number, store it in the even list! If it's not even, append it to the odd list!
even_list = [x for x in list_num if x % 2 == 0 or odd_list.append(x)]

#Prints the result
print("The even numbers are: {} \nThe odd numbers are: {}".format(even_list, odd_list))
