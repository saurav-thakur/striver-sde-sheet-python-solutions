# The brute force solution is to traverse through 2D matrix and find the element. The time complexity will be O(N * M)

# O(log(N*M)) time and O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix) - 1
        m = len(matrix[0]) - 1

        for i in range(len(matrix)):

            start = 0
            end = m

            while start <= end:
                mid = (start + end)//2

                if matrix[i][mid] == target:
                    return True

                elif target < matrix[i][mid]:
                    end = mid - 1

                else:
                    start = mid + 1
        return False 