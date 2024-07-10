# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Put odd items first and then the even ones
        """
        
        temp = head
        count = 0 
        while temp:
            temp = temp.next
            count+=1
        # No need to rearrage
        if count<3:
            return head
        temp = head #First is odd
        itemsSwapped = 0
        while temp:
            prevTemp = temp
            currTemp = temp
            count = 0 
            while count!=itemsSwapped+2 and currTemp:
                prevTemp = currTemp
                currTemp = currTemp.next
                count+=1
            if currTemp is None:
                return head
            else:
                nextEven = temp.next #2
                lastEven = prevTemp
                nextChain = currTemp.next #4
                temp.next = currTemp
                currTemp.next = nextEven
                lastEven.next=nextChain
                itemsSwapped+=1
            temp=temp.next
        return head
                
        