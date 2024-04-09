# https://www.youtube.com/watch?v=gmu0RA5_zxs

# Time O(N) and space O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # k is divided by length because eg if length of nums is 5 and k is 8 then
        # we count 8 from starting and when we reach 5th position we go from start
        # and then at third position we reach upto 8. so we take the mod
        k = k % len(nums)

        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
    
    def reverse(self,nums,start,end):
        while start <= end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1