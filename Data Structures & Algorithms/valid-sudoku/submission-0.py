class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for row in range(9):
            seen = set()
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        # Columns
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        # Squares
        for i in range(9):
            seen = set()
            square_row = (i // 3) * 3
            square_col = (i % 3) * 3
            for j in range(9):
                space_row = j // 3
                space_col = j % 3
                num = board[square_row + space_row][square_col + space_col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        return True
