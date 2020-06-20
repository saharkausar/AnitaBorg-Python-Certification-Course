#   SCRIPT: findOddNum.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Input a list of numbers “num_list”. All numbers in the list occur even times expect one number which occurs odd number of
#                times. Find the number that occurs odd number of time in O(1) space complexity and O(n) time complexity.
#                Note: Use Bitwise operator.
"""
Sample Input:
1 2 2 5 5 1 3 9 3 9 6 4 4

Sample Output:
6

Explanation:
The number 6 occurs 1 time(odd).
"""

#Initializes an empty list
num_list = []

#Takes in a list of numbers as an input from the user and stores this as 'num_list'
num_list = [int(num) for num in input("Please enter a list of numbers separated by spaces: ").split()]

print("Inputted List:", num_list)

#Function that finds the element that occurs an odd number of times using a bitwise XOR
def findOdd(ls):
    #Initializes the number count to 0
    num = 0

    #Loops through each element in the passed in list
    for element in ls:
        #Bitwise XOR: (1 ^ 1 = 0 | 1 ^ 0 = 1 | 0 ^ 1 = 1 | 0 ^ 0 = 0)
        #Cancels out the even occurring elements
        num = num ^ element

    #Returns the final result (the odd occurring element)
    return num

print("The number that occurs an odd number of times in the list is:", findOdd(num_list))
