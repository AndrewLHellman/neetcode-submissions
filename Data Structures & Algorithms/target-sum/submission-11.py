class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target >= total+1:
            return 0
        last_row = [0] * total + [1] + [0]*total
        cur_row = [0] * (2*total + 1)
        for row in range(1, len(nums)+1):
            for col in range(2*total+1):
                add_total = last_row[col+nums[row-1]] if abs(col+nums[row-1]) < (2*total + 1) else 0
                sub_total = last_row[col-nums[row-1]] if abs(col-nums[row-1]) >= 0 else 0
                cur_row[col] = add_total + sub_total
            last_row = cur_row
            cur_row = [0] * (2*total + 1)
        return last_row[total+target]
