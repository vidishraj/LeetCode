class RandomizedSet:
    itemExists:dict
    items:list
    deleteCount:int
    def __init__(self):
        self.items = []
        self.itemExists = {}
        self.deleteCount = 0
    def insert(self, val: int) -> bool:
        if(self.itemExists.get(val) is None):
            self.items.append(val)
            self.itemExists[val]=len(self.items)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.itemExists.get(val) is None:
            return False
        else:
            if len(self.items)==1:
                self.itemExists[val] = None
                self.items=[]
                return True
            index = self.itemExists[val]
            self.itemExists[val] = None
            self.items[index] = self.items[len(self.items)-1]
            self.itemExists[self.items[len(self.items)-1]] = index
            self.items[len(self.items)-1]= val
            self.items.pop()
            del self.itemExists[val]
            self.deleteCount+=1
            return True

    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.items)-1)
        # print(randomIndex)
        return self.items[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()