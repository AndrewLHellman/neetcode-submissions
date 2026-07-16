class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * 2 * n
        for i, val in enumerate(nums):
            ans[i] = val
            ans[n + i] = val
        return ans