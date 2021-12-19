class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'X' and (not i or board[i-1][j] != 'X') and (not j or board[i][j-1] != 'X'):
                    ans += 1
        return ans
