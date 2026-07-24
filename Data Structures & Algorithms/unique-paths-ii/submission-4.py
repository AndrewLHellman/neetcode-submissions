class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c, memo = {}):
            if (r, c) not in memo:
                if min(r, c) < 0 or r >= m or c >= n:
                    memo[(r, c)] = 0
                elif obstacleGrid[r][c] == 1:
                    memo[(r, c)] = 0
                elif r == m - 1 and c == n - 1:
                    memo[(r, c)] = 1
                else:
                    memo[(r, c)] = dfs(r + 1, c, memo) + dfs(r, c + 1, memo)
            return memo[(r, c)]

        return dfs(0, 0)