class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # bfs
        N2 = (len(board)*len(board)) - 1
        step = 0
        visited = set()
        dropped = set()
        queue = [0]
        while len(queue):
            nes = []
            for cur in queue:
                if cur == N2: return step
                for ne in range(cur+1, min(cur+6, N2)+1):
                    if ne in visited: continue
                    # define row, col
                    row = ne//len(board)
                    col = ne%len(board)
                    if row & 1: # odd then right to left
                        col = len(board) - col - 1
                    val = board[-(row+1)][col]
                    if val == -1:
                        if ne not in visited:
                            nes.append(ne)
                    else:
                        if val-1 not in dropped:
                            nes.append(val-1)
                            dropped.add(val-1)
                    visited.add(ne)
            queue = nes
            step += 1
        return -1

