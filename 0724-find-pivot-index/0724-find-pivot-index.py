class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        dpL = [0 for num in nums]
        dpR = [0 for num in nums]
        runningSum = 0 
        for index,num in enumerate(nums):
            dpL[index] = runningSum
            runningSum+=num
        runningSum = 0
        for i in range(len(nums)-1, -1, -1):
            dpR[i] = runningSum
            runningSum+=nums[i]
        for i in range(len(nums)):
            if dpL[i]==dpR[i]:
                return i
        return -1