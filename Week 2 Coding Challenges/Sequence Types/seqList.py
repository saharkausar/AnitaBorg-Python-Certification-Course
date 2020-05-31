#   SCRIPT: seqList.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A python program that calculates how many unique elements are in a certain list, prints its odd elements, and replaces a string with its corresponding
#               numerical value while storing the string it replaces in its own list.

L1 = [2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
str1 = "hello python three"

#Function that calculates the number of unique elements in a list
def calcListEl(ls):
    x = []
    for a in ls:
        if a not in x:
            x.append(a)
    return x

#Stores the unique elements of L1 in a new list
newList = calcListEl(L1)

#Function that prints odd elements in the List
def oddNum(ls):
    for num in newList:
        if num % 2 != 0:
            print(num, end = " ")

#Prints out our original list for reference
print("List L1:", L1)

#Prints out the elements that are both unique and odd in List L1 by passing in our newList to the oddNum function for reference
print("Unique and odd elements in List L1:", end = " ")
oddNum(newList)

#Prints the original string for our reference
print(sep="\n")
print("Original string:", str1)

#Replaces "three" in string str1 with "3" and saves it to a new string repStr
repStr = str1.replace("three","3")
print("New python string:", repStr)

#Function that saves all words in a list where the characters of the list are all capitalized
def lowToUpper(ls):
    #Takes in a list of lowercase input
    lowerList = []
    #converts the elements to uppercase
    upperList = [x.upper() for x in repStr]
    print(upperList)

#Passes in our new string repStr into the lowToUpper function to capitalize each character
newString = lowToUpper(repStr)

"""
Tuples are immutable which means that once we declare the contents of a tuple, we are unable to modify the contents of that tuple as opposed to a list.
The values can not change in a tuple!
"""

#Function that converts a list into a tuple
def change(list):
    return tuple(list)

#Let's convert L1 into a tuple for testing purposes!
tupleL1 = change(L1)
print("L1 is now a tuple:", tupleL1)

"""
Let's prove that tuples are immutable by trying to add or remove an element from tupleL1!
tupleL1.append(10)
tupleL1.remove(9)

We receive the errors in the console as the following: AttributeError: 'tuple' object has no attribute 'remove'
However, we are able to run the following if we wish on our original list:

L1.append(10)
L1.remove(9)

This works because lists are mutable whereas tuples are immutable!
"""
