class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if 2**(int(num)-1) & rows[row] or 2**(int(num)-1) & cols[col] or 2**(int(num)-1) & squares[(row // 3)*3+(col // 3)]:
                    return False
                rows[row] |= 2**(int(num)-1)
                cols[col] |= 2**(int(num)-1)
                squares[(row // 3)*3+(col // 3)] |= 2**(int(num)-1)

        return True
