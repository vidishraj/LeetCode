# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    solution:list
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            Keep travelling right and remember the nodes encountered? Wouldnt work
            Keep a queue and add the last item seen on this level
        """
        
        if root is None:
            return []
        
        self.solution = []
        q= queue.Queue()
        q.put(root)
        currentLevel = 1
        while q.qsize()!=0:
            prevLevel = currentLevel
            currentLevel = 0
            nextLevelAdded = 0
            while currentLevel!= prevLevel:
                curr = q.get()
                if curr.left:
                    q.put(curr.left)
                    nextLevelAdded+=1
                if curr.right:
                    q.put(curr.right)
                    nextLevelAdded+=1
                if currentLevel==prevLevel-1:
                    self.solution.append(curr.val)
                currentLevel+=1
            currentLevel = nextLevelAdded
        return self.solution