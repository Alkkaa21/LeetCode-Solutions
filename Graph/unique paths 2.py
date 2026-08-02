class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0]*cols for _ in range(rows)]

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif i==rows-1 and j==cols-1:
                    dp[i][j]=1
                elif i==rows-1: 
                    dp[i][j]=dp[i][j+1]
                elif j==cols-1:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]