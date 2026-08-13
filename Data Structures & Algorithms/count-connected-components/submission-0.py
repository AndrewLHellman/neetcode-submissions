class UnionFind:
    def __init__(self, n: int):
        self.pars = list(range(n))
        self.rank = [1] * n
        self.components = n
    
    def find(self, x: int) -> int:
        p = self.pars[x]
        while p != self.pars[p]:
            self.pars[p] = self.pars[self.pars[p]]
            p = self.pars[p]
        return p
    
    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.pars[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.pars[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.components -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x1, x2 in edges:
            uf.union(x1, x2)
        return uf.components