class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur_set, subsets = [], []
        
        self.worker(0, nums, cur_set, subsets)

        return subsets
    
    def worker(self, i: int, nums: List[int], cur_set: List[int], subsets: List[List[int]]):
        if i >= len(nums):
            subsets.append(cur_set.copy())
            return
        
        cur_set.append(nums[i])
        self.worker(i+1, nums, cur_set, subsets)
        cur_set.pop()

        while i < len(nums) - 1 and nums[i] == nums[i+1]:
            i += 1
        self.worker(i+1, nums, cur_set, subsets)