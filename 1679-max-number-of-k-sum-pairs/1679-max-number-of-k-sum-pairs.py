from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        It is sort of like two sum
        """
        occurDict = defaultdict(int)
        for num in nums:
            occurDict[num]+=1
        res=0
        for num in nums:
            if num<k and k-num==num:
                if occurDict.get(num)>1:
                    res+=1
                    occurDict[num]-=2
            else:
                if num<k and occurDict.get(k-num) is not None and occurDict[k-num]>0 and occurDict[num]>0:   
                    res+=1
                    occurDict[num]-=1
                    occurDict[k-num]-=1
        return res
        