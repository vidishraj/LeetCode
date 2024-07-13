class Solution:
    def binary_check(self,item, potions, success):
        ##Change the approach. IF mid*item>success, then everyrhing on the right matches, add the items and reduce end. Else increase start
        start= 0 
        end = len(potions)-1
        mid = start+ math.floor((end-start)/2) 
        res = 0
        while start<=end:
            if potions[mid]*item>=success:
                res+=end-mid+1
                end = mid-1
            else:
                start = mid+1
            mid = start+ math.floor((end-start)/2) 
        return res
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Binary search? on the potions after sorting 
        """
        #nlog(n)
        potions.sort()
        fin = []
        for spell in spells:
            fin.append(self.binary_check(spell, potions, success))
        return fin