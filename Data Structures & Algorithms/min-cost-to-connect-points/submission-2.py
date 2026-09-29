class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = i
    
    def find(self, n: int) -> int:
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = []
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[:i]):
                dist = abs(x1-x2) + abs(y1-y2)
                minHeap.append((dist, i, j))
        
        heapq.heapify(minHeap)
        unionFind = UnionFind(len(points))
        weight = 0
        while minHeap and n > 1:
            w, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            weight += w
            n -= 1
        return weight
