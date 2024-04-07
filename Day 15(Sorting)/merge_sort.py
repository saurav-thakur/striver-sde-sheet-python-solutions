def merge(nums,start,end):

    mid = (start + end)//2

    len1 = mid - start + 1
    len2 = end - mid

    first,second = [],[]

    # copy values
    mainArrayIdx = start
    for i in range(len1):
        first.append(nums[mainArrayIdx])
        mainArrayIdx+=1

    mainArrayIdx = mid + 1
    for i in range(len2):
        second.append(nums[mainArrayIdx])
        mainArrayIdx+=1

    # merge
    idx1 = 0
    idx2 = 0
    mainArrayIdx = start

    while (idx1 < len1 and idx2 < len2):
        if first[idx1] < second[idx2]:
            nums[mainArrayIdx] = first[idx1]
            idx1 += 1
        else:
            nums[mainArrayIdx] = second[idx2]
            idx2 += 1

        mainArrayIdx += 1

    while idx1 < len1:
        nums[mainArrayIdx] = first[idx1]
        mainArrayIdx += 1
        idx1 += 1

    while idx2 < len2:
        nums[mainArrayIdx] = second[idx2]
        mainArrayIdx += 1
        idx2 += 1


def merge_sort(nums,start,end):

    if start >= end:
        return

    mid = (start + end) // 2

    merge_sort(nums,start,mid)
    merge_sort(nums,mid+1,end)

    merge(nums,start,end)

    return nums


nums = [10,4,2,121,5,82,31]
print(merge_sort(nums,0,len(nums)-1))