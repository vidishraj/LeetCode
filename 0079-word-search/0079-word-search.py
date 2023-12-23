import copy

class Solution:
    def recursiveBFS(self, matrix, word, wordIndex, i, j, visited):
        visited[i][j] = True
        # print(wordIndex, i, j, visited)
        if wordIndex == len(word):
            return True
        if i + 1 < len(matrix) and matrix[i + 1][j] == word[wordIndex] and not visited[i + 1][j]:
            if self.recursiveBFS(matrix, word, wordIndex + 1, i + 1, j, copy.deepcopy(visited)):
                return True
        if i - 1 > -1 and matrix[i - 1][j] == word[wordIndex] and not visited[i - 1][j]:
            if self.recursiveBFS(matrix, word, wordIndex + 1, i - 1, j, copy.deepcopy(visited)):
                return True
        if j + 1 < len(matrix[i]) and matrix[i][j + 1] == word[wordIndex] and not visited[i][j + 1]:
            if self.recursiveBFS(matrix, word, wordIndex + 1, i, j + 1, copy.deepcopy(visited)):
                return True
        if j - 1 > -1 and matrix[i][j - 1] == word[wordIndex] and not visited[i][j - 1]:
            if self.recursiveBFS(matrix, word, wordIndex + 1, i, j - 1, copy.deepcopy(visited)):
                return True
        return False

    def exist(self, matrix, word):
        localVisited = []
        uniqueLetterCount = len(set(word))
        dic ={}
        matrixCount=0
        for row in matrix:
            for letter in row:
                if dic.get(letter)==None:
                    matrixCount+=1
                dic[letter]=1
        if matrixCount<uniqueLetterCount:
            return False
        for i in range(len(matrix)):
            tempArray = []
            for j in range(len(matrix[0])):
                tempArray.append(False)
            localVisited.append(tempArray)
        for outerIndex, row in enumerate(matrix):
            for innerIndex, letter in enumerate(row):
                if letter == word[0]:
                    if self.recursiveBFS(matrix, word, 1, outerIndex, innerIndex, copy.deepcopy(localVisited)):
                        return True
        return False




