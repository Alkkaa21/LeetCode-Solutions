class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(key):
            visited.add(key)
            for keys in rooms[key]:
                if keys not in visited:
                    dfs(keys)
        visited=set()
        dfs(0)
        for room in range(len(rooms)):
            if room not in visited:
                return False
        return True