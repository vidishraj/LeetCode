class TrieNode:
    letterMap: dict
    isEndOfWord: bool

    def __init__(self):
        self.letterMap = {}
        self.isEndOfWord = False

    def get(self, letter):
        if self.letterMap is None:
            return None
        return self.letterMap.get(letter)

    def set(self, letter):
        self.letterMap[letter] = TrieNode()
        return

    def setIsEndOfWord(self):
        self.isEndOfWord = True

    def printItems(self):
        print(self.letterMap, self.isEndOfWord)


class Trie:
    letterMap: TrieNode

    def __init__(self):
        self.letterMap = TrieNode()

    def insert(self, word: str) -> None:
        currentNode: TrieNode = self.letterMap
        for i in range(0, len(word)):
            if currentNode.get(word[i]) is None:
                currentNode.set(word[i])
                currentNode = currentNode.get(word[i])
            else:
                currentNode = currentNode.get(word[i])
        currentNode.setIsEndOfWord()

    def search(self, word: str) -> bool:
        currentNode: TrieNode = self.letterMap.get(word[0])
        for i in range(1, len(word)):
            if currentNode is None:
                return False
            else:
                currentNode = currentNode.get(word[i])
        if currentNode is None:
            return False
        if currentNode.isEndOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        currentNode: TrieNode = self.letterMap.get(prefix[0])
        for i in range(1, len(prefix)):
            if currentNode is None:
                return False
            else:
                currentNode = currentNode.get(prefix[i])
            
        if currentNode is None:
            return False
        return True

