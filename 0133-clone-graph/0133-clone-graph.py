import queue

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        We want to run BFS and keep all the nodes in a separate dicts so that we can refer to their neighbours
        while creating our graph.

        eg. For 1-> we create 2 and 4 and insert 1 in both their neighbours
        we insert the actual neighbours in our queues
        now we reach 
        2-> for 2, we already have 1 in our neighbours. We refer the actual dict-> interate thorugh it 
        create new nodes insert it while cloning.
        Now we have inserted 3 
        We also need a visited array during the dfs
        [1, 2, 3, 4]
        [1->[2, 4], ]
        referList-> [1, 2, 4]
        """
        if node is None:
            return None
        visited = {}
        q = queue.Queue()
        q1 = queue.Queue()
        q.put(node)
        visited[node.val] = True
        while q.qsize() > 0:
            current: Node = q.get()
            q1.put(current)
            for neighbour in current.neighbors:
                if visited.get(neighbour.val) is None:
                    q.put(neighbour)
                    visited[neighbour.val] = True
        

        # DFS DONE

        nodeDict = {}
        startNode = None
        while q1.qsize() > 0:
            curr: Node = q1.get()
            if nodeDict.get(curr.val) is None:
                parentNode = Node()
                parentNode.val = curr.val
                parentNode.neighbors = []
                nodeDict[curr.val] = parentNode
            else:
                parentNode = nodeDict[curr.val]
            if startNode is None:
                startNode = parentNode
            for neighbour in curr.neighbors:
                if nodeDict.get(neighbour.val) is None:
                    childNode = Node()
                    childNode.val = neighbour.val
                    childNode.neighbors = []
                else:
                    childNode = nodeDict[neighbour.val]
                parentNode.neighbors.append(childNode)
                nodeDict[childNode.val] = childNode
        return startNode