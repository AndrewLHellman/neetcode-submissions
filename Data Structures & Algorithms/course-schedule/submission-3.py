class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for a, b in prerequisites:
            adjList[a].append(b)
        
        path = set()
        visit = set()

        def dfs(n):
            if n in path:
                return False
            if n in visit:
                return True
            
            path.add(n)
            visit.add(n)
            for m in adjList[n]:
                if not dfs(m):
                    return False
            path.remove(n)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
