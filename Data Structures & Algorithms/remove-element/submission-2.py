class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = len(nums)
        while k < i:
            if nums[k] != val:
                k += 1
            else:
                i -= 1
                nums[k] = nums[i]
        return k