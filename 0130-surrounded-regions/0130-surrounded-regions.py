from queue import Queue
from collections import defaultdict


class Solution:
    visited: defaultdict

    def visitedCheck(self, id1, id2):
        if self.visited.get(id1) is not None and self.visited.get(id1).get(id2) is not None:
            return False
        return True

    def setVisited(self, id1, id2):
        if self.visited.get(id1) is None:
            self.visited[id1] = {}
        self.visited[id1][id2] = True
        return

    def doBfs(self, board: list[list[str]], index: tuple):
        try:
            currentQueue = Queue()
            indexList = []
            indexList.append(index)
            currentQueue.put(index)
            boundaryCheck = False
            while currentQueue.qsize() > 0:
                currentIndex = currentQueue.get()
                ot, inn = currentIndex[0], currentIndex[1]
                if ot + 1 < len(board) and board[ot + 1][inn] == "O" and self.visitedCheck(ot + 1, inn):
                    self.setVisited(ot + 1, inn)
                    if ot + 1 == len(board) - 1:
                        boundaryCheck = True
                    indexList.append(tuple([ot+1, inn]))
                    currentQueue.put(tuple([ot + 1, inn]))
                if inn + 1 < len(board[0]) and board[ot][inn + 1] == "O" and self.visitedCheck(ot, inn + 1):
                    self.setVisited(ot, inn + 1)
                    if inn + 1 == len(board[0]) - 1:
                        boundaryCheck = True
                    indexList.append(tuple([ot, inn + 1]))
                    currentQueue.put(tuple([ot, inn + 1]))
                if inn - 1 >= 0 and board[ot][inn - 1] == "O" and self.visitedCheck(ot, inn - 1):
                    self.setVisited(ot, inn - 1)
                    if inn - 1 == 0:
                        boundaryCheck = True
                    indexList.append(tuple([ot, inn - 1])) 
                    currentQueue.put(tuple([ot, inn - 1]))
                if ot - 1 >= 0 and board[ot - 1][inn] == "O" and self.visitedCheck(ot - 1, inn):
                    self.setVisited(ot - 1, inn)
                    if ot - 1 == 0:
                        boundaryCheck = True
                    indexList.append(tuple([ot-1, inn]))
                    currentQueue.put(tuple([ot - 1, inn]))
                    
            if not boundaryCheck:
                for ind in indexList:
                    board[ind[0]][ind[1]] = "X"
            return board

        except Exception as ex:
            print(f"Exception while doing BFS {ex}")

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.visited = defaultdict()
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O" and self.visitedCheck(i, j):
                    newBoard = board.copy()
                    check = self.doBfs(newBoard, tuple([i, j]))
                    if check is not None:
                        board = check
        return board