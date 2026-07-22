class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {len(nums): 0, len(nums) - 1 : max(nums[-1], 0)}

        def recurse(nums, index = 0):
            if index in memo:
                return memo[index]
            else:
                memo[index] = max(nums[index] + recurse(nums, index + 2), recurse(nums, index + 1))
            return memo[index]

        return recurse(nums)