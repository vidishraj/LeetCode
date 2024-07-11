# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pathToP:list
    pathToQ:list
    def rec(self, node, targetNode, possiblePath, typeOfHunt):
        if node is None:
            return
        if node.val == targetNode.val:
            possiblePath.append(targetNode.val)
            if typeOfHunt == "P":
                self.pathToP = possiblePath
            else:
                self.pathToQ = possiblePath
            return
        possiblePath.append(node.val)
        self.rec(node.left, targetNode, possiblePath.copy(), typeOfHunt)
        self.rec(node.right, targetNode, possiblePath.copy(), typeOfHunt)
    
    def findNode(self, node, item):
        if node is None:
            return
        if node.val == item:
            self.targetNode = node
        self.findNode(node.left, item)
        self.findNode(node.right, item)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        remember the path to the two nodes
        Match the paths after that
        """
        self.rec(root, p, [],"P")
        self.rec(root, q, [],"Q")
        self.targetNode = None
        checkDict = {}
        for item in self.pathToP:
            checkDict[item] = True
        for i in range(len(self.pathToQ)-1,-1,-1):
            if checkDict.get(self.pathToQ[i]) is not None:
                self.findNode(root, self.pathToQ[i])
                return self.targetNode
        return root
        
        