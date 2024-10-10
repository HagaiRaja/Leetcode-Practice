class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changes = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                # check
                live_nei = 0
                for x in range(max(i-1, 0), min(len(board), i+2)):
                    for y in range(max(j-1, 0), min(len(board[0]), j+2)):
                        live_nei += board[x][y]
                        print(x, y, "|", board[x][y], live_nei)
                live_nei -= board[i][j]
                print("====", i, j, live_nei)
                if board[i][j]:
                    if live_nei < 2 or live_nei > 3: changes.append((i, j, 0))
                else:
                    if live_nei == 3: changes.append((i, j, 1))
        
        for i, j, val in changes:
            board[i][j] = val