class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        At each point in the matrix, we need to check. We need to move backwards from the bottom of the matrix. 
        Essentially, we move in the opposite direction and fill our dp matrix
        """
        dp = []
        for i in range(len(grid)):
            dp.append([])
            for j in range(len(grid[0])):
                dp[i].append(0)
        dp[0][0] = grid[0][0]
        for i in range(1,len(grid)):
            dp[i][0] += grid[i][0]+dp[i-1][0]
        for i in range(1, len(grid[0])):
            dp[0][i] += grid[0][i]+dp[0][i-1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[-1][-1]
            