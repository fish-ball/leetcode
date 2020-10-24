class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1 = board
        set2 = zip(*board)
        set3 = [board[i//3*3][i%3*3:i%3*3+3] +
                board[i//3*3+1][i%3*3:i%3*3+3] +
                board[i//3*3+2][i%3*3:i%3*3+3] for i in range(9)]
        for s in (set1, set2, set3):
            # print('>>>')
            for l in s:
                ll = [x for x in l if x != '.']
                # print(ll, len(ll), len(set(ll)))
                if len(ll) != len(set(ll)):
                    return False
        return True
