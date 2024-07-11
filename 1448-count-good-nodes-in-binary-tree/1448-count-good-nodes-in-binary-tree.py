# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    counter:int
    
    def rec(self, node, greatestTillNow:int):
        if node is None:
            return
        if node.val>=greatestTillNow:
            self.counter+=1
            greatestTillNow = node.val
        self.rec(node.left, greatestTillNow)
        self.rec(node.right, greatestTillNow)
        return 
    
    def goodNodes(self, root: TreeNode) -> int:
        """
        We have to essentially iterate through the tree and remember the greatest value encounterd till now 
        If our current Node is greater than the greatest encountered till now, increase the global counter
        """
        self.counter = 0
        self.rec(root, root.val)
        return self.counter