class Solution:
    def countBits(self, n: int) -> List[int]:
        count=0
        ans=[]
        for i in range(n+1):
            if i==0:
                ans.append(i)
            else:
                while i:
                    i=i&(i-1)
                    count+=1
                ans.append(count)
                count=0
        return ans
