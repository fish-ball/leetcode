class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        c = Counter(''.join(board))
        xwin = 'XXX' in board or ('X', 'X', 'X') in zip(*board) \
            or board[0][0] == board[1][1] == board[2][2] == 'X' \
            or board[0][2] == board[1][1] == board[2][0] == 'X'
        owin = 'OOO' in board or ('O', 'O', 'O') in zip(*board) \
            or board[0][0] == board[1][1] == board[2][2] == 'O' \
            or board[0][2] == board[1][1] == board[2][0] == 'O'
        if c.get('X', 0) == c.get('O', 0) + 1:
            return not owin
        elif c.get('X', 0) == c.get('O', 0):
            return not xwin
        return False
