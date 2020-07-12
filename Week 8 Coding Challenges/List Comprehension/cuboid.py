#   SCRIPT: cuboid.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Let's learn about list comprehensions! You are given three integers P,Q and R representing the dimensions of a cuboid along with an integer N.
#                You have to print a list of all possible coordinates given by i, j, k on a 3D grid where the sum of (i+j+k)  is not equal to N.
#                Here, 0 <= i <=P; 0 <= j <= Q; 0 <= k <= R.

"""
INPUT FORMAT: Four integers P, Q, R and N each on four separate lines, respectively.

CONSTRAINTS: Print the list in lexicographic increasing order.

Sample Input
1
1
1
2

Sample Output:
[[0,0,0], [0,0,1], [0,1,0], [1,0,0], [1,1,1]]
"""

#Gives a prompt to the user
print("Please input an integer on each line for i, j, k, n respectively: ")

#Stores input from the user to i,j,k,n
a = int(input())
b = int(input())
z = int(input())
n = int(input())

#Prints out the corresponding list while checking the range and making sure that (i + j + k) != n)
print([[i,j,k] for i in range(a + 1) for j in range(b + 1) for k in range(z + 1) if ((i + j + k) != n)])
