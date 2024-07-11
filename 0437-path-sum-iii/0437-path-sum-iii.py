# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    
    res:int
    target:int 
        
    def checkSum(self, node, currentSum:int):
        if node is None:
            return 
        if node.val+currentSum == self.target:
            self.res+=1
        currentSum+=node.val
        self.checkSum(node.left, currentSum)
        self.checkSum(node.right, currentSum)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            Can be fucking complicated. Have to go through every single node and check 
        """
        self.res = 0
        self.target = targetSum
        if root is None:
            return 0
        q = queue.Queue()
        q.put(root)
        while q.qsize()!=0:
            curr = q.get()
            self.checkSum(curr, 0)
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)
        return self.res