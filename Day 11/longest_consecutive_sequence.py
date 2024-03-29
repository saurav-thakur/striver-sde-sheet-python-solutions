# Time O(n*m) and space O(n) for set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = []
        max_count = 0

        for i in num_set:
            temp = i
            count = 1
            if temp - 1 not in num_set:
                while temp + 1 in num_set:
                    count += 1
                    temp += 1

            max_count = max(count, max_count)
        return max_count
                
