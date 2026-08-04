class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cur=intervals[0]
        count=0
        for i in range(1,len(intervals)):
            if cur[1]<=intervals[i][0]:
                cur=intervals[i]
            else:
                count+=1
        return count

