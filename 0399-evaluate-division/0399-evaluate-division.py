import queue

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Will run bfs to remake the graph
        """
        graph={}
        for index,eq in enumerate(equations):
            if graph.get(eq[0]) is None:
                graph[eq[0]] = {eq[1]:values[index]}
                if graph.get(eq[1]) is None:
                    graph[eq[1]] = {eq[0]:1/values[index]}
                else:
                    graph[eq[1]][eq[0]]=1/values[index]
            else:
                graph[eq[0]][eq[1]] = values[index]
                if graph.get(eq[1]) is None:
                    graph[eq[1]] = {eq[0]:1/values[index]}
                else:
                    graph[eq[1]][eq[0]]=1/values[index]
        q = queue.Queue()
        keys= list(graph.keys())
        for key in keys:
            for denom in graph[key]:
                q.put([denom, graph[key][denom]])
            visited = {}
            while q.qsize()>0:
                curr = q.get()
                currVal = curr[1]
                visited[curr[0]] = True
                if curr[0] in graph:
                    for val in graph[curr[0]]:
                        if visited.get(val) is None:
                            q.put([val, graph[curr[0]][val]*currVal])
                        if graph[key].get(val) is None:
                            graph[key][val] = graph[curr[0]][val]*currVal

        res = []  
        print(graph)
        for query in queries:
            denom = query[1]
            numer = query[0]
            if numer == denom:
                if graph.get(denom) is None and graph.get(numer) is None:
                    res.append(-1.00000)
                else:
                    res.append(1.00000)
            elif graph.get(numer) is not None and graph.get(numer).get(denom) is not None:
                res.append(graph.get(numer).get(denom))
            elif graph.get(denom)is not None and graph.get(denom).get(numer) is not None:
                res.append(1/graph.get(denom).get(numer))
            else:
                res.append(-1.0000)
        return res