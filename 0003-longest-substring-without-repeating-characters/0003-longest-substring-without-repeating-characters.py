class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sounds like a sliding window question. 
        
        """
        
        left = 0
        right = 0 
        existDict = {}
        res = 0
        curr = 0 
        while right<len(s) and left<=right:
            if existDict.get(s[right]) is None:
                existDict[s[right]] = True
                
                # print("adding",right, s[right])
                right+=1
                curr+=1
                res = max(res, curr)
            else:
                #found repition
                while s[left]!=s[right]:
                    del existDict[s[left]]
                    # print("removing", left, s[left])
                    left+=1
                    curr-=1
                left+=1
                curr-=1
                del existDict[s[right]]
                # print("removing", left, s[right])
        # print(res)
        return max(res, curr)