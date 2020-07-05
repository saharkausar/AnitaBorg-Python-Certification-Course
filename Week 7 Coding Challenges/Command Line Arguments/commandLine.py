#   SCRIPT: commandLine.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Write a program using sys.Argv that would depict the name of the script, the number of the arguments used, and
#               lastly the list of the arguments used.

import sys

print("The name of the script is: ", sys.argv[0])
print("The number of arguments used is: ", len(sys.argv))
print("The list of the arguments used are: ", str(sys.argv))
