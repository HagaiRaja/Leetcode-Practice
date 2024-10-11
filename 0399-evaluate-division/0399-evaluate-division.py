class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(values)):
            if equations[i][0] not in graph: graph[equations[i][0]] = {}
            graph[equations[i][0]][equations[i][1]] = values[i]
            if equations[i][1] not in graph: graph[equations[i][1]] = {}
            graph[equations[i][1]][equations[i][0]] = 1/values[i]
        
        ans = []
        for src, dst in queries:
            if src == dst:
                if src in graph: ans.append(1.0)
                else: ans.append(-1.0)
                continue
            cur_ans = -1
            visited = set([src])
            queue = [(src, 1)]
            while queue:
                pos, val = queue.pop()
                if pos == dst:
                    cur_ans = val
                    break
                if pos not in graph: continue
                if pos != src and pos not in graph[src]:
                    graph[src][pos] = val # caching
                for nei in graph[pos]:
                    if nei in visited: continue
                    visited.add(nei)
                    queue.append((nei, val*graph[pos][nei]))
            ans.append(cur_ans)
        return ans
