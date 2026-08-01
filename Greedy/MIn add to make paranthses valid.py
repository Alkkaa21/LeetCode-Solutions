class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s=="":
            return 0
        balance=0
        additions=0
        for ch in s:
            if ch=='(':
                balance+=1
            elif ch==')':
                balance-=1
            if balance<0:
                additions+=1
                balance=0
                
        return additions+balance