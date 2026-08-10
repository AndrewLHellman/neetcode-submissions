class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                self.prefix_matrix[row][col] = (
                    matrix[row - 1][col - 1]
                    + self.prefix_matrix[row - 1][col]
                    + self.prefix_matrix[row][col - 1]
                    - self.prefix_matrix[row - 1][col - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_matrix[row2 + 1][col2 + 1]
            - self.prefix_matrix[row2 + 1][col1]
            - self.prefix_matrix[row1][col2 + 1]
            + self.prefix_matrix[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
