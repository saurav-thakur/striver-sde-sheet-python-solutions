class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            nums.reverse()
            return
        
        pointer = len(nums) - 2

        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1

        if pointer == -1:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,pointer,-1):
            if nums[i] > nums[pointer]:
                nums[i],nums[pointer] = nums[pointer],nums[i]
                break

        nums[pointer+1:] = reversed(nums[pointer+1:])
