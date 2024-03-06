class Solution:
    maximumLength: int
    index: int

    def checkContinuation(self, string: str, startIndex: int, k ):
        commonLength = 0
        for i in range(startIndex, len(string)):
            if string[i] == string[i - i + commonLength]:
                commonLength += 1
            else:
                return
            if i == len(string) - 1 and self.maximumLength < commonLength:
                if commonLength>startIndex:
                    if startIndex%k==0:
                        self.maximumLength = commonLength
                        self.index = startIndex    
                else:
                    self.maximumLength = commonLength
                    self.index = startIndex

    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        self.maximumLength = 0
        self.index = len(word) + 1
        firstLetter = word[0]
        for i in range(k, len(word)):
            if word[i] == firstLetter and len(word) - k > self.maximumLength and i%k==0:
                self.checkContinuation(word, i, k)
        if self.index == len(word) + 1:
            return math.ceil(len(word) / k)
        if self.index % k == 0:
            return int(self.index / k)
        return int((self.index / k) + 1)