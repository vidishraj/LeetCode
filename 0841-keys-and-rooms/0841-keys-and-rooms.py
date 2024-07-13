class Solution:
    
    def dfs(self, currentIndex, rooms, visited):
        
        if visited[currentIndex] is True:
            return
        visited[currentIndex]=True
        for room in rooms[currentIndex]:
            self.dfs(room, rooms, visited)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Run basic dfs to check
        """
        
        visited = [False for room in rooms]
        self.dfs(0, rooms, visited)
        res = True
        for v in visited:
            res &= v
        return res