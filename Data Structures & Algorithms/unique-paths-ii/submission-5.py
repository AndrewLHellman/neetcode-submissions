class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        prev_row = [0]*cols
        prev_row[cols-1] = 1
        

        for r in range(rows-1, -1, -1):
            cur_row = [0]*cols
            if obstacleGrid[r][cols - 1] == 0:
                cur_row[cols-1] = prev_row[cols-1]

            for c in range(cols-2, -1, -1):
                if obstacleGrid[r][c] == 0:
                    cur_row[c] = prev_row[c] + cur_row[c+1]
            
            prev_row = cur_row
        
        return prev_row[0]
