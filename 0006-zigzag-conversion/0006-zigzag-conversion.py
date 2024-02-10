class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        numRows-=1
        objectTree =[]
        for letter in s:
            objectTree.append({
                "letter": letter,
                "index" : (None ,None)
            })
        patternFlag = False
        startColumn = 0
        startRow = 0

        for letterObject in objectTree:
            if patternFlag:
                letterObject["index"] = (startColumn, startRow)
                startRow -= 1
                startColumn += 1
                if startRow == 0:
                    patternFlag = False
            else:
                letterObject["index"] = (startColumn, startRow)
                startRow += 1
                if startRow == numRows:
                    patternFlag = True
        stringLineList = []
        for i in range(0, numRows+1):
            stringLineList.append("")
        for letterObject in objectTree:
            rowNumber = letterObject["index"][1]
            lineString = stringLineList[rowNumber]
            lineString=lineString+letterObject["letter"]
            stringLineList[rowNumber]=lineString
        return ''.join(stringLineList)