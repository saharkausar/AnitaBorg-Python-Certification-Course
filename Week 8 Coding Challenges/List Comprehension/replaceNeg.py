#   SCRIPT: replaceNeg.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Input a list of integers containing both positive and negative numbers.
#                You have to print a list in which all the negative integers of this list are replaced by their
#                squares and all the positive numbers are left as it is.
#                Note: This problem can also be done without using list comprehension but since this is a
#                challenge on List Comprehension, you need to complete this using a single list comprehension statement.

"""
Sample Input1:
2 -3 4 5 -1

Sample Output1:
[2, 9, 4, 5, 1]
"""

#Accepts a list of numbers from the user and stores them in a list
enterInput = [int(m) for m in input("Please enter a list of integers separated by a space: ").split()]

#Squares the numbers if they are negative from the inputted list
new_list = [m**2 if m < 0 else m for m in enterInput]

#Prints out the new list
print(new_list)
