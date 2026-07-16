class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1

        freq = [set() for _ in range(len(nums))]
        for num in map:
            freq[map[num]-1].add(num)

        res = []
        for freq_set in freq[::-1]:
            for num in freq_set:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
