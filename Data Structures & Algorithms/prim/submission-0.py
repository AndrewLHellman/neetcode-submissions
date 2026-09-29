class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}

        for i in range(n):
            adjList[i] = []

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        print(adjList)
        minHeap = []
        visit = set()
        weight = 0
        for v, w in adjList[0]:
            minHeap.append((w, v))
        heapq.heapify(minHeap)
        visit.add(0)

        while minHeap:
            print(minHeap)
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            weight += w1
            visit.add(n1)
            n -= 1
            if n == 1:
                return weight

            for n2, w2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2, n2))

        return -1
