#   SCRIPT: tempConv.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
#                Formula for conversion: (C × 9/5) + 32 = F
#                Where C is temperature in Celsius and F is temperature in Fahrenheit.

"""
Sample Input 1: 100
Sample Output 1: 212
Sample Input 2: 90
Sample Output 2: 194
"""

celsTemp = float(input("Please enter a temperature in Celsius: "))

farTemp = ((celsTemp * (9/5)) + 32)

print("{} degrees Celsius is equal to {} degrees Fahrenheit".format(celsTemp, farTemp))
