class Solution(object):
    def rotate(self, nums:list, k:int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        Calculate index to swap at every index that you are at 
        make a copy of the array for reference first 
        [1, 2, 3, 4, 5, 6, 7] k = 3
        1 moved from 0-> 3. 3%7 = 3
        5 moved from 4 to 0 because 4+3=7 and 7%7 = 0
        k=3
        [5, 6, 7, 1, 2, 3, 4]
        
        """
        copyList = nums.copy()
        k = k % len(nums)
        
        for index, item in enumerate(nums):
            # print(index, ((index+k)%len(nums)))
            nums[(index+k)%len(nums)] = copyList[index]
        