from typing import List


class Solution:
    resultA: dict = {}
    resultP: dict = {}

    def checkPath(self, oType, i, j, matrix, visited):
        visited[f"{i}-{j}"] = True
        if i == len(matrix) - 1 or j == len(matrix[0]) - 1:
            if oType == "A":
                return True
        if j == 0 or i == 0:
            if oType == "P":
                return True
        
        leftCheck, rightCheck, topCheck, bottomCheck = False,False,False,False
        if i + 1 < len(matrix) and matrix[i + 1][j] <= matrix[i][j] and not visited.get(f"{i + 1}-{j}"):
            if oType == "A" and self.resultA.get(f"{i + 1}-{j}") :
                bottomCheck = True
            elif oType == "P" and self.resultP.get(f"{i + 1}-{j}") :
                bottomCheck = True
            else:
                bottomCheck = self.checkPath(oType, i + 1, j, matrix, visited)
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] <= matrix[i][j] and not visited.get(f"{i}-{j + 1}"):
            if oType == "A" and self.resultA.get(f"{i}-{j + 1}") :
                rightCheck = True
            elif oType == "P" and self.resultP.get(f"{i}-{j + 1}") :
                rightCheck = True
            else:
                rightCheck = self.checkPath(oType, i, j + 1, matrix, visited)
        if i - 1 >= 0 and matrix[i - 1][j] <= matrix[i][j] and not visited.get(f"{i - 1}-{j}"):
            if oType == "A" and self.resultA.get(f"{i - 1}-{j}") :
                topCheck = True
            elif oType == "P" and self.resultP.get(f"{i - 1}-{j}") :
                topCheck = True
            else:
                topCheck = self.checkPath(oType, i - 1, j, matrix, visited)
        if j - 1 >= 0 and matrix[i][j - 1] <= matrix[i][j] and not visited.get(f"{i}-{j - 1}"):
            if oType == "A" and self.resultA.get(f"{i}-{j - 1}") :
                leftCheck = True
            elif oType == "P" and self.resultP.get(f"{i}-{j - 1}") :
                leftCheck = True
            else:
                leftCheck = self.checkPath(oType, i, j - 1, matrix, visited)

        return leftCheck or rightCheck or topCheck or bottomCheck

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        self.resultA = {}
        self.resultP = {}
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visitedA = {}
                visitedP = {}
                checkAO = self.checkPath("A", i, j, heights, visitedA)
                checkPO = self.checkPath("P", i, j, heights, visitedP)
                # print(i, j, checkAO, checkPO)
                if checkAO:
                    self.resultA[f"{i}-{j}"] = True
                if checkPO:
                    self.resultP[f"{i}-{j}"] = True
                if checkAO and checkPO:
                    res.append([i, j])

        return res