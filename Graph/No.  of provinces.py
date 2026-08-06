class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and neighbour not in visited:
                    dfs(neighbour)
        visited=set()
        count=0
        n=len(isConnected)
        for city in range(n):
            if city not in visited:
                count+=1
                dfs(city)
        return count                    