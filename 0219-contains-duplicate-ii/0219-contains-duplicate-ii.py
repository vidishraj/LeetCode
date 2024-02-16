class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        countDict={}
        for index, item in enumerate(nums):
            if countDict.get(item) is None:
                countDict[item]= index
            else:
                if abs(countDict[item]-index)<=k:
                    return True
                countDict[item]=index
        return False