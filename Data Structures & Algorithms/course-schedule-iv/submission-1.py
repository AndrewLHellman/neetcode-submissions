class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for a, b in prerequisites:
            adjList[b].append(a)
        
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = set()
        visit = set()
        def find_preqs(n):
            if n in visit:
                return
            
            visit.add(n)
            for prereq in adjList[n]:
                prereqs[n].add(prereq)
                find_preqs(prereq)
                prereqs[n] = prereqs[n].union(prereqs[prereq])

        for i in range(numCourses):
            find_preqs(i)
            print("{")
            for i in prereqs:
                print(i, prereqs[i])
            print("}")
        
        res = []
        for u, v in queries:
            res.append(u in prereqs[v])
        
        return res
        
