class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        pars = list(range(1, n + 1))
        rank = [1] * n

        def find(x: int) -> int:
            p = pars[x-1]
            while p != pars[p-1]:
                pars[p-1] = pars[pars[p-1] - 1]
                p = pars[p-1]
            return p
        
        def union(x: int, y: int) -> bool:
            print(x, y)
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False

            if rank[p1-1] > rank[p2-1]:
                pars[p2-1] = p1
            elif rank[p1-1] < rank[p2-1]:
                pars[p1-1] = p2
            else:
                pars[p2-1] = p1
                rank[p1-1] += 1
            return True
        
        res = [-1, -1]
        for edge in edges:
            if not union(edge[0], edge[1]):
                res = edge

        return res