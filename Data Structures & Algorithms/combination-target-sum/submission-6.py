class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        combs = []
    
        def worker(i, cur_comb, total):
            if total == target:
                combs.append(cur_comb.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur_comb.append(nums[j])
                worker(j, cur_comb, total + nums[j])
                cur_comb.pop()

        worker(0, [], 0)
        return combs