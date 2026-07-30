class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numSet:
                count = 1
                while num + 1 in numSet:
                    num += 1
                    count += 1
                res = max(res, count)
        return res 