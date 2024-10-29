class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # create graph of valid move
        graph = {}
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n-1):
                ne = []
                for x in range(max(0, i-1), min(m, i+2)):
                    if grid[x][j+1] > grid[i][j]:
                        ne.append((x,j+1))
                graph[(i,j)] = ne

        # iterate over all starting point and do caching
        cache = {}
        def search(i, j):
            if j == (len(grid[0])-1): return 0
            key = (i,j)
            if key in cache: return cache[key]
            ans = 0
            for ii, jj in graph[key]:
                ans = max(ans, 1 + search(ii, jj))
            cache[key] = ans
            return ans

        ans = 0
        for i in range(m):
            ans = max(ans, search(i, 0))
        return ans
