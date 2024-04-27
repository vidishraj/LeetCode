from queue import Queue
from collections import defaultdict


class Solution:
    visited: defaultdict

    def __init__(self):
        self.visited = defaultdict(dict)

    def doBFS(self, matrix, start, end):
        bfsQueue = Queue()
        bfsQueue.put(tuple([start, end]))
        self.visited[start][end] = True
        while bfsQueue.qsize() != 0:
            currentIndex = bfsQueue.get()
            id1, id2 = currentIndex[0], currentIndex[1]
            if id1 + 1 < len(matrix) and matrix[id1 + 1][id2] == '1' and self.visited.get(id1 + 1).get(id2) is False:
                bfsQueue.put(tuple([id1 + 1, id2]))
                self.visited[id1 + 1][id2] = True
            if id2 + 1 < len(matrix[0]) and matrix[id1][id2 + 1] == '1' and self.visited.get(id1).get(id2 + 1) is False:
                bfsQueue.put(tuple([id1, id2+1]))
                self.visited[id1][id2 + 1] = True
            if id1 - 1 >= 0 and matrix[id1 - 1][id2] == '1' and self.visited.get(id1 - 1).get(id2) is False:
                bfsQueue.put(tuple([id1 - 1, id2]))
                self.visited[id1 - 1][id2] = True
            if id2 - 1 >= 0 and matrix[id1][id2 - 1] == '1' and self.visited.get(id1).get(id2 - 1) is False:
                bfsQueue.put(tuple([id1, id2-1]))
                self.visited[id1][id2 - 1] = True
        return

    def numIslands(self, grid: list[list[str]]) -> int:
        bfsCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.visited.get(i) is None:
                    self.visited[i] = {}
                self.visited[i][j] = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and self.visited.get(i).get(j) is False:
                    bfsCount += 1
                    self.doBFS(grid, i, j)
        return bfsCount