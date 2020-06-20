#   SCRIPT: printNum.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A program that takes an input as a number. This number strictly needs to be an integer as per the constraints given. The input does not accept strings and floating point numbers.
#                The program displays the digits by mathematical operations and not by iterating the number as a python string.
#               Input - Accept an integer as an input where 0 <= N <= 10000
#               Output - Print all the digits of the number from left to right.

"""
Sample Input:
1024

Sample Output:
1
0
2
4
"""

#Function that recursively prints each element vertically and mathematically
def printVert(num):
    #Base Case: If num only has one digit
    if num < 10:
        #Print the number
        print(num)
    #Recursive Step: If num has 2 or more digits
    else:
        #Remove the last digit of that number and recursively print
        printVert(num // 10)
        #Prints the last digit of num
        print(num % 10)

#Takes an integer input from the user within the range of 0 to 10000
numInput = int(input("Please enter an integer between the range of 0 to 10000: "))

print("The number you inputted is:", numInput)

#Prints the inputted integer number from left to right on a new line while also checking that the integer is within bounds
while True:
    try:
        #Checks if the inputted number is within bounds
        if (numInput < 0) or (numInput > 10000):
            #If the number is not within bounds, an error is raised!
            raise ValueError

        #Otherwise, let's print numInput vertically!
        print("Let's print" ,numInput, "vertically:")
        #Passes in 'numInput' into our 'printVert' function
        printVert(numInput)

        break

    except ValueError:
        print("The inputted number is not within bounds! Please enter an integer between 0 and 10000!")
