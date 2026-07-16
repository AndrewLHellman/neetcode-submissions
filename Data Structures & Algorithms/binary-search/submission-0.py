class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l < r):
            index = (l + r) // 2
            num = nums[index]
            if (num == target):
                return index
            if (num > target):
                r = index - 1
            if (num < target):
                l = index + 1
        if nums[l] == target:
            return l
        return -1