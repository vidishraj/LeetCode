class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        We need to find how many number are there that have +1/-1 difference.
        We need to store the boundaries of the sequence
        Straight forward solution would be to sort and check 
        """
        numDict = {}
        res = 0
        for num in nums:
            if numDict.get(num) is None:
                right = 0
                left = 0
                if  numDict.get(num+1) is not None:
                    right = numDict[num+1]
                if  numDict.get(num-1) is not None:
                    left = numDict[num-1]
                sumO = left+right+1
                numDict[num] = sumO
                res = max(sumO, res)

                numDict[num-left] = sumO
                numDict[num+right] = sumO
            else:
                continue
        return res