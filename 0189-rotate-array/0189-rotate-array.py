class Solution(object):
    def rotate(self, nums:list, k:int):
        copyList = nums.copy()
        k = k % len(nums)
        for index, item in enumerate(nums):
            nums[(index+k)%len(nums)] = copyList[index]
        