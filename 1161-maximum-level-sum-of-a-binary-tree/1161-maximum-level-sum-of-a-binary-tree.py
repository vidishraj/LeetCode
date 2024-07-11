# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root.val
        q = queue.Queue()
        q.put(root)
        currentLevel = 1
        globalMax = root.val
        res = 1
        level = 1
        while q.qsize() != 0:
            prevLevel = currentLevel
            currentLevel = 0
            currentLevelAdded = 0
            currentSum = 0
            while currentLevel != prevLevel:
                curr = q.get()
                currentSum += curr.val
                if curr.left:
                    q.put(curr.left)
                    currentLevelAdded += 1
                if curr.right:
                    q.put(curr.right)
                    currentLevelAdded += 1
                currentLevel += 1
            if globalMax < currentSum:
                globalMax = currentSum
                res = level
            currentLevel = currentLevelAdded
            level += 1
        return res
