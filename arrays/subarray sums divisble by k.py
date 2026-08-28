class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map={0:1}
        res=0
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            remainder=prefix%k
            if remainder in prefix_map:
                res+=prefix_map[remainder]
            prefix_map[remainder]=1+prefix_map.get(remainder,0)
        return res