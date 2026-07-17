class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or 
                        grid[nr][nc] == 1):
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            
            length += 1

        return -1