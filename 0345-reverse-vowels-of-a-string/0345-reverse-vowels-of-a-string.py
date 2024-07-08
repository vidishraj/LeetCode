class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelsInWord = ""
        for letter in s:
            if letter in vowels:
                vowelsInWord+=letter
        vowelsInWord=vowelsInWord[::-1]
        curr = 0
        finalString = ""
        for index,letter in enumerate(s):
            if letter in vowels:
                finalString += vowelsInWord[curr]
                curr+=1
            else:
                finalString+=letter
        return finalString