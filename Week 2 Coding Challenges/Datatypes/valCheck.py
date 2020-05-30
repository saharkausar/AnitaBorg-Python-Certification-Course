#-----------------------------------------------------------------#
#   SCRIPT: valCheck.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A Python program to check whether a specified value is contained in a group of values.
"""
Test Data:
3  -> [1,5,8,3]: True
-1 -> [1,5,8,3]: False
"""

listValue = input("Enter a list of values separated by spaces (Example: 5 7 4): ")

val = int(input("Please enter a specified value to see if it's in the list: "))

checkList = list(map(int,listValue.split()))

print("List:",checkList)

if val in checkList:
    print("The specified value", val, "was found in the list!")

else:
    print("The specified value", val, "was not found in the list!")
