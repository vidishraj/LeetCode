class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        existDictA: dict = {}
        for index, item in enumerate(A):
            existDictA[item] = index
        solution = []
        currentCount = 0
        unSeenDict = {} #to let us know at index i, we need to add x
        for index, item in enumerate(B):
            if existDictA[item] <= index:
                currentCount += 1
            else:
                unSeenDict[existDictA[item]] = True
            if unSeenDict.get(index) is not None:
                solution.append(currentCount+1)
                currentCount+=1
            else:
                solution.append(currentCount)
        return solution
