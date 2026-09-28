class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = set()
        minheap = [(0, k)]
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            
            n -= 1
            if n == 0:
                return w1
            visited.add(n1)
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (w1 + w2, n2))
            
        return -1