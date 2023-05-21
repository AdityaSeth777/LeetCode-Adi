from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = self.buildGraph(equations, values)
        results = []
        
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                results.append(-1.0)
            else:
                result = self.bfs(dividend, divisor, graph)
                results.append(result)
        
        return results
    
    def buildGraph(self, equations, values):
        graph = defaultdict(dict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value
        
        return graph
    
    def bfs(self, start, end, graph):
        queue = deque([(start, 1.0)])
        visited = set()
        
        while queue:
            node, value = queue.popleft()
            
            if node == end:
                return value
            
            visited.add(node)
            
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, value * weight))
        
        return -1.0