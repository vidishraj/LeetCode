class Solution:
    globalMaximum :int
        
    def maxUniqueSplit(self, s: str) -> int:
        """
        The choice seems to be about wheteher we split at a point or not.
        Write a recurrsive function. 
        Base condition-> Reach the end of the parent string (positive condition-> Check with global maximum) Beyond length-> Failing condition
        Else-> Increase the functional variable for maximum till now, split and call function again.
        Dont split, dont increase, just increase splitting index and move forward.
        
        Later we will need to keep all this in memory
        
        """
        
        self.globalMaximum = 0
        occurrenceDict = {}
        self.rec(0, 1, 0, s, occurrenceDict.copy())
        return self.globalMaximum
        
        
    def rec(self, splitIndex, currIndex, maximum, s, occurrenceDict):
        # print(splitIndex,currIndex,s[splitIndex:currIndex+1])
        if currIndex==len(s):
            if occurrenceDict.get(s[splitIndex:currIndex]) is None and self.globalMaximum<maximum+1:
                # Success in splitting
                if maximum+1==10:
                    print(occurrenceDict, currIndex, splitIndex)
                self.globalMaximum = maximum+1
                return
        if currIndex>len(s):
            return 
        self.rec(splitIndex, currIndex+1, maximum, s, occurrenceDict.copy())
        # This split has not occurred     
        if occurrenceDict.get(s[splitIndex:currIndex]) is None:
            occurrenceDict[s[splitIndex:currIndex]] = True
            self.rec(currIndex,currIndex+1, maximum+1, s, occurrenceDict.copy())
            
            
        