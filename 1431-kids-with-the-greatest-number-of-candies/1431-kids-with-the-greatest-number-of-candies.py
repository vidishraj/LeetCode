class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if candy+extraCandies>=max(candies) else False for candy in candies]
        