class Solution(object):
    
    def getUniqueId(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)
    
    def groupAnagrams(self, nums):
        result=[]
        itemDict = {}
        for num in nums:
            if itemDict.get(self.getUniqueId(num)) is not None:
                itemDict[self.getUniqueId(num)].append(num)
            else:
                itemDict[self.getUniqueId(num)]=[num]
        result.extend(itemDict.values())
        return result