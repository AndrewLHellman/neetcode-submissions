class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        total = 0
        maxCurr, minCurr = 0, 0

        for num in nums:
            maxCurr = max(maxCurr, 0) + num
            minCurr = min(minCurr, 0) + num
            total += num
            maxSum = max(maxSum, maxCurr)
            minSum = min(minSum, minCurr)
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum