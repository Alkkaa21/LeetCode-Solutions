class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum=[]
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            runningsum.append(total)
        return runningsum