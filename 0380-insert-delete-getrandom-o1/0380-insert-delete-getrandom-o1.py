import random


class RandomizedSet:
    insertionObject: dict

    def __init__(self):
        self.insertionObject = {}

    def insert(self, val: int) -> bool:
        if self.insertionObject.get(val) is None:
            self.insertionObject[val] = True
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        #Equal probability of returning any item
        if self.insertionObject.get(val) is None:
            return False
        else:
            # self.insertionObject[val] = False
            self.insertionObject.pop(val)
            return True

    def getRandom(self) -> int:
        keyList = list(self.insertionObject.keys())
        randomIndex = random.Random().randint(0, len(keyList)-1)
        return keyList[randomIndex]
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()