class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # Find the lowest power of 2 and use it if [1, 2] in the list then [1, 2^3 +1 ] range of numbers can be formed
        setNums = set(nums)
        solution = 0 
        for i in range(32):
            current = 2** i 
            currentInNums=False
            for num in setNums:
                if num == current:
                    currentInNums = True
            if currentInNums:
                solution+=current
            else:
                return solution+1
        return solution+1
