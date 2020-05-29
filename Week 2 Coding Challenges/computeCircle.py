#-----------------------------------------------------------------#
#   SCRIPT: computeCircle.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A Python program which accepts the radius of a circle from the user and computes the area of the circle.
#
import math

rad = int(input("Please enter the desired radius for a circle: "))

area = (math.pi * ((pow(rad,2))))

print("The radius of the circle is: ", rad, "\nThe area of the circle is: ", area)
