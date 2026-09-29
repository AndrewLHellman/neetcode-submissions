class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n: int) -> int:
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
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
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for u, v, w in edges:
            minHeap.append((w, u, v))
        heapq.heapify(minHeap)

        uf = UnionFind(n)
        weight = 0
        while minHeap and n > 1:
            w, n1, n2 = heapq.heappop(minHeap)
            if not uf.union(n1, n2):
                continue
            
            weight += w
            n -= 1
        return weight if n == 1 else -1
