# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Cant think of a way without space
        """
        nodeDict={}
        index=0
        while head:
            nodeDict[index] = head.val
            index+=1
            head = head.next
        globalMax = 0
        for i in range(math.floor(index/2)):
            currentSum = nodeDict[i]+nodeDict[index-1-i]
            if globalMax<currentSum:
                globalMax=currentSum
        return globalMax