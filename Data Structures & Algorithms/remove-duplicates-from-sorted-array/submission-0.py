class Solution:
    def removeFromMiddle(self, nums, i):
        for j in range(i+1, len(nums)):
            nums[j-1] = nums[j]

    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        i = 1
        while i < k:
            if nums[i-1] == nums[i]:
                self.removeFromMiddle(nums, i)
                k -= 1
            else:
                i += 1
        return k