class Solution:
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                self.swap(nums,i,j)
                i += 1
                j += 1

            elif nums[j] == 1:
                j += 1

            elif nums[j] == 2:
                self.swap(nums,j,k)
                k-=1