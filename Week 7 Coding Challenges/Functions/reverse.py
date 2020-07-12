#   SCRIPT: reverse.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
#                Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

"""
Sample Input : 1234
Sample Output : 4321
"""

#Function that reverses a given number
def reverseNum(n):
    try:
        backward = int(str(n)[::-1])

    except ValueError:
        print("The inputted value is not a number! Please enter a number!")

    return backward

#Receives input from the user to input a number
num = int(input("Please enter a number: "))

#Prints out the reversed number from the user by passing in the inputted number to the ReverseNum function
print("The number reversed is: {}".format(reverseNum(num)))
