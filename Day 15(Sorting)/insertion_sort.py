'''
Insertion sort is a sorting algorithm wherein the given array is divided right into a looked after and an unsorted segment. 
In every iteration, the element to be inserted has to find its ultimate position within the taken care of subsequence and is then 
inserted whilst shifting the closing factors to the proper.
'''
# Time O(N^2) and Space O(1)

def insertion_sort(nums):

    for i in range(1,len(nums)):

        temp = nums[i]
        j = i-1

        while j >= 0:
            if nums[j] > temp:
                nums[j+1] = nums[j]

            else:
                break
            j-=1
                
        nums[j+1] = temp

    return nums

nums = [10,4,2,121,5,82,31]
print(insertion_sort(nums))
