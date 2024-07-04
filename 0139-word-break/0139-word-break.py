class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        @lru_cache(None)
        def dp(start):
            if start == n:  # Found a valid way to break words
                return True

            for end in range(start + 1, n + 1):  # O(N^2)
                word = s[start:end]  # O(N)
                if word in wordSet and dp(end):
                    return True
            return False

        return dp(0)