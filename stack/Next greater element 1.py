class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map={}
        ans=[]
        for n in nums2:
            while stack and n>stack[-1]:
                map[stack[-1]]=n
                stack.pop()
            stack.append(n)
        for n in nums1:
            ans.append(map.get(n,-1))
        return ans

            
            