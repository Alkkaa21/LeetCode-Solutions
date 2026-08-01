class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        res=[]
        for ch in s:
            freq[ch]=1+freq.get(ch,0)
        arr=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for ch,val in arr:
            res.append(ch*val)
        return "".join(res)
