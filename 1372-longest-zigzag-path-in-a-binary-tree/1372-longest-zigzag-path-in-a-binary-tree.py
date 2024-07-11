# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    maximumDepth:int
    dp:dict
    def rec(self, node, currentDirection, currentDepth):
        if node is None:
            return 
        self.dp[node] = currentDepth+1
        if currentDepth>self.maximumDepth:
            self.maximumDepth = currentDepth
        if currentDirection == "Right":
            currentDirection = "Left"
            if self.dp.get(node.right) is None:
                self.rec(node.right, currentDirection, currentDepth+1)
        else:
            currentDirection = "Right"
            if self.dp.get(node.left) is None:
                self.rec(node.left, currentDirection, currentDepth+1)
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Put every node in a queue and iterate through the queue
        """
        
        self.maximumDepth = 0
        self.dp={}
        q= queue.Queue()
        if root is None:
            return 0
        q.put(root)
        while q.qsize()!=0:
            curr = q.get()
            self.rec(curr, "Right", 0)
            self.rec(curr, "Left", 0)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
        return self.maximumDepth
        
        