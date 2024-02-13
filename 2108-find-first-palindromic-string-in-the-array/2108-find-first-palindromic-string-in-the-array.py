class Solution(object):
    def palindromic(self, string):
        i=0
        j=len(string)-1
        while(i<j):
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True
        
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if self.palindromic(word):
                return word
        return ""
        