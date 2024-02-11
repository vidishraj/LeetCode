class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        """
        Idea is straight forward,
        step 1-> parse n words till the number of letters in the n words + n(spaces between them) is <== maxWidth

        step 2-> if equal, just push the sentence into our solution list
                 else, since its greater, we will take the sentence till the second last word,
                 The spaces will be equal to maxWidth - len(wordTaken).
        step 3->  To divide the spaces, we need to check if it can be divided evenly between words.
                    The formula will be (number of spaces)%(number of words-1)==0?
                     =>(number of spaces)/(numberOfWords-1) spaces should be inserted between words :
                    else we need to put (number of spaces)/(numberOfWords-1)+(number of spaces)%(number of words-1)+1 after
                    the first word, rest get  (number of spaces)/(numberOfWords-1) spaces.
        step 4-> Follow the steps for the last word.
        :param words: list of words
        :param maxWidth: width to be followed
        :return: list of sentences
        """
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
                    # print(currentString,numberOfSpaces,numberOfWords)
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
                            # print(currentString)
                            # print(numberOfSpaces)
                            # print(currentWords)
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
            # last sentence case

        return listOfSentences


