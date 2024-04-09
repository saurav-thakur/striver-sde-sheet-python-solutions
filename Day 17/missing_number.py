# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        total_sum = sum(nums)
        total_length_sum = n*(n+1)//2

        return total_length_sum - total_sum