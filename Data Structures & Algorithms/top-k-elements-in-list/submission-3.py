class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = 0
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            max_freq = max(counts[num], max_freq)
        array = [[] for _ in range(max_freq)]
        for num, count in counts.items():
            array[count-1].append(num)
        
        res = []
        for bucket in array[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) >= k:
                    return res
        return res
            