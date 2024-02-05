class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        highDict= {}
        highest = -1
        for index in range(len(prices)-1,-1, -1):
            if prices[index]>highest:
                highest = prices[index]
            highDict[index] = highest
        maxProfit= -1
        for index, item in enumerate(prices):
            if highDict[index]-item>maxProfit:
                maxProfit=highDict[index]-item
        return maxProfit
            