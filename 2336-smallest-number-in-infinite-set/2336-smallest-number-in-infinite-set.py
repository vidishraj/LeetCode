from collections import defaultdict
class SmallestInfiniteSet:
    """
    Can probably use a minHeap? or is this not the implementation of minHeap
    """
    removed:dict
    currentSmallest:int
        
    def __init__(self):
        self.removed = defaultdict(bool) 
        self.currentSmallest = 1

    def popSmallest(self) -> int:
        self.removed[self.currentSmallest] = True
        currSmallest = self.currentSmallest
        tempSmallest = self.currentSmallest +1
        while self.removed[tempSmallest] is not False:
            tempSmallest+=1
        self.currentSmallest = tempSmallest
        return currSmallest

    def addBack(self, num: int) -> None:
        if self.removed.get(num) is True:
            self.removed[num]= False
            if self.currentSmallest>num:
                self.currentSmallest = num
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)