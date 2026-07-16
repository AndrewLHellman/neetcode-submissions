class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_len = 0
        cur_len = 0
        prev = float("-inf")
        for num in nums:
            if num - 1 == prev:
                cur_len += 1
            elif num != prev:
                cur_len = 1
            max_len = max(max_len, cur_len)
            prev = num

        return max_len