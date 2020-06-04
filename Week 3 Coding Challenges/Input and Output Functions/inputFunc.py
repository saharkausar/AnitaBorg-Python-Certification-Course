#   SCRIPT: inputFunc.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Write a program to input your name and your marks in 3 subjects. Display the marks with your name as shown in the sample output. Do not use more than 2 input statements in your program.

"""
Sample Input:
Enter your name: Anita
Enter your marks: 80,70,60
Sample Output: Anita, your marks are [80,70,60]
Make sure you display messages as shown above.
"""

enterName = input("Enter your name: ")

enterMarks = [int(m) for m in input("Enter your marks in 3 subjects separated by a space: ").split()]

print("{}, your marks are {}".format(enterName, enterMarks))
