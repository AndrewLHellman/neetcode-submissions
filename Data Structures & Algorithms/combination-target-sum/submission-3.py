class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.worker(0, [], 0, combs, nums, target)

        return combs
    
    def worker(self, i, cur_comb, cur_sum, combs, nums, target):
        if cur_sum == target:
            combs.append(cur_comb.copy())
            return
        elif cur_sum > target or i >= len(nums):
            return
        
        cur_comb.append(nums[i])
        cur_sum += nums[i]
        self.worker(i, cur_comb, cur_sum, combs, nums, target)
        cur_comb.pop()
        cur_sum -= nums[i]
        self.worker(i+1, cur_comb, cur_sum, combs, nums, target)