class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        cur=intervals[0]
        for i in range(len(intervals)-1):
            next=intervals[i+1]
            if cur[1]>=next[0]:
                cur=[cur[0],max(cur[1],next[1])]
            else:
                res.append(cur)
                cur=next
        res.append(cur)
        return res            
            