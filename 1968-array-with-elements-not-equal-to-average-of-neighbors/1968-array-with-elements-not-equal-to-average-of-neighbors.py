class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        There are patterns with the math here -> average (a+b)/2=c-> a = 2c-b
        (10, 15, 20) or (8, 16, 24) -> same difference between all. If the difference between the three numbers it he same, the middle  number will be the average. 
        Try to make the pattern like this-> a1, an, a2, a(n-1)....and so on 
        
        Two conditions----> odd elements and even elements. [1, 2,3]    a1, a3, a2
        [1,2,3,4]-> 1, 4, 2, 3]
        """
        i = 0
        j = len(nums) - 1
        nums.sort()
        newNums = []
        while i < j:
            newNums.append(nums[i])
            newNums.append(nums[j])
            i += 1
            j -= 1
        if i==j:
            newNums.append(nums[i])
        return newNums
