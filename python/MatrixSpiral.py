"""This program takes a matrix of size mxn as input, and prints the matrix in a spiral format
for example: input ->> [[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]]
             output ->> 1 2 3 6 9 12 11 10 7 4 5 8"""


class Solution:
    def solve(self, matrix):
        ls=list()
        while matrix:
            ls.extend(matrix[0])
            #print(ls)
            matrix=list(zip(*matrix[1:]))[::-1]
            #print(matrix)
        return ls