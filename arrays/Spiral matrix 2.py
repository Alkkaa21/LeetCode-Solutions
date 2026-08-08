class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for _ in range(n)]
        top=0
        bottom=len(mat)-1
        left=0
        right=len(mat[0])-1
        num=1
        while top<=bottom and left<=right:
            for j in range(left,right+1):
                mat[top][j]=num
                num+=1
            top+=1
            for j in range(top,bottom+1):
                mat[j][right]=num
                num+=1
            right-=1
            for j in range(right,left-1,-1):
                mat[bottom][j]=num
                num+=1
            bottom-=1
            for j in range(bottom,top-1,-1):
                mat[j][left]=num
                num+=1
            left+=1
        return mat