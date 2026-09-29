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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        minHeap = []
        for i, (u, v, w) in enumerate(edges):
            minHeap.append((w, i, u, v))
        heapq.heapify(minHeap)

        unionFind = UnionFind(n)
        min_weight = 0
        m = n-1
        curHeap = minHeap.copy()
        while curHeap and m > 0:
            w, i, n1, n2 = heapq.heappop(curHeap)
            if not unionFind.union(n1, n2):
                continue
            min_weight += w
            m -= 1
        
        required_edges = set()
        mst_edges = set()

        for i in range(len(edges)):
            # include edge i
            unionFind = UnionFind(n)
            weight = 0
            m = n-1
            curHeap = minHeap.copy()
            u, v, w = edges[i]
            weight += w
            unionFind.union(u, v)
            m -= 1
            while curHeap and m > 0:
                w, j, n1, n2 = heapq.heappop(curHeap)
                if not unionFind.union(n1, n2):
                    continue
                weight += w
                m -= 1
            if weight == min_weight:
                mst_edges.add(i)
                unionFind = UnionFind(n)
                weight = 0
                m = n-1
                curHeap = minHeap.copy()
                while curHeap and m > 0:
                    w, j, n1, n2 = heapq.heappop(curHeap)
                    if i == j or not unionFind.union(n1, n2):
                        continue
                    weight += w
                    m -= 1
                if m > 0 or weight > min_weight:
                    required_edges.add(i)
        
        return [list(required_edges), list(mst_edges.difference(required_edges))]
