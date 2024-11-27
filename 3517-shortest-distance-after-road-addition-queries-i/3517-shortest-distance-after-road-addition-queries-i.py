class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)
        n -= 1

        def bfs():
            queue = deque([0])
            step = 0
            visited = set([0])
            while True:
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    if cur == n: return step
                    for nei in graph[cur]:
                        if nei in visited: continue
                        visited.add(nei)
                        queue.append(nei)
                step += 1

        ans = []
        for a, b in queries:
            graph[a].append(b)
            ans.append(bfs())
        return ans