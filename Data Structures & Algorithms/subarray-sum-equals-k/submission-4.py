class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        res = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] += 1
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
            prefix_sum_counts[prefix_sums[-1]] += 1

        for num in prefix_sums:
            prefix_sum_counts[num] -= 1
            res += prefix_sum_counts[k + num]
        
        return res