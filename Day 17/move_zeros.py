# https://leetcode.com/problems/move-zeroes/description/

# Time O(N) and Space O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            
            else:
                i+=1
                j+=1
                