class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        j = 0
        capital_min_heap = [(cap, profit) for cap, profit in zip(capital, profits)]
        heapq.heapify(capital_min_heap)
        profit_max_heap = []
        while j < k and j < n and (capital_min_heap or profit_max_heap):
            while capital_min_heap and capital_min_heap[0][0] <= w:
                cap, profit = heapq.heappop(capital_min_heap)
                heapq.heappush(profit_max_heap, -profit)
            if not profit_max_heap:
                break
            w -= heapq.heappop(profit_max_heap)
            j += 1
        return w