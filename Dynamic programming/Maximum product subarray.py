class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod=nums[0]
        maxprod=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            tempmax=max(nums[i],nums[i]*maxprod,nums[i]*minprod)
            tempmin=min(nums[i],nums[i]*maxprod,nums[i]*minprod)
            maxprod=tempmax
            minprod=tempmin
            ans=max(maxprod,ans)
        return ans
