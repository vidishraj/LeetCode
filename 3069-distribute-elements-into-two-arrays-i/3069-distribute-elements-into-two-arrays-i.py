class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[0]]
        for i in range(1, len(nums)):
            if(arr1[-1]>arr2[-1]):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for index, item in enumerate(arr2):
            if index!=0:
                arr1.append(item)
        return arr1