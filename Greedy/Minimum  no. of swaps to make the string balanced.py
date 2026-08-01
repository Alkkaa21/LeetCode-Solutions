class Solution:
    def minSwaps(self, s: str) -> int:
        if s=="[]":
            return 0
        balance=0
        table=[]
        for ch in s:
            if ch=='[':
                balance+=1
            elif ch==']':
                balance-=1
            table.append(balance)
        minbalance=min(table)
        swaps=ceil(abs(minbalance)/2)
        return swaps
