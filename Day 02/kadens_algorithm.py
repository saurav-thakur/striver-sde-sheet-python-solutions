class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cum_sum = 0
        total_sum = 0
        max_neg = float('-inf')
        count_neg = 0

        for i in nums:
            if i < 0:
                max_neg = max(max_neg,i)
                count_neg += 1

            cum_sum += i

            if cum_sum < 0:
                cum_sum = 0
            
            total_sum = max(total_sum,cum_sum)

        if count_neg == len(nums):
            return max_neg
        return total_sum
