import queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        check all the paths and then check if the current path is an exit
        """
        q = queue.Queue()
        colEnd = len(maze[0])-1
        rowEnd = len(maze)-1
        # Keep list in the form [[rIndex, cIndex], steps]
        
        res = sys.maxsize
        originalRes = res
        q.put([entrance, 0])
        visited = [[False for item in maze[0]] for item in maze]
        visited[entrance[0]][entrance[1]] = True
        while(q.qsize()!=0):
            curr = q.get()
            cord = curr[0]
            rowIndex = cord[0]
            colIndex = cord[1]
            steps = curr[1]
            if (colIndex == 0 or colIndex == colEnd or rowIndex == 0 or rowIndex == rowEnd) and steps!=0:
                if res>steps:
                    res = steps
            else:
                if rowIndex!=rowEnd and maze[rowIndex+1][colIndex]!="+" and not visited[rowIndex+1][colIndex]:
                    q.put([[rowIndex+1, colIndex], steps+1])
                    visited[rowIndex+1][colIndex] = True
                if rowIndex!=0 and maze[rowIndex-1][colIndex]!="+" and not visited[rowIndex-1][colIndex]:
                    q.put([[rowIndex-1, colIndex], steps+1])
                    visited[rowIndex-1][colIndex] = True
                if colIndex!=colEnd and maze[rowIndex][colIndex+1]!="+" and not visited[rowIndex][colIndex+1]:
                    q.put([[rowIndex, colIndex+1], steps+1])
                    visited[rowIndex][colIndex+1] = True
                if colIndex!=0 and maze[rowIndex][colIndex-1]!="+" and not visited[rowIndex][colIndex-1]:
                    q.put([[rowIndex, colIndex-1], steps+1])
                    visited[rowIndex][colIndex-1] = True
        
        if res==originalRes or res == 0:
            return -1
        return res
                