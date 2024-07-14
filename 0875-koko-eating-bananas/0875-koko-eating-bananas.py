class Solution:
    
    def feasible(self, speed, piles, hours):
        timeTakenAtSpeed = 0
        for pile in piles:
            timeTakenAtSpeed+=math.ceil(pile/speed)
        if timeTakenAtSpeed<=hours:
            return True
        return False
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Maximum for Koko is that he should eat either the max in the pile or 1-n where n is the max in the pile
        We need to run binary search on this and find the right one
        """
        maximum = max(piles)
        start = 1
        end = maximum
        mid = start +math.floor((end-start)/2)
        while(start<=end):
            if self.feasible(mid, piles, h):
                end = mid-1
            else:
                start=mid+1
            mid = start +math.floor((end-start)/2)
        return start