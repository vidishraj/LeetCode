class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        itemDict={}
        index=0
        while index<len(nums):
            item = nums[index]
            if itemDict.get(item) is not None and itemDict[item]['count']==3:
                nums[index]=nums[len(nums)-1]
                nums = nums[:-1]
            else:
                if itemDict.get(item) is None:
                    itemDict[item]={}
                    itemDict[item][index]=index
                    itemDict[item]['count']=1
                else:
                    itemDict[item][index]=index
                    itemDict[item]['count']+=1
                index+=1
        solutionList =[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                itemToFind = 0-nums[i]-nums[j]
                if itemDict.get(itemToFind) is not None:
                    if (itemDict[itemToFind].get(i) is None and itemDict[itemToFind].get(j) is None) or nums.count(itemToFind)>2:
                        solutionList.append(tuple([nums[i], nums[j], itemToFind]))
        solutionList = list(set(tuple(sorted(sub)) for sub in solutionList))
                    
        return solutionList
                