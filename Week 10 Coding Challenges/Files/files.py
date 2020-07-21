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


try:
    os.path.isfile("doc1.txt")
    file = open("doc1.txt", "r")

#Checks if the file exists and if the file is not found then an exception is raised
except:
    print("The specified file does not exist - Please check the file name or path!")
    sys.exit()

#If the file exists, then we execute the following
else:
    #Reads the attached file 'doc.txt'
    readFile = file.read()

    with open("doc1.txt", "a") as file:
        file.write("\nEditing the file through python scripting, wohoooo! ")

    #Prints the strings in the file as a list but excludes the special characters
    printFile = [x for x in readFile.split() if x.isalnum()]
    print(printFile)
    file.close()
