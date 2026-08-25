class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(node):
            r,c=node
            visited.add(node)
            area=1
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if nr>=0 and nr<rows and nc>=0 and nc<cols and (nr,nc) not in visited and grid[nr][nc]==1:
                    area+=dfs((nr,nc))
            return area
        rows,cols=len(grid),len(grid[0])
        visited=set()
        max_area=0
        for i  in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    area=dfs((i,j))
                    max_area=max(area,max_area)
        return max_area