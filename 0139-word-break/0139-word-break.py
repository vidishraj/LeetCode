class Solution:
    wordDict:dict
    dp:dict
        
    # @lru_cache(maxsize=None)
    def rec(self, word, startIndex, endIndex):
        """
        """
        if endIndex>len(word):
            return False # base case 1
        currentWord = word[startIndex:endIndex]
        if self.wordDict.get(currentWord) is not None:
            # Winning match
            # print(currentWord)
            if endIndex == len(word):
                return True
            acceptSol = False
            rejectSol = False
            if self.dp.get(f"{startIndex}-{endIndex+1}") is not None:
                acceptSol = self.dp.get(f"{startIndex}-{endIndex+1}") #accept the word
            else:
                acceptSol = self.rec(word, startIndex, endIndex+1) #accept the word
            if self.dp.get(f"{endIndex}-{endIndex+1}") is not None:
                rejectSol = self.dp.get(f"{endIndex}-{endIndex+1}") #accept the word             
            else:
                rejectSol = self.rec(word, endIndex, endIndex+1) # disregard the word
            self.dp[f"{startIndex}-{endIndex}"] = acceptSol or rejectSol
            return acceptSol or rejectSol
        else:
            if self.dp.get(f"{startIndex}-{endIndex+1}") is not None:
                return self.dp.get(f"{startIndex}-{endIndex+1}") #accept the word
                
            else:
                sol = self.rec(word, startIndex, endIndex+1) # No match we move forward
                self.dp[f"{startIndex}-{endIndex}"] = sol
                return sol
                
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            The idea is to start from the beginning, call rec function from beginning
            winning case is reaching end of the string and it being a match
            base case is surpassing the end of the string also a losing case
            on every match, we need to call rec two time, once-> Two accept the current solution/ Once to move ahead without accepting the current solution 
            Try using lruCache?
        """
        self.wordDict = {}
        self.dp = {}
        for word in wordDict:
            self.wordDict[word] = True
        return self.rec(s, 0, 1)
        
        