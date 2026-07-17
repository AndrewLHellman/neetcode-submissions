class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        for r, row in enumerate(grid):
            for c, fruit in enumerate(row):
                if fruit == 1:
                    fresh_count += 1
                if fruit == 2:
                    queue.append((r, c))
        
        time = 0
        while fresh_count != 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != 1):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh_count -= 1
            
            time += 1
        
        return time if fresh_count == 0 else -1
