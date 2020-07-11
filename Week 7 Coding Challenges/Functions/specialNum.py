#   SCRIPT: specialNum.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Input a number x. Find whether the number is a special number or not.
#                A special number is a number composed of only prime digits.
#                Print "True" if x is a special number and "False" if otherwise.

"""
Sample Input 1: 37534

Sample Output 1: False

Sample Input 2: 3555

Sample Output 2: True
"""

#Accepts an number as an input from the user
num = input("Please input a number x: ")

#Function that checks if an inputted number is a special number (comprised of only prime digits)
def primeCheck(n):

    #Stores inputted string as integer digits into an array
    array = [int(i) for i in num]

    #Loops through the array
    for i in array:
        #Checks if the number is composite
        if i == 4 or i == 6 or i == 8 or i == 9:
            #If any digit is found to be composite, return false
            return 0
    #If only prime digits are found, return true
    return 1

if (primeCheck(num)):
    print("True")
else:
    print("False")
