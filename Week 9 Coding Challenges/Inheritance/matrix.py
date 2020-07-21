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

        print("The first matrix (Matrix A) is:", [[matrixA[0],matrixA[1]],[matrixA[2],matrixA[3]]])
        print("The second matrix (Matrix B) is:", [[matrixB[0],matrixB[1]],[matrixB[2],matrixB[3]]])

        #Splits the matrices from the user input
        firstInput = [matrixA[0], matrixA[1]] #[[a1 a2]]
        secondInput =  [matrixB[0], matrixB[2]] #[[b1 b3]]
        thirdInput = [matrixB[1], matrixB[3]] #[[b2 b4]]
        fourthInput = [matrixA[2], matrixA[3]] #[[a3 a4]]

        #Calculates the dot product from the split matrices by feeding it back into one_D.dot_prod()
        matrixCalc = [[super().dot_prod(firstInput, secondInput), super().dot_prod(firstInput, thirdInput)], [super().dot_prod(fourthInput, secondInput), (super().dot_prod(fourthInput, thirdInput))]]

        return matrixCalc

#Input for the first matrix [a1 a2 a3 a4]
matrixA = [int(m) for m in input("Please enter [a1 a2 a3 a4] for the first matrix 'A' separated by a space (Sample Input Example: 1 2 3 4): ").split()]
#Input for the second matrix [b1 b2 b3 b4]
matrixB = [int(m) for m in input("Please enter [b1 b2 b3 b4] for the second matrix 'B' separated by a space (Sample Input Example: 5 6 7 8): ").split()]

#Create an object and print the result
finalMatrix = two_D(matrixA, matrixB)
print("The dot product of Matrix A and B is:", finalMatrix.dot_prod(matrixA, matrixB))
