from copy import deepcopy
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        If there is an obstacle in the path, we will not be caring about the paths out that shit
        """
        if obstacleGrid[0][0]==1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0] = 1
        for i in range(cols):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i] = 1
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[rows-1][cols-1]
                    
            