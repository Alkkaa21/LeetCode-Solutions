class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        subarray=nums[0]
        for i in range(len(nums)):
            cursum=max(nums[i],nums[i]+cursum)
            subarray=max(cursum,subarray)
        return subarray