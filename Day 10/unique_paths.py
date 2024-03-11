# time and space is exponential O(2^N). Space is because of stack space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [0]

        def validPath(r, c):
            if r >= m or c >= n:
                return False
            return True

        def solve(r, c):
            if r == m - 1 and c == n - 1:
                count[0] += 1
                return

            if not validPath(r, c):
                return

            # down
            solve(r + 1, c)
            # right
            solve(r, c + 1)

        solve(0, 0)

        return count[0]
    
# a slight variation into dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        i = 0
        j = 0
        dp = [[-1 for i in range(n)] for i in range(m)]

        def countPaths(m,n,i,j):
            if (i == (m - 1) and j == (n - 1)):
                return 1

            if (i >= m or j >= n or i < 0 or j < 0):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = countPaths(m,n,i+1,j) + countPaths(m,n,i,j+1)

            return dp[i][j]
        
        return countPaths(m,n,i,j)

# time and space O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]
        
        # Fill the first row and first column with 1's since there is only one way to reach each cell in them
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the rest of the array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Unique paths to reach cell (i,j) = unique paths from above + unique paths from left
        
        return dp[m-1][n-1]  # Return the number of unique paths to reach the bottom-right cell
        