class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [["T"]*n for _ in range(m)]

        ans = (m*n) - len(guards) - len(walls)
        for r, c in walls:
            grid[r][c] = "W"
        
        for r, c in guards:
            grid[r][c] = "G"

        for r, c in guards:
            # left
            i = r - 1
            while (i >= 0):
                if grid[i][c] == "W" or grid[i][c] == "G":
                    break
                if grid[i][c] == "T":
                    ans -= 1
                grid[i][c] = "F"
                i -= 1
            # right
            i = r + 1
            while (i < m):
                if grid[i][c] == "W" or grid[i][c] == "G":
                    break
                if grid[i][c] == "T":
                    ans -= 1
                grid[i][c] = "F"
                i += 1
            # top
            j = c - 1
            while (j >= 0):
                if grid[r][j] == "W" or grid[r][j] == "G":
                    break
                if grid[r][j] == "T":
                    ans -= 1
                grid[r][j] = "F"
                j -= 1
            # bottom
            j = c + 1
            while (j < n):
                if grid[r][j] == "W" or grid[r][j] == "G":
                    break
                if grid[r][j] == "T":
                    ans -= 1
                grid[r][j] = "F"
                j += 1
    
        return ans