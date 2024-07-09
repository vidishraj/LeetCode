from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        When can a string not be converted to another string?
        i) Not the same length
        ii) One has chars that the other doesnt have.
        iii) The occurence of chars in both should be the same.
        """
        
        #Length check
        if len(word1)!=len(word2):
            return False 
        char1Dict = defaultdict(int)
        char2Dict = defaultdict(int)
        for char in word1:
            char1Dict[char]+=1
        for char in word2:
            char2Dict[char]+=1
            
        #unique char check
        for key in list(char1Dict.keys()):
            if char2Dict.get(key) is None:
                return False
        for key in list(char2Dict.keys()):
            if char1Dict.get(key) is None:
                return False
        
        #Non-unique occurence check
        char1Values = char1Dict.values()
        char2Values = char2Dict.values()
        occurenceDict1= defaultdict(int)
        occurenceDict2= defaultdict(int)
        for value in char1Values:
            occurenceDict1[value]+=1
        for value in char2Values:
            occurenceDict2[value]+=1
        for key in list(occurenceDict1.keys()):
            if occurenceDict2.get(key)!=occurenceDict1[key]:
                return False
        for key in list(occurenceDict2.keys()):
            if occurenceDict1.get(key)!=occurenceDict2[key]:
                return False
        return True
        