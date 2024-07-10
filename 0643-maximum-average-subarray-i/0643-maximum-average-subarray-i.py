class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Sounds easy, create a window and do the averaging 
        Can do simple math
        """
        runningSum = 0
        i =0 
        j = 0
        localMax = 0
        globalMax = 0
        itemCount = 0
        while j<k:
            runningSum+=nums[j]
            j+=1
        
        globalMax = round(runningSum/k,5)
        while j<len(nums):
            runningSum-=nums[i]
            runningSum+=nums[j]
            localMax = round(runningSum/k,5)
            if globalMax<localMax:
                globalMax = localMax
            i+=1
            j+=1
        return globalMax