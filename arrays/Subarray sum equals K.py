class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count={0:1}
        prefix=0
        res=0
        for n in nums:
            prefix+=n
            
            if prefix-k in prefix_count:
                res+=prefix_count[prefix-k]
            prefix_count[prefix]=1+prefix_count.get(prefix,0)
        return res

