class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res=""
        for i in range(num):
            for d in range(9,-1,-1):
                rem_sum=sum-d
                rem_digit=n-i-1
                if 0 <=rem_sum<=rem_digit * 9:
                    res+=str(d)
                    sum=rem_sum
                    break
        return res