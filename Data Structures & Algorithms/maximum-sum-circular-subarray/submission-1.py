class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax, 0) + num
            curMin = min(curMin, 0) + num
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax