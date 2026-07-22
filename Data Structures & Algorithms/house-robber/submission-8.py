class Solution:
    def rob(self, nums: List[int]) -> int:
        tab = [0, 0]
        for num in nums:
            tab.append(max(num + tab[-2], tab[-1]))
        return tab[-1]
