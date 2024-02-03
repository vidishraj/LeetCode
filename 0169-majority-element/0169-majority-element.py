
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countMap = {}
        majorityCount = math.floor(len(nums)/2)
        for num in nums:
            if countMap.get(num) is None:
                countMap[num]=1
            else:
                countMap[num]+=1
                
        for key in countMap.keys():
            if countMap[key]>majorityCount:
                return key