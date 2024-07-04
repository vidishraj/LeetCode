class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Usual n2 solution would be to use dp and mark all single letter and two letter patterns as true
        and then run a nested for loop to build our dp array. 
        How to get total count. 
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                dp[i][i+1] = True
                dp[i+1][i] = True
        res = 0
        n = len(s)
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res
            
