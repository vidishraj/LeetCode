class CLL:
    val:int
    next = None

    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:


    def findTheWinner(self, n: int, k: int) -> int:
        """
        Can just represent it in the form of a CLL.
        """
        startNode = None
        curr = None
        for i in range(1,n+1):
            if startNode == None:
                startNode = CLL(i, None)
                curr  = startNode
            else:
                newNode = CLL(i, None)
                curr.next= newNode
                curr = curr.next
        curr.next = startNode
        #CLL initialsied.
        #Let the games begin
        nodesRemoved = 0 
        newPrev = curr
        newCurr = startNode
        while nodesRemoved<n-1:
            nodesTraveled = 1
            while nodesTraveled<k:
                newPrev = newCurr
                newCurr = newCurr.next
                nodesTraveled+=1
            newPrev.next = newCurr.next #node detached
            newCurr = newCurr.next
            nodesRemoved+=1
        return newCurr.val
        