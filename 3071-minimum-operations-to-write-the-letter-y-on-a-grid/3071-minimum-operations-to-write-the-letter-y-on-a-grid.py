from collections import defaultdict


class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        """
        First count the items in the Y cell and then count the elements in the non-y cells. Then start counting operations 
        """
        yCountDict = defaultdict(int)
        nyCountDict = defaultdict(int)
        middleIndex = math.floor(len(grid) / 2)
        for rowIndex, row in enumerate(grid):
            for columnIndex, rowItem in enumerate(row):
                key = rowItem
                if ((rowIndex == columnIndex and rowIndex <= middleIndex and columnIndex <= middleIndex) or (
                        rowIndex + columnIndex + 1 == len(
                    grid) and rowIndex <= middleIndex and columnIndex >= middleIndex) or (
                        columnIndex == middleIndex and rowIndex > middleIndex)):
                    if key != 1:
                        yCountDict[1] += 1
                    if key != 0:
                        yCountDict[0] += 1
                    if key != 2:
                        yCountDict[2] += 1
                else:
                    if key != 1:
                        nyCountDict[1] += 1
                    if key != 0:
                        nyCountDict[0] += 1
                    if key != 2:
                        nyCountDict[2] += 1
        possibleList = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        totalOperations = len(grid) ** 2
        for combo in possibleList:
            if totalOperations > yCountDict[combo[0]] + nyCountDict[combo[1]]:
                totalOperations = yCountDict[combo[0]] + nyCountDict[combo[1]]
        
        return totalOperations