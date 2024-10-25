from copy import deepcopy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        The idea isnt to iterate from the top to the bottom but rather from the bottom to the top and 
        check the choices we are presented
        """
        dp = deepcopy(grid)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows-2, -1, -1):
          dp[i][cols-1] +=dp[i+1][cols-1]
        for i in range(cols-2, -1, -1):
          dp[rows-1][i] +=dp[rows-1][i+1]
        for i in range(rows-2, -1, -1):
            for j in range(cols-2, -1, -1):
                rightSum = dp[i+1][j] + grid[i][j]
                downSum = dp[i][j+1] + grid[i][j]
                dp[i][j] = min(rightSum, downSum)
        # print(dp)
        return dp[0][0]
        
            