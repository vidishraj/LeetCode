# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkIfNodeExists(self, root, key):
        if root is None:
            return False
        if root.val == key:
            return True
        return self.checkIfNodeExists(root.left, key) or self.checkIfNodeExists(root.right, key)

    def checkChildren(self, root, key):
        if root is None:
            return None
        if root.val == key:
            if root.left and root.right:
                return [4, root]
            if not root.left and not root.right:
                return [3, root]
            if root.right:
                return [2, root]
            if root.left:
                return [1, root]
        leftTreeCheck = self.checkChildren(root.left, key)
        rightTreeCheck = self.checkChildren(root.right, key)

        if leftTreeCheck is not None:
            return leftTreeCheck
        return rightTreeCheck

    def findRightMostChild(self, deletionNode):
        rightMostChild = deletionNode.left
        while rightMostChild.right:
            rightMostChild = rightMostChild.right
        return rightMostChild

    def findLeftMostChild(self, deletionNode):
        leftMostChild = deletionNode.right
        while leftMostChild.left:
            leftMostChild = leftMostChild.left
        return leftMostChild

    def deleteLeaf(self, root, deletionNode):
        if root is None:
            return None
        if root.left == deletionNode or root.right == deletionNode:
            if root.left == deletionNode:
                root.left = None
                return root
            root.right = None
            return root
        leftCheck = self.deleteLeaf(root.left, deletionNode)
        rightCheck = self.deleteLeaf(root.right, deletionNode)
        if leftCheck:
            return leftCheck
        return rightCheck

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            Three possibilities while deleting
            No children-> Just delete the node
            1 child-> 2 sub cases
                Sub case 1-> left subtree-> Replace deletion node with the rightmost node of the left subtree and delete leaf.
                Sub case 2-> right subtree-> Replace deletion node with the leftmost node of the right subtree and delete leaf.
            2 children-> go to the left most child of the right child of the deletion node. Replace and delete leaf.

        Flow-> Check if node is there -> If there delete-> Else return root
        """
        if not root:
            return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            
        if self.checkIfNodeExists(root, key):
            # 1 for only left, 2 for only right, 3 for not children, 4 for 2 children
            checkRes = self.checkChildren(root, key)
            childCount = checkRes[0]
            deletionNode = checkRes[1]
            if childCount == 1:
                rightMostChild = self.findRightMostChild(deletionNode)
                rightMostChild.val, deletionNode.val = deletionNode.val, rightMostChild.val
                self.deleteNode(root, key)
            elif childCount == 2:
                leftMostChild = self.findLeftMostChild(deletionNode)
                leftMostChild.val, deletionNode.val = deletionNode.val, leftMostChild.val
                self.deleteNode(root, key)
            elif childCount == 3:
                self.deleteLeaf(root, deletionNode)
            else:
                leftMostChild = self.findLeftMostChild(deletionNode)
                leftMostChild.val, deletionNode.val = deletionNode.val, leftMostChild.val
                
                self.deleteNode(root, key)
        return root
