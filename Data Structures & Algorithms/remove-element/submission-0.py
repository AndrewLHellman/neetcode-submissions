class Solution:
    def removeMiddle(self, arr, i, length):
        # Shift starting from i + 1 to end.
        for index in range(i + 1, length):
            arr[index - 1] = arr[index]

    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            while nums[i] == val and i < len(nums) - count:
                count += 1
                self.removeMiddle(nums, i, len(nums))
        return len(nums) - count