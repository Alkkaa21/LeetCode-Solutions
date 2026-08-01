class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
       stack=[]
       for n in num:
        while stack and k>0 and stack[-1]>n:
            stack.pop()
            k-=1
        stack.append(n)
       while k>0:
            stack.pop()
            k-=1
    
       ans="".join(stack)
       return ans.lstrip('0') or '0'
    