class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for i, (a, b) in enumerate(edges):
            adj_list[a].append((b, succProb[i]))
            adj_list[b].append((a, succProb[i]))
        
        seen = set()
        max_heap = [(-1, start_node)]
        while max_heap:
            p1, n1 = heapq.heappop(max_heap)
            if n1 == end_node:
                return -p1
            if n1 in seen:
                continue
            seen.add(n1)

            for n2, p2 in adj_list[n1]:
                if n2 not in seen:
                    heapq.heappush(max_heap, (p1*p2, n2))

        return 0
