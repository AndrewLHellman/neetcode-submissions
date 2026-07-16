class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                count1 += 1
                maxCount = max(maxCount, count1)
            else:
                count1 = 0
        return maxCount