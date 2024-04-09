def second_largest(nums):
    largest = nums[0]
    sec_large = nums[0]


    for i in range(1,len(nums)):
        largest = max(largest,nums[i])

    for i in range(len(nums)):
        if nums[i] < largest and nums[i] > sec_large:
            sec_large = nums[i]

    return sec_large

nums = [1,4,5,2,332,10000,1213]
print(second_largest(nums))