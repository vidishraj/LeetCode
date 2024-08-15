class NeighborSum:
    grid:list
    rowLength:int
        
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rowLength = len(grid)
    
    def findItem(self, value):
        for outerIndex, cont in enumerate(self.grid):
            for innerIndex, item in enumerate(cont):
                if item == value:
                    return outerIndex, innerIndex

    def adjacentSum(self, value: int) -> int:
            rowIndex, colInd = self.findItem(value)
            indices = [(rowIndex-1,colInd),(rowIndex+1,colInd),(rowIndex, colInd+1),(rowIndex, colInd-1)]
            adjSum=0
            for index in indices:
                if index[0]<self.rowLength and index[0]>=0 and index[1]<self.rowLength and index[1]>=0:
                    adjSum+=self.grid[index[0]][index[1]]
            return adjSum
            

    def diagonalSum(self, value: int) -> int:
            rowIndex, colInd = self.findItem(value)
            indices = [(rowIndex-1,colInd-1),(rowIndex+1,colInd+1),(rowIndex-1, colInd+1),(rowIndex+1, colInd-1)]
            diagSum=0
            for index in indices:
                if index[0]<self.rowLength and index[0]>=0 and index[1]<self.rowLength and index[1]>=0:
                    diagSum+=self.grid[index[0]][index[1]]
            return diagSum

# We have to find value first and then just find the values around it
# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)