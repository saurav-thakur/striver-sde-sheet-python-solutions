# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
# https://youtu.be/t1GLDWqWVQk

# Time O(N) and Space O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        
        count = 0
        n = len(nums)
        for i in range(len(nums)):

            if (nums[i] > nums[(i+1)%n]):
                count += 1

            if count > 1:
                return False

        return True