class Solution:
    def climbStairs(self, n: int) -> int:
        resultList=[1, 1]
        for i in range(2,46):
            resultList.append(resultList[i-1]+resultList[i-2])
        return resultList[n]