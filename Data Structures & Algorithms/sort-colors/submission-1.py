class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]
        for num in nums:
            counter[num] += 1

        index = 0
        for i in range(len(counter)):
            for _ in range(counter[i]):
                nums[index] = i
                index += 1
