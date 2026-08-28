class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_map={0:-1}
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix%k in prefix_map:
                if i-prefix_map[prefix%k]>=2:
                    return True
            else:
                prefix_map[prefix%k]=i
        return False

            