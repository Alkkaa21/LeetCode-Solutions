class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        hashmap={}
        for num in nums:
            hashmap[num]=1+hashmap.get(num,0)
        for num in hashmap:
            if hashmap[num]>n//2:
                return int(num)