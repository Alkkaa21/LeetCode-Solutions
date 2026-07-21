class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        
        for n in numset:
            if n-1  not in numset:
                length=1
              
                current=n
                while current+1 in numset:
                    length+=1
                    current+=1
                res=max(length,res)

        return res

