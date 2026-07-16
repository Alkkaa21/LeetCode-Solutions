class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum
        l=0
        for r in range(k,len(nums)):
            window_sum+=nums[r]
            window_sum-=nums[l]
            l+=1
            max_sum=max(max_sum,window_sum)
        return max_sum/k