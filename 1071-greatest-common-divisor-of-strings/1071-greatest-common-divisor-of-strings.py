class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        find pattern in either of the string
        """
        pattern = None
        for i in range(0,int(len(str1)/2)+1):
            current = str1[0:i+1]
            patternMod = len(str1)%len(current)
            patternDic = int(len(str1)/len(current))
            if patternMod==0 and current*patternDic==str1:
                pattern = str1[0:i+1]
                break
        if pattern is None:
            return ""
        else:
            largestPattern = None
            initPattern = pattern
            start = 1
            while len(pattern)<=len(str1):
                if pattern*int(len(str1)/len(pattern))==str1 and pattern*int(len(str2)/len(pattern))==str2:
                    largestPattern = pattern
                pattern+=initPattern
            if largestPattern is None:
                return ""
            return largestPattern
        return ""
                
                