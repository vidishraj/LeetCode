import copy
class Solution:

    def checkFreshOranges(self, grid):
        freshOrangeCount = 0
        for orangeRow in grid:
            for orange in orangeRow:
                if orange == 1:
                    freshOrangeCount += 1
        return freshOrangeCount

    def checkIfAdjacentRotten(self, grid, rIndex, cIndex):
        if (rIndex > 0 and grid[rIndex - 1][cIndex] == 2) or (rIndex < len(grid)-1 and grid[rIndex + 1][cIndex] == 2):
            return True
        if (cIndex > 0 and grid[rIndex][cIndex - 1] == 2) or (cIndex < len(grid[0])-1 and grid[rIndex][cIndex + 1] == 2):
            return True
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Check how many oranges are there, then run bfs with alive oranges that many times+1.
        in the end, check if there are stil any oranges left
        """
        freshOrangeCount = self.checkFreshOranges(grid)
        minCheckRequired = 0
        mins = 0
        while minCheckRequired < freshOrangeCount + 1:
            gridCopy = copy.deepcopy(grid)
            changes = 0
            freshOrange = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    # fresh orange check
                    if grid[i][j] == 1:
                        freshOrange +=1
                        if self.checkIfAdjacentRotten(grid, i, j):
                            gridCopy[i][j] = 2
                            changes+=1
            if freshOrange == 0:
                return mins
            if changes == 0:
                return -1
            grid = gridCopy
            minCheckRequired += 1
            mins += 1
        return -1
