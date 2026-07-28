#Given an array of non-negative integers, the task is to find the minimum number of elements such that their sum should be greater than the sum of the rest of the elements of the array.

#Input: arr[] = [ 3 , 1 , 7, 1 ]
#Output: 1
class Solution:
    def minSubset(self, arr):
        # code here
        arr.sort(reverse=True)
        tot=sum(arr)
        chosen=0
        count=0
        for num in arr:
            chosen+=num
            count+=1
            rem=tot-chosen
            if chosen>rem:
                return count
            