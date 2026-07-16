class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, set())
        
    def dfs(self, grid, r, c, visit = set()) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            (r, c) in visit or
            grid[r][c] == 1):
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visit.add((r, c))

        count = 0
        count += self.dfs(grid, r-1, c, visit)
        count += self.dfs(grid, r+1, c, visit)
        count += self.dfs(grid, r, c-1, visit)
        count += self.dfs(grid, r, c+1, visit)

        visit.remove((r, c))
        return count