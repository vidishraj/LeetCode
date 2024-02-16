class Solution:
    def isHappy(self, n: int) -> bool:
        seenItems={}
        currentInt=n
        totalSum=0
        while True:
            while currentInt>0:
                totalSum+=(currentInt%10)*(currentInt%10)
                currentInt=int(currentInt/10)
            if seenItems.get(totalSum) is not None:
                return False
            if totalSum==1:
                return True
            seenItems[totalSum]=True
            currentInt=totalSum
            totalSum=0
        return True
                