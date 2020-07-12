#   SCRIPT: fibonacci.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Given a number n, generate a list of the first n fibonacci numbers, being the first number.
#                Then, apply the map function and a lambda expression to square each fibonacci number and print the list.
#                Input Format: Number N, where N= [0,20]
#                Output Format: A list on a single line which has the first N fibonacci numbers squared.

"""
Sample Input:
6

Sample Output:
[0, 1, 1, 4, 9, 25]
"""

from functools import reduce

fibNum = int(input("Please enter a number between 0 and 20 for the desired fibonacci sequence to square: "))

#Lambda function for receiving a given n fibonacci sequence
def seqFibb(n):

    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

#Executes for squaring a given n fibonacci sequence while checking that the value inputted is within bounds
while True:
    try:
        #If the input is not within bounds
        if (fibNum > 20 or fibNum < 0):
            #Then an error is raised
            raise ValueError

        #Otherwise, we pass in the input from the user 'fibNum' into our squareFibb lambda function
        list_fibb = seqFibb(fibNum)
        print("The fibonacci series for the inputted number would be: {}".format(list_fibb))

        result = list(map(lambda n: n ** 2, list_fibb))

        print("The square of each element on this list would be: {}".format(result))
        break

    except ValueError:
        print("The inputted number is not within bounds! Please enter an integer between 0 and 20!")
        break
