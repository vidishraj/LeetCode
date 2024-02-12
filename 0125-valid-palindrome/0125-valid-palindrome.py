import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        difference = 97 - 65
        i = 0
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]','',s)
        j = len(s) - 1
        while (i < j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
