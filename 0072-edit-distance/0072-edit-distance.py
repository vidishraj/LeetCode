class Solution:
    dp:any
    def rec(self, word1, word2):
        if self.dp.get(word1) is None:
            self.dp[word1] = {}
        if self.dp[word1].get(word2) is None:
            if not word1:
                return len(word2)
            if not word2:
                return len(word1)
            if word1[0] == word2[0]:
                return self.rec(word1[1:], word2[1:])
            replacement = 1 + self.rec(word1[1:], word2[1:])
            deletion = 1 + self.rec(word1[1:], word2)
            insertion = 1 + self.rec(word1, word2[1:])
            self.dp[word1][word2] = min(replacement, deletion, insertion)
            return min(replacement, insertion, deletion)
        else:
            return self.dp[word1][word2]

    def minDistance(self, word1: str, word2: str) -> int:
        """
            We have to check whether we can remove, duplicate and replace the character
            If the chars match, we can move to the next on e
            For Dp we need to remember the solution for a certain 
        """    
        self.dp = {}
        return self.rec(word1, word2)