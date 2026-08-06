class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0

        for num in nums:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        
        return maxSum
