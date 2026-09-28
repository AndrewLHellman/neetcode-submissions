class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # adj = {}
        # for row in range(n):
        #     for col in range(n):
        #         adj[(row, col)] = []
        
        seen = set()
        minheap = [(grid[0][0], (0, 0))]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 == (n-1, n-1):
                return w1
            if n1 in seen:
                continue
            seen.add(n1)

            neighbors = []
            if n1[0] > 0 and (n1[0] - 1, n1[1]) not in seen:
                neighbors.append((n1[0] - 1, n1[1]))
            if n1[1] > 0 and (n1[0], n1[1] - 1) not in seen:
                neighbors.append((n1[0], n1[1] - 1))
            if n1[0] < n - 1 and (n1[0] + 1, n1[1]) not in seen:
                neighbors.append((n1[0] + 1, n1[1]))
            if n1[1] < n - 1 and (n1[0], n1[1] + 1) not in seen:
                neighbors.append((n1[0], n1[1] + 1))
            
            for n2 in neighbors:
                heapq.heappush(minheap, (max(w1, grid[n2[0]][n2[1]]), n2))
            
        return -1
