# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Basic binary search
        """
        start =1 
        end = n
        mid = start+math.floor((end-start)/2)
        while start<=end:
            currCall = guess(mid)
            if currCall==0:
                return mid
            if currCall == -1:
                end = mid-1
            else:
                start = mid+1
            mid = start+math.floor((end-start)/2)
        return 