class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for a, b in prerequisites:
            adjList[b].append(a)
        
        visit = set()
        path = set()
        courseOrder = []
        def dfs(n):
            if n in path:
                return False
            if n in visit:
                return True
            
            visit.add(n)
            path.add(n)
            for m in adjList[n]:
                if not dfs(m):
                    return False
            path.remove(n)
            courseOrder.append(n)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        courseOrder.reverse()
        return courseOrder
        