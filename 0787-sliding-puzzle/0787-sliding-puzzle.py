class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def check(board):
            return (board[0][0] == 1) and (board[0][1] == 2) and (board[0][2] == 3) \
                and (board[1][0] == 4) and (board[1][1] == 5)

        visited = set()
        def is_visited(board):
            key = ""
            for k in board[0] + board[1]:
                key += f"{k}-"
            if key in visited: return True
            visited.add(key)
            return False

        def copy(board):
            return [[board[0][0], board[0][1], board[0][2]],
                    [board[1][0], board[1][1], board[1][2]]]

        # find 0
        queue = deque()
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    queue.append([board, i, j])

        step = 0
        while len(queue):
            for _ in range(len(queue)):
                cur_board, i, j = queue.popleft()
                # check
                if check(cur_board): return step
                # append
                if i == 0: # down
                    cur_board[0][j] = cur_board[1][j]
                    cur_board[1][j] = 0
                    if not is_visited(cur_board):
                        queue.append([copy(cur_board), 1, j])
                    cur_board[1][j] = cur_board[0][j]
                    cur_board[0][j] = 0
                else: # up
                    cur_board[1][j] = cur_board[0][j]
                    cur_board[0][j] = 0
                    if not is_visited(cur_board):
                        queue.append([copy(cur_board), 0, j])
                    cur_board[0][j] = cur_board[1][j]
                    cur_board[1][j] = 0

                if j < 2: # right
                    cur_board[i][j] = cur_board[i][j+1]
                    cur_board[i][j+1] = 0
                    if not is_visited(cur_board):
                        queue.append([copy(cur_board), i, j+1])
                    cur_board[i][j+1] = cur_board[i][j]
                    cur_board[i][j] = 0
                if j > 0: # left
                    cur_board[i][j] = cur_board[i][j-1]
                    cur_board[i][j-1] = 0
                    if not is_visited(cur_board):
                        queue.append([copy(cur_board), i, j-1])
                    cur_board[i][j-1] = cur_board[i][j]
                    cur_board[i][j] = 0

            step += 1
        return -1