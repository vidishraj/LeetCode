class Solution:
    
    def rec(self, nums, availMoves, currentIndex):
        if self.dp.get(currentIndex) is not None:
            return self.dp[currentIndex]
        if currentIndex >= len(nums)-1:
            return True
        maxMovesAvailables = max(availMoves, nums[currentIndex])
        if maxMovesAvailables == 0:
            return False
        self.dp[currentIndex+1] = self.rec(nums, maxMovesAvailables - 1, currentIndex+1)
        self.dp[currentIndex+maxMovesAvailables] =  self.rec(nums, 0, currentIndex+maxMovesAvailables)
        return self.dp[currentIndex+1] or self.dp[currentIndex+maxMovesAvailables]
    
    def canJump(self, nums: List[int]) -> bool:
        self.dp = {}
        if len(nums)==1:
            return True
        self.rec(nums, 0, 0)
        if self.dp.get(len(nums)-1) is None:
            return False
        return self.dp.get(len(nums)-1)
        #Choice should be to whether jump the maximum or move one ahead and check the result