class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            big_stone = heapq.heappop(stones)
            little_stone = heapq.heappop(stones)
            new_stone = big_stone - little_stone
            if new_stone:
                heapq.heappush(stones, new_stone)
        return 0 if len(stones) == 0 else -heapq.heappop(stones)