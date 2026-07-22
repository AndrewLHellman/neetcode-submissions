class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            temp = one
            one = max(num + two, one)
            two = temp
        return one
