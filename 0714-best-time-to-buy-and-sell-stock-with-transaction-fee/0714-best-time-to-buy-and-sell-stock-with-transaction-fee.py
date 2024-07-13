class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(2):
                if j == 1:
                    dp[i][j] = max(dp[i+1][j], dp[i+1][0] - prices[i])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i+1][1] + prices[i] - fee)
                
        return dp[0][1]