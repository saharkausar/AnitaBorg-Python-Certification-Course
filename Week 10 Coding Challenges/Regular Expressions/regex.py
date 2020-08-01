#   SCRIPT: regex.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Utilize various expressions (found below) to answer various questions on the topic of regular expressions!

"""
Question 1:

Sample String:
textStr = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"

Q1: Extract email extension from the above string using re.findall
[output should be 'ab.etc']
"""

#Imports the regex module
import re
#Sample string
textStr = "From john.doe@ab.etc"
#a (starts at a), \w (any alphanumeric character), \D* (any nondigit character with 0 or more occurrences)
#result = re.findall(r'a\w\D*', textStr)
#Changing the approach so that if the string is changed then the same structured output can be printed
result = re.findall(r'@(\S+)', textStr)
#Prints the result to return 'ab.etc'
print(result)

"""
Question 2:

Sample String:
textStr = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"

Q2: Extract email from the above string using re.findall
[output should be 'john.doe@ab.etc']
"""

#Using the same import module and textStr from question one - Now let's extract the email!
#email = re.findall(r'j\w\D*', textStr)
#Changing the approach so that if the string is changed then the same structured output can be printed
email = re.findall(r'\S+?@\S+', textStr)
#Prints the result to return 'john.doe@ab.etc'
print(email)

"""
Question 3:

x = 'From: Using the : character'
Q3: Extract 'From: Using the :' from the above string x. [Use re.findall]
"""

#Sample string
x = 'From: Using the : character'
#F (starts with F), \w* (any alphanumeric) character with one or more occurrences, \W (any nonalphanumeric character), \s (non-whitespace) and so forth
#extract = re.findall(r'F\w*\W\s\w*\s\w*\s\W', x)

#Changing the approach so that if the string is changed then the same structured output can be printed
extract = re.findall(r'\S+:\s\S+\s\S+\s:', x)
#Prints the result
print(extract)

"""
Question 4:

MathScores = '''
Ann got 99 and Maria got 95,
David got 84 and Jose got 21
'''
Q4: Print out the dictionary of name and scores from the above string "MathScores" above.

[Output should be - {'Ann': '99', 'Maria': '95', 'David': '84', 'Jose': '21'}]
"""

#Sample String
MathScores = "Ann got 99 and Maria got 95, David got 84 and Jose got 21"

#Finds the keys and values while setting the leys and values for our dictionary
#names_list = [re.findall(r'A\w*', MathScores)[0], re.findall(r'M\w*', MathScores)[0], re.findall(r'D\w*', MathScores)[0], re.findall(r'J\w*', MathScores)[0]]
#Changing the approach so that if the names in the string changed then the same structured output can be printed
names_list = [re.findall(r'\S+', MathScores)[0], re.findall(r'\S+\s\S+\s\S+\s\S+\s(\S+)', MathScores)[0], re.findall(r'\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s(\S+)', MathScores)[0], re.findall(r'\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s\S+\s(\S+)', MathScores)[0]]
scores_list = [re.findall(r'\d{1,2}', MathScores)[0], re.findall(r'\d{1,2}', MathScores)[1], re.findall(r'\d{1,2}', MathScores)[2], re.findall(r'\d{1,2}', MathScores)[3]]

#Zips the two lists together and coverts the output to a dictionary
final_Dict = dict(zip(names_list, scores_list))
#Prints the result
print(final_Dict)
