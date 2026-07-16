class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        count = m * n
        l, r = 0, count-1

        while l <= r:
            p = (l + r) // 2
            p_row = p // n
            p_col = p - p_row*n
            if matrix[p_row][p_col] < target:
                l = p + 1
            elif matrix[p_row][p_col] > target:
                r = p - 1
            else:
                return True

        return False