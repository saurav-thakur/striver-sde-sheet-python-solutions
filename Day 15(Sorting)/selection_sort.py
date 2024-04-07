

'''
Selection type is a sorting algorithm wherein the given array is split into two subarrays, the sorted left segment, and the unsorted proper segment.
Initially, the taken care of component is empty and the unsorted component is the entire list. In each iteration, we fetch the minimal detail from the 
unsorted listing and push it to the quit of the taken care of list for that reason constructing our taken care of array.
'''

# Idea is to select the smallest element from the i+1 array and swap it with the i
# move right to left. i.e sort from smallest to largest
# Time O(N^2) and Space O(1) 
def selection_sort(nums):

    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return nums

nums = [64,25,12,22,11,12]
print(selection_sort(nums))