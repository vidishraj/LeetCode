##Have to create a trie with the root node and so on 
class trieNode:
    isEndOfWord: bool
    nextLayer: dict

    def __init__(self):
        self.isEndOfWord = False
        self.nextLayer = {}

    def checkIfLetterInNextLayer(self, letter):
        if self.nextLayer.get(letter):
            return True
        return False

    def getNextLayer(self, letter):
        return self.nextLayer[letter]

    def addNextLayer(self, letter):
        self.nextLayer[letter] = trieNode()
        return


class Solution:
    rootNode: trieNode
    longestPrefix: int

    def addWordToRoot(self, word):
        currentNode = self.rootNode
        for index, letter in enumerate(word):
            if currentNode.checkIfLetterInNextLayer(letter):
                if index == len(word) - 1:
                    currentNode.isEndOfWord = True
            else:
                currentNode.addNextLayer(letter)
            currentNode = currentNode.getNextLayer(letter)

    def checkIfLongestFound(self, word):
        currentNode = self.rootNode
        for index, letter in enumerate(word):
            if currentNode.checkIfLetterInNextLayer(letter):
                currentNode = currentNode.getNextLayer(letter)
            else:
                break
            if self.longestPrefix < index+1:
                self.longestPrefix = index+1

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1.sort()
        arr2.sort()
        self.rootNode = trieNode()
        self.longestPrefix = 0
        for i in range(len(arr1)):
            self.addWordToRoot(str(arr1[i]))
        for j in range(len(arr2)):
            self.checkIfLongestFound(str(arr2[j]))
        return self.longestPrefix

