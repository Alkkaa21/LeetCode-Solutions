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
            