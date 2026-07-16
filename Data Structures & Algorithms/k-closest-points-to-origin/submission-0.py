class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify_max(dist_points)
        while len(dist_points) > k:
            heapq.heappop_max(dist_points)
        return [point for dist, point in dist_points]