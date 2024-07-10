class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Seems easy, remember the last point of deletion, in case of another zero encountered, reset the pointer to after the last deletion 
        in our total, we will remove, lastDeletionIndex-i items and add j-lastDeletionIndex items
        """
        i = 0
        j= 0 
        lastDeletionIndex = None
        deleted= False
        longestOnes = 0
        res = 0 
        while j<len(nums):
            if nums[j]==1:
                longestOnes+=1
                j+=1
            else:
                if deleted:
                    itemsToRemove = lastDeletionIndex-i
                    longestOnes-=itemsToRemove
                    i = lastDeletionIndex+1
                    deleted=False
                    
                else:
                    deleted = True #Acknowledge deletion
                    lastDeletionIndex = j
                    j+=1 #Move ahead
            if res<longestOnes:
                res = longestOnes
        if lastDeletionIndex == None:
            #no deletions
            return len(nums)-1
        return res