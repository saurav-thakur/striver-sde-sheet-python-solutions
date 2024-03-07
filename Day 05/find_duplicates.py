
# O(N) time and space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return i
            

# O(N) time and O(1) space           
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow