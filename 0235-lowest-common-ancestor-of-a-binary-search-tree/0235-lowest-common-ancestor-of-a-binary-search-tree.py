# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Run bfs and store level wise node of the tree, if p has ancestor y, remember y.
            If the other required node is on the same level. Return the ancestor. 
            otherwise return p.
        How do we remember the current level?-> Remember the q length before checking child. Make sure to consume
        only that many and increase the steps.  
        """

        if p.val == root.val or q.val == root.val:
            return root
        que = queue.Queue()
        temp = root 
        que.put(temp)
        ancestorDict = {}
        ancestorP = None
        ancestorQ = None
        # print(ancestorDict, ancestorP, ancestorQ)
        while(que.qsize()!=0):
            nodesToConsume = que.qsize()
            consumed = 0
            while consumed!=nodesToConsume:
                curr = que.get()
                consumed+=1
                if curr.left:
                    ancestorDict[curr.left.val] = [curr.val, curr]
                    if curr.left.val == p.val:
                        ancestorP = curr.val
                    if curr.left.val == q.val:
                        ancestorQ = curr.val
                    que.put(curr.left)
                if curr.right: 
                    ancestorDict[curr.right.val] = [curr.val, curr]
                    if curr.right.val == p.val:
                        ancestorP = curr.val
                    if curr.right.val == q.val:
                        ancestorQ = curr.val
                    que.put(curr.right)
            if ancestorP is not None and ancestorQ is not None:
                break
            # if ancestorP is not None:
            #     return p
            # if ancestorQ is not None:
            #     return q 
        # print(ancestorDict)
        pAncestorDict = []
        qAncestorDict = []
        check = True
        check2 = []
        while check:
            try:
                if len(check2) == 0:
                    check2.append(ancestorDict[p.val][0])
                    pAncestorDict.append(ancestorDict[p.val][1])

                    if ancestorDict[p.val][0] == q.val:
                        return ancestorDict[p.val][1]
                pAncestorDict.append(ancestorDict[ancestorP][1])
                if ancestorDict[ancestorP][0] == q.val:
                    return ancestorDict[ancestorP][1]
                check2.append(ancestorDict[ancestorP][0])
                ancestorP = ancestorDict[ancestorP][0]
            except:
                check = False
        check=True
        check2=[]
        while check:
            try:
                if len(check2) == 0:
                    check2.append(ancestorDict[q.val][0])
                    qAncestorDict.append(ancestorDict[q.val][1])
                    if ancestorDict[q.val][0] == p.val:
                        return ancestorDict[q.val][1]
                qAncestorDict.append(ancestorDict[ancestorQ][1])
                if ancestorDict[ancestorQ][0] == p.val:
                    return ancestorDict[ancestorQ][1]
                check2.append(ancestorDict[ancestorQ][0])
                ancestorQ = ancestorDict[ancestorQ][0]
            except:
                check = False
        for i in range(len(pAncestorDict)):
            for j in range(len(qAncestorDict)):
                if pAncestorDict[i].val==qAncestorDict[j].val:
                    return pAncestorDict[i]
        # print(ancestorP, ancestorQ) 
        # if ancestorQ == p.val:
        #     return p
        # if ancestorP == q.val:
        #     return q
        # while ancestorP!=ancestorQ:
        #     ancestorP = ancestorDict[ancestorP][0]
        #     ancestorQ = ancestorDict[ancestorQ][0]
        
        # if ancestorP==root.val:
        #     return root 
        # return ancestorDict[ancestorP][1]
        return root
        