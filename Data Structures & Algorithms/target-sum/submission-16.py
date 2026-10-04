class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        last_row = defaultdict(int)
        last_row[total] = 1
        cur_row = defaultdict(int)
        for row in range(1, len(nums)+1):
            for col in range(2*total+1):
                add_total = last_row[col+nums[row-1]]
                sub_total = last_row[col-nums[row-1]]
                cur_row[col] = add_total + sub_total
            last_row = cur_row
            cur_row = defaultdict(int)
        print(last_row)
        return last_row[total+target]
