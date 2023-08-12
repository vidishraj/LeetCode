class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        answerDict = {}
        answer = 0
        for index, reward in enumerate(reward1):
            answerDict[index] = reward - reward2[index]
        sortedDict = dict(sorted(answerDict.items(), key=lambda item: item[1]))
        removedIndicies={}
        for num in sortedDict:
            if len(removedIndicies)<len(reward1)-k:
                removedIndicies[num]=True
        for index in removedIndicies:
            answer+=reward2[index]
        for index, num in enumerate(reward1):
            if removedIndicies.get(index) is None:
                answer+=num
        return answer