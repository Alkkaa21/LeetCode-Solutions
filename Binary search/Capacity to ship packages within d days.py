class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l=max(weights)
        r=sum(weights)
        res=r

        def canship(cap):
            curcap=cap
            ships=1
            for w in weights:
                if curcap < w:
                    ships+=1
                    curcap=cap
                curcap-=w
            return ships<=days


    
        while l<=r:
            cap=(l+r)//2
            if canship(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res