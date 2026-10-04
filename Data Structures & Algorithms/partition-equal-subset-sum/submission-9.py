class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if not (total % 2 == 0):
            return False
        tab = [[False] * (total//2) for _ in range(len(nums)+1)]
        for row in range(1, len(tab)):
            for col in range(total//2):
                remaining = (col+1) - nums[row-1]
                if remaining == 0:
                    tab[row][col] = True
                elif remaining < 0:
                    tab[row][col] = tab[row-1][col]
                else:
                    tab[row][col] = (tab[row-1][col] or tab[row-1][remaining-1])
        return tab[-1][-1]
