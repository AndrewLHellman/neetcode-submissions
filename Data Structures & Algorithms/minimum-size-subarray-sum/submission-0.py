class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        L, total = 0, 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minLen = min(minLen, R - L + 1)
                total -= nums[L]
                L += 1
        
        return minLen if minLen != float("inf") else 0