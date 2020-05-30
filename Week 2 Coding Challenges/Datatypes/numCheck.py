#-----------------------------------------------------------------#
#   SCRIPT: numCheck.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Write a Python program to test whether a number is within 100 of 1000 or 2000

num = int(input("Please enter a number: "))

if 900 <= num <= 1100:
    print("The number you entered is within 100 of 1000")

elif 1900 <= num <= 2100:
    print("The number you entered is within 100 of 2000")

else:
    print("The number you entered is not within 100 of either 1000 or 2000")
