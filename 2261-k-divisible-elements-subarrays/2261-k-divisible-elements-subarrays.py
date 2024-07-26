class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        uniqueDicts = {}
        for i in range(len(nums)):
            currString = ""
            currCount = 0
            for j in range(i, len(nums)):
                if nums[j]%p==0:
                    currCount+=1                    
                if currCount > k:
                    break
                currString+=str(nums[j])+","
                uniqueDicts[currString] = True
        return len(list(uniqueDicts.keys()))