
'''
The simple concept of bubble sorting is that it time and again swaps adjoining elements if they're now not in the preferred order. YES, it is as simple as that.
If a given array of factors must be looked after in ascending order, bubble sorting will begin by way of comparing the primary element of the array with the second 
one element and immediately change them if it turns out to be greater than the second one element, after which flow directly to evaluate the second and 0.33 element, and so on.
'''

# Idea is to swap each element if one element is greater than other.
# move right to left. i.e sort from smallest to largest
# Time O(N^2) and Space O(1) 

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

    return nums

nums = [10,4,2,121,5,82,31]
print(bubble_sort(nums))
