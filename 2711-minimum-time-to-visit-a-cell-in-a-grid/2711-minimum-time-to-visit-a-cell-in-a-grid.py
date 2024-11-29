class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1

        rows, cols = len(grid)-1, len(grid[0])-1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        pq = [(grid[0][0], 0, 0)] # time, row, col

        def _is_valid(row, col, rows, cols):
            return 0 <= row <= rows and 0 <= col <= cols and (row, col) not in visited

        while pq:
            time, row, col = heapq.heappop(pq)

            if (row, col) == (rows, cols): return time

            if (row, col) in visited: continue
            visited.add((row, col))

            for dx, dy in directions:
                row1, col1 = row+dx, col+dy
                if not _is_valid(row1, col1, rows, cols): continue

                wait_time = (
                    0 if ((grid[row1][col1] - time) % 2) & 1 else 1
                )
                time1 = max(grid[row1][col1] + wait_time, time + 1)
                heapq.heappush(pq, (time1, row1, col1))
        return -1
        