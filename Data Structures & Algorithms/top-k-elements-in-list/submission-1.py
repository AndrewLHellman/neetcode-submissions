class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        return [x[0] for x in sorted(map.items(), key = lambda x : x[1], reverse=True)[:k]]

