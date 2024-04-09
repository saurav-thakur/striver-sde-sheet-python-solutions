def largest_element(nums):
    largest = nums[0]

    for i in range(1,len(nums)):
        largest = max(largest,nums[i])

    return largest

nums = [1,4,5,2,332,1213]
print(largest_element(nums))