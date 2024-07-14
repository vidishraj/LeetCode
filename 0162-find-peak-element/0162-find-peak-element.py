class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        if len(nums)<3:
            return nums.index(max(nums))
        end = len(nums)-1
        mid = start +math.floor((end-start)/2)
        
        #If we reach the boundary, that means that we have one of the elements as peak
        while start<=end:
            # print(mid)
            if (mid-1<0 or nums[mid]>nums[mid-1]) and (mid+1>=len(nums) or nums[mid]>nums[mid+1]):
                return mid
            if nums[mid]<nums[mid+1]:
                start = mid+1
            else:
                end = mid-1
            mid = start +math.floor((end-start)/2)
        # print(start, end, mid)
        return nums.index(max(nums[0], nums[-1]))