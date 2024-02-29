# Definition for a binary tree node.
from queue import Queue


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return False
        else:
            q = Queue()
            q.put(root)
            currentLevelCount = 1
            current: bool = False
            while q.qsize() != 0:
                nextLevelCount = 0 
                currentLevelVal = 0
                lastSeenValue = None
                while currentLevelVal != currentLevelCount:
                    currentNode: TreeNode = q.get()
                    if currentNode.left:
                        q.put(currentNode.left)
                        nextLevelCount += 1
                    if currentNode.right:
                        q.put(currentNode.right)
                        nextLevelCount += 1
                    if currentLevelVal == 0:
                        if  not current:  # value should be odd and increasing left to right
                            if currentNode.val % 2 == 0:
                                return False
                        else:  # val should be even and decreasing left to right
                            if currentNode.val % 2 != 0:
                                return False
                        lastSeenValue = currentNode.val
                    else:
                        if not current:
                            if currentNode.val % 2 == 0 or lastSeenValue >= currentNode.val:
                                return False
                        else:
                            if currentNode.val % 2 != 0 or lastSeenValue <= currentNode.val:
                                return False
                        lastSeenValue = currentNode.val
                    currentLevelVal += 1
                currentLevelCount = nextLevelCount
                current = not current
            return True
