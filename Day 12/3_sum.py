class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        nums.sort()  # Sort the list to use two-pointer approach

        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans
    
    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):

            # to avoid duplicates
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1
            target = -(nums[i])

            while low < high:
                sums = nums[low] + nums[high]

                if sums == target:
                    ans.append((nums[i],nums[low],nums[high]))

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1

                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1

                elif sums > target:
                    high -= 1

                elif sums < target:
                    low += 1

        return ans