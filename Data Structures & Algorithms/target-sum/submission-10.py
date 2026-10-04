class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target >= total+1:
            return 0
        tab = [[0] * total + [1] + [0]*total] + [[0] * (2*total + 1) for _ in range(len(nums))]
        for row in range(1, len(tab)):
            for col in range(2*total+1):
                add_total = tab[row-1][col+nums[row-1]] if abs(col+nums[row-1]) < (2*total + 1) else 0
                sub_total = tab[row-1][col-nums[row-1]] if abs(col-nums[row-1]) >= 0 else 0
                tab[row][col] = add_total + sub_total
        return tab[-1][total+target]
