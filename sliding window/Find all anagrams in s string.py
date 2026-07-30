class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts={}
        countp={}
        res=[]
        n=len(p)
        for i in p:
            countp[i]=1+countp.get(i,0)
        for r in s[:len(p)]:
            counts[r]=1+counts.get(r,0)
        if counts==countp:
            res.append(0)
        l=0
        for r in range(n,len(s)):
            counts[s[l]]-=1
            if counts[s[l]]==0:
                del counts[s[l]]
            l+=1
            counts[s[r]]=1+counts.get(s[r],0)
            if counts==countp:
                res.append(l)
        return res
