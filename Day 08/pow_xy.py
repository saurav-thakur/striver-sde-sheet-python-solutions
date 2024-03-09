# Time O(2^N) and space O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        if n == 0:
            return 1

        if n > 0:
            for i in range(n):
                ans = ans * x
        else:
            for i in range(abs(n)):
                ans = ans * x
            ans = 1 / ans
        return ans

# Time (Log base 2 N) because we are dividing our steps by half each step and Space O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ans = 1
        nn = n

        if nn < 0:
            nn = -1 * nn

        while nn > 0:
            if (nn % 2 == 0):
                x = x * x
                nn = nn / 2

            else:
                ans = ans * x
                nn = nn - 1

        if n < 0:
            ans = 1/ans

        return ans