
class Solution:
    def rec(self, node, leafNodes):
        if node is None:
            return
        if node.left is None and node.right is None:
            leafNodes.append(node)
            return
        self.rec(node.left, leafNodes)
        self.rec(node.right, leafNodes)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        firstLeafNode = []
        secondLeafNode = []
        self.rec(root1, firstLeafNode)
        self.rec(root2, secondLeafNode)
        if len(firstLeafNode)!=len(secondLeafNode):
            return False
        for i in range(len(firstLeafNode)):
            if firstLeafNode[i].val!=secondLeafNode[i].val:
                return False
        return True