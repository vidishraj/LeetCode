from collections import defaultdict, deque
from typing import List, Dict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def build_graph(equations: List[List[str]], values: List[float]) -> Dict[str, Dict[str, float]]:
            graph = defaultdict(dict)
            for (num, denom), value in zip(equations, values):
                graph[num][denom] = value
                graph[denom][num] = 1 / value
            return graph
        
        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            q = deque([(start, 1.0)])
            visited = set()
            while q:
                current, current_value = q.popleft()
                if current == end:
                    return current_value
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        q.append((neighbor, current_value * value))
            return -1.0
        
        graph = build_graph(equations, values)
        return [bfs(num, denom) for num, denom in queries]