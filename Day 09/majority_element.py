# O(N^2) time and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n_by_3 = len(nums) // 3
        ans = set()

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1

            if count > n_by_3:
                ans.add(nums[i])

        
        return list(ans)
    

# O(N) time and space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = {}
        n = len(nums)

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for key,val in d.items():
            if val > n//2:
                return key
            
# O(N) time and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0

        for i in range(len(nums)):

            if count == 0:
                ans = nums[i]

            if ans == nums[i]:
                count += 1
            else:
                count -= 1

        return ans
