from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l = 0
            freq = defaultdict(int)
            ans = 0
            distinct=0
            for r in range(len(nums)):
                if freq[nums[r]]==0:
                    distinct+=1
                freq[nums[r]]+=1
                while distinct>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        distinct-=1
                    l+=1
                ans+=r-l+1
            return ans
        return atmost(k)-atmost(k-1)