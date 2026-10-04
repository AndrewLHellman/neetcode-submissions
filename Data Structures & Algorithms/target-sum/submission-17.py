class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        last_row = defaultdict(int)
        last_row[0] = 1
        for num in nums:
            cur_row = defaultdict(int)
            for total, count in last_row.items():
                cur_row[total + num] += count
                cur_row[total - num] += count
            last_row = cur_row
        return last_row[target]
