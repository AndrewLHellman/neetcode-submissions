class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {}
        for i, (x1, y1) in enumerate(points):
            adjList[i] = []
            for j, (x2, y2) in enumerate(points[:i]):
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((j, dist))
                adjList[j].append((i, dist))

        minHeap = []
        weight = 0
        visit = set()
        for n, dist in adjList[0]:
            minHeap.append((dist, n))
        visit.add(0)
        heapq.heapify(minHeap)
        while minHeap and len(visit) < len(points):
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            weight += w1
            visit.add(n1)

            for n2, w2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2, n2))
        return weight
