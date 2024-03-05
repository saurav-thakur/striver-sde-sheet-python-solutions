
# Brute force with O(MN) Space
# Time - O((N*M)*(N+M) + (N*M))
# where (N*M) is first two loops and (N+M) is marking -1 and (N*M) is remarking 0  

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        mat_copy = [[None for i in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(n):
            for j in range(m):
                mat_copy[i][j] = matrix[i][j]

        
        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:
                    nrow = i
                    ncol = j

                    for r in range(n):
                        mat_copy[r][ncol] = 0

                    for c in range(m):
                        mat_copy[nrow][c] = 0
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = mat_copy[i][j]



# Brute force with O(1) Space
# Time - O(MN) 
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix[0])
        n = len(matrix)

        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:
                    nrow = i
                    ncol = j

                    for r in range(n):
                        if matrix[r][ncol] != 0:
                            matrix[r][ncol] = None

                    for c in range(m):
                        if matrix[nrow][c] != 0:
                            matrix[nrow][c] = None

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
# better 
# Time -> O(2*N*M) ->N*M + N*M
# Space -> O(N) + O(M)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [None for i in range(len(matrix))]
        col = [None for i in range(len(matrix[0]))]

        m = len(matrix[0])
        n = len(matrix)

        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(n):
            for j in range(m):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0