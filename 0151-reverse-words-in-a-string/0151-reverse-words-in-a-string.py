class Solution:
    def reverseWords(self, s: str) -> str:
        back=-1
        start=0
        s.strip()
        stringList = s.split()
        # print(stringList)
        while(start<=len(stringList)+back):
            # print(start, len(stringList)+back)
            temp = stringList[start]
            stringList[start] = stringList[back]
            stringList[back]=temp
            start+=1
            back-=1
        return " ".join(stringList)
            