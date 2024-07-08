class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []
        for candy in candies:
            if candy+extraCandies>=maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res