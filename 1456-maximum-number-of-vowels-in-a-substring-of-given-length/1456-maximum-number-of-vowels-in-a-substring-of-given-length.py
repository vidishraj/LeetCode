class Solution(object):
    def maxVowels(self, s, k):
        maxi=0
        count=0
        for i in range(k):
            if s[i] in "aieou":
                count+=1
        
        maxi=count
        i=0
        j=k
        while j<len(s):
            if s[i] in "aieou":
                count-=1
            if s[j] in "aieou":
                count+=1
            if count>maxi:
                maxi=count
            i+=1
            j+=1
        return maxi
        