class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = [(x**2 + y**2, [x, y]) for x, y in points]
        heap = []
        for dist_point in dist_points:
            if len(heap) < k:
                heapq.heappush_max(heap, dist_point)
            elif heap[0] > dist_point:
                heapq.heapreplace_max(heap, dist_point)
        return [point for dist, point in heap]
            
