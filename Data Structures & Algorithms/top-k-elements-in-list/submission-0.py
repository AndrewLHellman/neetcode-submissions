class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        return list(map(lambda x: x[0], sorted(counts.items(), key=(lambda x: -x[1]))[:k]))