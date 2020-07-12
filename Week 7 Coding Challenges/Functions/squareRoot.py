#   SCRIPT: squareRoot.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Given a number N, find its square root. You need to find and print only the integral part of the square root of N.
#                For eg. if the number given is 18, answer is 4.

"""
Sample Input : 10
Sample Output : 3
"""

import math

#Function that gives the square root of a number
def squareNum(n):
    try:
        root = math.trunc(math.sqrt(int(str(n))))

    except ValueError:
        print("The inputted value is not a number! Please enter a number!")

    return root

#Receives input from the user to input a number
num = int(input("Please enter a number: "))

#Prints out the square root of the number from the user by passing in the inputted number to the squareNum function
print("The square root of a number is: {}".format(squareNum(num)))
