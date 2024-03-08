# O(N^2) time and O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # O(N) time for loop
        for i in range(len(nums)):

            # O(N) time for checking if element exists
            if i not in nums:
                return i
        return len(nums)
    

# O(NLogN) time and O(1) Space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    
# O(N) time and O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
    
# O(N) time and O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_num_sums = sum(nums)
        total_sums = (n*(n+1))//2

        return total_sums - total_num_sums