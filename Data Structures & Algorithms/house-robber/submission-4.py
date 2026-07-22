class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recurse(nums, index = 0):
            if index in memo:
                return memo[index]
            if len(nums) - index <= 0:
                memo[index] = 0
            elif len(nums) - index == 1:
                memo[index] = nums[-1]
            else:
                memo[index] = max(nums[index] + recurse(nums, index + 2), recurse(nums, index + 1))
            return memo[index]

        return recurse(nums)