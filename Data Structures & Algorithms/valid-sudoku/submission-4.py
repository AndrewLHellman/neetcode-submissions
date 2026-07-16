class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cols = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                val = int(num) - 1
                bit = (1 << val)
                if bit & rows[row] or bit & cols[col] or bit & squares[(row // 3)*3+(col // 3)]:
                    return False
                rows[row] |= bit
                cols[col] |= bit
                squares[(row // 3)*3+(col // 3)] |= bit

        return True
