# O(N^2) time and O(1) space
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        
        count = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    count += 1
                    
        return count


# O(NLogN) Time and O(N) Space for temporary array.
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    
    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid + 1
        
        count = 0
        
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1
                
        
        while left <= mid:
            temp.append(arr[left])
            left+=1
            
        
        while right <= high:
            temp.append(arr[right])
            right+=1
            
        for i in range(low,high+1):
            arr[i] = temp[i - low]
            
        return count
    
    def mergeSort(self,arr,low,high):
        
        count = 0
        
        if low >= high:
            return count
            
        mid = (low + high)//2
        count += self.mergeSort(arr,low,mid)
        count += self.mergeSort(arr,mid+1,high)
        count += self.merge(arr,low,mid,high)
        return count
    
    def inversionCount(self, arr, n):
        # Your Code Here
        low = 0
        high = len(arr) - 1
        ans = self.mergeSort(arr,low,high)
        return ans
        
        