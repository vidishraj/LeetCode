class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        listOfSentences: list = []
        currentStringLength = 0
        currentString = ""
        index = 0
        currentWords = 0
        while index < len(words):
            word = words[index]
            currentString += f"{word}1"
            currentWords += 1
            if len(currentString)-1 >= maxWidth:
                if len(currentString)-1 == maxWidth:
                    currentString = currentString[0:-1]
                    numberOfSpaces = maxWidth - currentStringLength
                    numberOfWords = currentWords
                    if numberOfWords-1==0:
                        currentString= currentString.replace("1", '')
                    else:
                        spaces = int(numberOfSpaces / (numberOfWords-1)) * ' '
                        currentString= currentString.replace("1", ' ')
                    listOfSentences.append(currentString)
                    index+=1
                else:
                    currentString = currentString[0:len(currentString) - len(words[index]) - 1]
                    currentWords -= 1
                    currentStringLength = len(currentString) - currentWords

                    currentString = currentString[0:-1]
                    numberOfSpaces = maxWidth - currentStringLength
                    numberOfWords = currentWords
                    if numberOfWords-1==0:
                        spaces = numberOfSpaces*" "
                        currentString+=spaces
                        listOfSentences.append(currentString)
                    else:
                        if numberOfSpaces % (numberOfWords-1) == 0:
                            spaces = int(numberOfSpaces / (numberOfWords-1)) * ' '
                            currentString = currentString.replace("1", spaces)
                            listOfSentences.append(currentString)
                        else:
                            increasedSpaces = (int(numberOfSpaces / (numberOfWords-1)) + 1) * ' '
                            remainingSpace = int(numberOfSpaces / (numberOfWords-1)) * ' '
                            currentString = currentString.replace("1", increasedSpaces, numberOfSpaces%(numberOfWords-1))
                            currentString = currentString.replace("1", remainingSpace)
                            listOfSentences.append(currentString)
                currentWords = 0
                index -= 1
                currentString = ""
            index += 1
            
        if len(currentString) > 0:
            currentStringLength = len(currentString) - currentWords
            currentString=currentString[0:-1]
            numberOfSpaces= maxWidth - currentStringLength
            endOfTheSentenceSpaces = (numberOfSpaces-(currentWords-1))*' '
            currentString=currentString.replace('1',' ')
            currentString+=endOfTheSentenceSpaces
            listOfSentences.append(currentString)

        return listOfSentences


