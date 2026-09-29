class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for i, (a, b) in enumerate(edges):
            adj_list[a].append((b, i))
            adj_list[b].append((a, i))
        
        seen = set()
        max_heap = [(-1, start_node)]
        while max_heap:
            p, n1 = heapq.heappop(max_heap)
            if n1 == end_node:
                return -p
            if n1 in seen:
                continue
            seen.add(n1)

            for n2, i in adj_list[n1]:
                if n2 not in seen:
                    heapq.heappush(max_heap, (p*succProb[i], n2))

        return 0
