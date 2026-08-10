class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] += 1
        for num in nums:
            curSum += num
            res += prefix_sum_counts[curSum - k]
            prefix_sum_counts[curSum] += 1
        
        return res