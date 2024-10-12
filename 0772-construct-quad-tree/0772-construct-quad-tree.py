"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        val = grid[0][0]
        if N == 1:
            return Node(grid[0][0], True, None, None, None, None)

        i, same = 0, True
        while i < N and same:
            j = 0
            while j < N and same:
                if grid[i][j] != val:
                    same = False
                    break
                j += 1
            i += 1

        if same:
            return Node(val, True, None, None, None, None)
        else:
            mid = N // 2
            topLeft = self.construct([row[:mid] for row in grid[:mid]])
            topRight = self.construct([row[mid:] for row in grid[:mid]])
            bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
            bottomRight = self.construct([row[mid:] for row in grid[mid:]])
            return Node(val, False, topLeft, topRight, bottomLeft, bottomRight)