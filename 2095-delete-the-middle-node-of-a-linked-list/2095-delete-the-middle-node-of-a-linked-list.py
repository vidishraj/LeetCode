# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Count the number of items in the list.
        Find the middle point
        Keep a trailing pointer
        Rearrange
        """
        
        count=0
        temp = head
        while temp:
            count+=1
            temp=temp.next
        middleElement = math.floor(count/2)
        tempTrail = head
        temp = head
        runningCount = 0
        if count == 1 or count == 0:
            return None
        while tempTrail:
            if runningCount == middleElement:
                tempTrail.next = temp.next
                return head
            tempTrail = temp
            temp = temp.next
            runningCount += 1
        return head