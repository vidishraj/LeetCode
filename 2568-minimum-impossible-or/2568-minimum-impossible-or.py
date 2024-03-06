class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # Find the lowest power of 2 and use it if [1, 2] in the list then [1, 2^3 +1 ] range of numbers can be formed
        setNums = set(nums)
        itemDict = {}
        for num in setNums:
            itemDict[num] = True
        solution = 0 
        for i in range(32):
            current = 2** i 
            if itemDict.get(current) is not None:
                solution+=current
            else:
                return solution+1
        return solution+1
