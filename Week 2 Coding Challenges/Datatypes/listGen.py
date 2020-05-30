#-----------------------------------------------------------------#
#   SCRIPT: listGen.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
"""
Sample data: 3, 5, 7, 23

Output:
List: ['3, '5', '7', '23']
Tuple: ('3, '5', '7', '23')

"""

gen = input("Sample sequence: 3,5,7,23 \nPlease enter a desired sequence of comma-separated numbers: ")

genList = gen.split(",")

genTuple = tuple(genList)

print("Output: \nList:",genList,"\nTuple:",genTuple)
