class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:    
        countDict= {}
        for num in arr:
            if countDict.get(num) is None:
                countDict[num]=1
            else:
                countDict[num]+=1
        sortedValueList =sorted(countDict, key=countDict.get)
        for key in sortedValueList:
            if countDict[key]>=k and k>0:
                value = countDict[key]
                if countDict[key]-k<=0:
                    del countDict[key]
                else:
                    countDict[key]-=k
                k-=value
            elif countDict[key]<k:
                k-=countDict[key]
                del countDict[key]
        return len(countDict)
                