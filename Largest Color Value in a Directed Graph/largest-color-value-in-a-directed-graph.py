class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = collections.defaultdict(list)
        indegree = [0] * len(colors)
        for u, v in edges:
            graph[v].append(u)
            indegree[u] += 1
        count = [collections.defaultdict(int) for _ in range(n)]
        q = collections.deque(filter(lambda i: not indegree[i], range(n)))
        seen = 0
        ans = 0
        while q:
            curr = q.popleft()
            count[curr][colors[curr]] += 1
            ans = max(ans, count[curr][colors[curr]])
            seen += 1
            for v in graph[curr]:
                for c in count[curr]:
                    count[v][c] = max(count[v][c], count[curr][c])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if seen < n:
            return -1
        return ans