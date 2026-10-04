class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if not (total % 2 == 0):
            return False
        last_row = [False] * (total//2)
        cur_row = [False] * (total//2)
        for row in range(1, len(nums)+1):
            for col in range(total//2):
                remaining = (col+1) - nums[row-1]
                if remaining == 0:
                    cur_row[col] = True
                elif remaining < 0:
                    cur_row[col] = last_row[col]
                else:
                    cur_row[col] = (last_row[col] or last_row[remaining-1])
            last_row = cur_row
            cur_row = [False] * (total//2)
        return last_row[-1]
