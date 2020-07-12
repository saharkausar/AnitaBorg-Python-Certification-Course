#   SCRIPT: computePerf.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Compute the performance of list comprehension vs. a for loop.
#                Write two functions and use the Python time module to measure their execution time.

import time

#Code for testing list comprehension
start_comp = time.time()

list_comp = [i for i in range (1450000)]

final_comp = (time.time() - start_comp)

#Code for testing for loop
start_loop = time.time()

list_loop = []

for m in range(1450000):
    list_loop.append(m)

final_loop = (time.time() - start_loop)

#Prints the result
print("The time taken to execute creating a list using list comprehension was {} hs while it was {} hs for a for loop!".format(final_comp, final_loop))
print("It is quicker to create a list using list comprehension than a for loop!")
