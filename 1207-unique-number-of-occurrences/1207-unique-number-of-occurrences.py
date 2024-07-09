class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numDict = {}
        for num in arr:
            if numDict.get(num) is None:
                numDict[num] = 1
            else:
                numDict[num]+=1
        dictValues = list(numDict.values())
        occurDict={}
        for value in dictValues:
            if occurDict.get(value) is not None:
                return False
            occurDict[value] = True
        return True
        