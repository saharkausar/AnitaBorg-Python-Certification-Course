#   SCRIPT: sunday.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A Python program that prints the date of all the Sundays of a specified year.
#                The user should be able to input a year and get all the dates which were a Sunday.

"""
Sample Input: 2020
Sample Output:
2020-01-05
2020-01-12
2020-01-19
2020-01-26
2020-02-02
-----
2020-12-06
2020-12-13
2020-12-20
2020-12-27
"""

#Imports the module
from datetime import date, timedelta

#Function that prints out all the Sundays in a given year
def sundayDate(year):

    #Start the counter on January 1st of a year (year, month, day) where year is a value passed in from the user input (yearInput)
    initial = date(year, 1, 1)

    #Ends the counter on December 31st of a year (year, month, day) where year is a value passed in from the user input (yearInput)
    end = date(year, 12, 31)

    #For each day of the year
    for x in range((end - initial).days + 1):
        #If a day of the week is a Sunday (6 is Sunday for date.weekday())
        if (initial + timedelta(days = x)).weekday() == 6:
            #Prints out all the Sundays
            print(initial + timedelta(days = x))

#Prompts the user to input a year to receive the Sundays within a given year and stores that value in yearInput
yearInput = int(input("Please enter a year to receive all of the corresponding Sundays within that year: "))

#Passes the input from the user into the sundayDate function
sundayDate(yearInput)
