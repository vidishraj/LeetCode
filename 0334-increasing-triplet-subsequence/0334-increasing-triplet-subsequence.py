class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        if at every point we just remember the lowest and greatest number 
        we should be good to go
        """
        if len(nums)<3:
            return False
        dpL = []
        dpG = [0 for num in nums]
        runningMin = nums[0]
        for num in nums:
            if num<runningMin:
                runningMin = num
            dpL.append(runningMin)
        runningMax = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>runningMax:
                runningMax = nums[i]
            dpG[i] = runningMax
        for i in range(len(nums)):
            curr = nums[i]
            lowestBefore = dpL[i]
            greatestAfter = dpG[i]
            if lowestBefore<curr and greatestAfter>curr:
                return True
        return False