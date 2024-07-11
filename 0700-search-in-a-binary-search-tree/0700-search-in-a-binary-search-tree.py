class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        leftVal = self.searchBST(root.left, val)
        rightVal = self.searchBST(root.right, val)
        if leftVal is not None:
            return leftVal
        if rightVal is not None:
            return rightVal
        return None