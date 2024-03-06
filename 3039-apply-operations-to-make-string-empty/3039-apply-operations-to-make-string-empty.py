from collections import defaultdict


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        """
        The idea is simple. We keep a dictionary for the count and we keep a dictionary for the last possible positions
        of the letters
        :param s: The input string
        :return: The final number before erasure.
        """
        countDict: defaultdict = defaultdict(int)
        positionDict: dict = {}
        for index, letter in enumerate(s):
            countDict[letter] += 1
            if positionDict.get(letter) is None:
                positionDict[letter] = index
            else:
                positionDict[letter] = index
        sortedKeyList = sorted(countDict, key=countDict.get, reverse=True)
        highestCount = countDict[sortedKeyList[0]]
        finalOrderDict = {}
        for key in sortedKeyList:
            if countDict[key] < highestCount:
                break
            finalOrderDict[positionDict[key]] = key

        sorted_dict = dict(sorted(finalOrderDict.items()))
        finalStringList = [finalOrderDict[item] for item in sorted_dict]
        return "".join(finalStringList)