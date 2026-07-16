class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r: int, c: int) -> int:
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0
            
            area = 1
            visited.add((r, c))
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area

        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))

        return max_area
