# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = queue.Queue()
        q.put(root)
        if root is None:
            return 0
        currentLevel = 1
        res = 0
        while q.qsize()!=0:
            res+=1
            analysed = 0
            prevLevel = currentLevel
            currentLevel = 0
            while analysed != prevLevel:
                curr = q.get()
                if curr.left is not None:
                    q.put(curr.left)
                    currentLevel+=1
                if curr.right is not None:
                    q.put(curr.right)
                    currentLevel+=1
                analysed+=1
            analysed = currentLevel
            
        return res