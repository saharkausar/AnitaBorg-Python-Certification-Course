#   SCRIPT: rightTriangle.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Anna likes to draw right angled triangles. She recently learnt how to code in Python, and she is curious to see if it can be used to print the same.
#               You need to help her out by writing a program which takes an input number n from the user and prints a right angled triangle of height n. Anna also wants that the triangle should display the respective line numbers if the line number is odd (1st, 3rd, 5th… line), and censor out the even numbered lines (2nd, 4th, 6th… line) using the hash (‘#’) symbol.
#               Note: 1 ≤ n ≤ 10

"""
Sample Input: 5

Sample Output:
    1
   ##
  333
 ####
55555
"""

triHeight = int(input("Please enter a number between 1 and 10 for the desired height of the triangle: "))

#Function for printing the specialized right triangle
def rightTriangle(height):
    for row in range(1, height + 1):
        for col in range(1, height + 1):
            if (col <= height - row):
                print(' ', end = "")
            else:
                #if a row is on an odd lined number (1st, 3rd, 5th...), then print that number
                    if (row % 2) != 0:
                        print(row, end = "")

                #if a row is on an even lined number (2nd, 4th, 6th...), then print the hash ('#') symbol
                    else:
                        print("#", end = "")
        print()

#Executes for printing a right triangle while checking that the value inputted is within bounds
while True:
    try:
        #If the input is not within bounds
        if (triHeight > 10 or triHeight < 0):
            #Then an error is raised
            raise ValueError

        #Otherwise, we pass in the input from the user 'triHeight' into our rightTriangle function
        rightTriangle(triHeight)
        break

    except ValueError:
        print("The inputted number is not within bounds! Please enter an integer between 1 and 10!")
        break
