# time complexity O(N^3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        nums.sort()

        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+= 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans
