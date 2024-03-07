class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        i = 0
        j = len(matrix) - 1

        while i <= j:
            matrix[i],matrix[j] = matrix[j],matrix[i]
            i+=1
            j-=1

        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]