# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        length=mountainArr.length()
        l,r=1,length-2
        while l<=r:
            m=(l+r)//2
            left,mid,right=mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)
            if left<mid<right:
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        peak=m

        l,r=0,peak
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m)
            if val>target:
                r=m-1
            elif val<target:
                l=m+1
            else:
                return m
        #right
        l,r=peak,length-1
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m)
            if val<target:
                r=m-1
            elif val>target:
                l=m+1
            else:
                return m
        return -1

        