class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for u, v in edges:
            adjList[u].append(v)
        
        visit = set()
        path = set()
        topSort = []
        def dfs(n1):
            if n1 in path:
                return False
            if n1 in visit:
                return True
            
            visit.add(n1)
            path.add(n1)
            for n2 in adjList[n1]:
                if not dfs(n2):
                    return False
            path.remove(n1)
            topSort.append(n1)
            return True
            
        for i in range(n):
            if not dfs(i):
                return []
        
        topSort.reverse()
        return topSort