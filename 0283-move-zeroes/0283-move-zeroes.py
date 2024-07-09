class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        remember the last zeros index at all time
        moves forward if nonZero
        """
        lastZero = None
        for index, num in enumerate(nums):
            if num==0:
                if lastZero is None:
                    lastZero = index
            else:
                if lastZero is not None:
                    nums[lastZero] = num
                    nums[index] = 0
                    lastZero += 1
        return nums
        