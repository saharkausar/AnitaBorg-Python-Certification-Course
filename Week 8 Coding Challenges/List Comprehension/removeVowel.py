#   SCRIPT: removeVowel.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Take a string as an input and return a string with vowels removed.

#Accepts an inputted string from the user and stores them in a list
enterInput = [char for char in input("Please enter a sentence: ")]

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

#Removes the vowels from the inputted list
new_list = ''.join([x for x in enterInput if x not in vowels])

#Prints out the new list
print(new_list)
