class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total+=i
        rangetotal=0
        n=len(nums)
        for i in range(n+1):
            rangetotal+=i
        return(rangetotal-total)


