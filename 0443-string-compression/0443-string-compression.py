class Solution:
    def compress(self, chars: List[str]) -> int:
        runningCount = 0
        currentChar = chars[0]
        strLength = 0
        writingIndex = 0
        for i in range(len(chars)):
            if currentChar == chars[i]:
                runningCount+=1
            else:
                chars[strLength] = currentChar
                strLength+=1 #add the letter
                if runningCount>1:
                    numInStr=str(runningCount)
                    for j in range(len(numInStr)):
                        chars[strLength] = numInStr[j]
                        strLength+=1
                    # print(runningCount, strLength)
                currentChar = chars[i] #assign next char as currentchar
                runningCount = 1 #running count becomes 1
        chars[strLength] = currentChar
        strLength+=1 #add the letter
        if runningCount>1:
            numInStr=str(runningCount)
            for j in range(len(numInStr)):
                chars[strLength] = numInStr[j]
                strLength+=1
        return strLength