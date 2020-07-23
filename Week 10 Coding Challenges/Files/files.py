#   SCRIPT: files.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Read a file and print strings in the file as a list. Ensure to not count in the special characters: ! @ # $ % ^ & * ” + - ~
#                Try to use exception handling in the case that the file is not found.
#                Add the sentence “Editing the file through python scripting, wohoooo! " to the file.

"""
Input:
Use the attached file doc1.txt
"""

import os, sys
import re


try:
    os.path.isfile("doc1.txt")
    file = open("doc1.txt", "r+")

#Checks if the file exists and if the file is not found then an exception is raised
except:
    print("The specified file does not exist - Please check the file name or path!")
    sys.exit()

#If the file exists, then we execute the following
else:
    #Reads the attached file 'doc.txt'
    readFile = file.read()

    file.write("\nEditing the file through python scripting, wohoooo! ")

    #Cleans the file input to exclude any special characters from the string
    cleanFile = (re.sub(r"[^a-zA-Z0-9]+", r" ", readFile))
    #Stores each string of the cleanFile in a new list called printFile
    printFile = [x for x in cleanFile.split()]
    #Prints the file
    print(printFile)
    #Closes the file
    file.close()
