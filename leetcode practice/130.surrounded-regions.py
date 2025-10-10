#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
             for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c]="O"
                    

        
# @lc code=end

