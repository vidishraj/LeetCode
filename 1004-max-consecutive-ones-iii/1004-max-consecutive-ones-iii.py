class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        
        """
        i=0
        j=0
        globalMax = 0
        maxOnes = 0
        zeroCount = 0
        while j<len(nums):
            if nums[j] == 1:
                maxOnes+=1
                j+=1
            else:
                if zeroCount == k:
                    while nums[i] != 0:
                        i+=1
                        if maxOnes>0:
                            maxOnes-=1
                    if zeroCount>0:
                        zeroCount-=1
                    if maxOnes>0:
                        maxOnes-=1
                    i+=1
                    if j<i:
                        j=i
                else:
                    zeroCount+=1
                    maxOnes+=1
                    j+=1
            if globalMax<maxOnes:
                globalMax = maxOnes
        return globalMax