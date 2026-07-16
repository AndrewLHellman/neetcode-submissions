class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        starts = []
        max_count = 0
        for num in nums:
            if num - 1 not in seen:
                starts.append(num)
        for start in starts:
            count = 1
            cur = start
            while cur + 1 in seen:
                count += 1
                cur += 1
            max_count = max(count, max_count)
        return max_count