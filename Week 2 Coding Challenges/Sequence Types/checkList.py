#   SCRIPT: checkList.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Input a list of strings “str_list” separated by spaces and input a character “ch”.
#                For each string in str_list, count the number of occurrences of the character “ch” in that string
#                and store in a new answer list and print the answer list.
#                Note: The order of the occurrence of the words and the corresponding answer list matters.
"""
Sample Input:
python sword happy code star good wow
o

Sample Output:
[1, 1, 0, 1, 0, 2 , 1]

Explanation:
The word ‘python’ has 1 ‘o’ , so 1 is appended.
The word ‘sword’ has 1 ‘o’, so 1 is appended.
The word ‘good’ has 2 ‘o’, so 2 is appended.
The words ‘happy’ has 0 ‘o’, so 0 is appended.
"""

#Takes a list of strings as an input from the user and stores them in list 'str_list'
str_list = input("Please enter a list of strings separated by a space: ").split()

print("Inputted String:", str_list)

#Takes a character as an input from the user and stores it as a string 'ch'
ch = input("Please enter a character: ")

#Function that determines how many occurrences there is of 'ch' in a string
def occurList(ls):
    count = 0

    #searches each index in the passed in string
    for index in ls:
        #if 'ch' is in the index
        if ch in index:
            #count the occurrence
            count = count + 1

    #returns the list storing the count
    return count

#Passes in each index of str_list to the function occurList and stores the returning count in a new list 'num_list'
num_list = [occurList(index) for index in str_list]

print("The number of times that the character, {}, appeared in each string of the list was: \n{}".format(ch, num_list))
