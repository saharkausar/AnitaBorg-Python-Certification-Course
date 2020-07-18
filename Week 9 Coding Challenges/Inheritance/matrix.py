#   SCRIPT: matrix.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Perform matrix multiplication on 2 given 2*2 arrays and return a 2*2 matrix as answer. Using functions as specified in
#                the description using partial solutions computed by the super class.
#                Given two 2*2 matrices A and B,
#                A= [[a1 a2],
#                [a3 a4]]
#                B= [[b1 b2]
#                [b3 b4]]
#                write a superclass, one_D that:
#                Has function dot_prod() (i/p : ( a1(array 1[1*2]) , a2(array 2[1*2]) ) , o/p: ans(integer)) performs dot product on 2 given 1 dimensional matrices,
#                here [a1 a2] and [b1 b3]]. And returns an integer(a1*b1+a2*b3 ) as the answer. Write a subclass, two_D that
#                Has function dot_prod() (i/p : ( a1(array 1[2*2]) , a2(array 2[2*2]) ) , o/p: ans(array [2*2])) performs matrix
#                multiplication on 2 given 2 dimensional matrices, And returns a matrix as the answer, which calls the dot_prod() function of the super class.

"""
Sample input:
[[1,2],[3,4]]
[[5,6],[7,8]]

Sample output:
[[19,22],[43,50]]
"""

#Superclass, one_D, that has a dot_prod() function that performs dot product on two given 1 dimensional matrices
class one_D:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    #Method that performs dot product on two given 1 dimensional matrices
    def dot_prod(self, array1, array2):
        a1 = array1[0]
        a2 = array1[1]
        b1 = array2[0]
        b2 = array2[1]

        #Computes the dot product of the elements: array 1[1*2] and a2(array 2[1*2]
        result = ((array1[0] * array2[0]) + (array1[1] * array2[1]))
        #Returns the result as an integer sum
        return result

#Subclass, two_D, that has a dot_prod() function that performs dot product on two given 2 dimensional matrices
class two_D(one_D):
    def __init__(self, array3, array4):
        super().__init__(self, two_D)

    #Method that performs matrix multiplication on two given 2 dimensional matrices by calling the dot_prod() function of the super class
    def dot_prod(self, array3, array4):

        matrix = [[super().dot_prod(array1, array2), super().dot_prod(array1, array3)], [super().dot_prod(array4, array2), (super().dot_prod(array4, array3))]]

        return matrix

#Array based on a1, a2 from the example
array1 = [int(m) for m in input("Please enter [a1 a2] for the first matrix 'A' separated by a space (Sample Input Example: 1 2): ").split()]
#Array based on b1, b3 from the example
array2 = [int(m) for m in input("Please enter [b1 b3] for the second matrix 'B' separated by a space (Sample Input Example: 5 7): ").split()]
#Array based on b2, b4 from the example
array3 = [int(m) for m in input("Please enter [b2 b4] for the second matrix 'B' separated by a space (Sample Input Example: 6 8): ").split()]
#Array based on a3, a4 from the example
array4 = [int(m) for m in input("Please enter [a3 a4] for the first matrix 'A' separated by a space (Sample Input Example: 3 4): ").split()]

#Create an object and print the result
finalMatrix = two_D(array3, array4)
print(finalMatrix.dot_prod(array3, array4))
