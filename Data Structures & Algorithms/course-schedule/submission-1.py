class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = { num: [] for num in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        def cycleExists(cur, path = None):
            if path == None:
                path = set()
            if cur in path:
                return True

            path.add(cur)
            for course in adj_list[cur]:
                if cycleExists(course, path):
                    return True
            path.remove(cur)
            
            return False

        for num in range(numCourses):
            if cycleExists(num):
                return False

        return True