class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=0
        for d in range(len(number)):
            if number[d]==digit:
                candidate=number[:d]+number[d+1:]
                ans=max(ans,int(candidate))
        return str(ans)