class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur_set, subsets = [], []
        self.worker(0, nums, cur_set, subsets)
        return subsets
        
    def worker(self, i, nums: List[int], cur_set: List[int], subsets: List[List[int]]):
        if i >= len(nums):
            subsets.append(cur_set.copy())
            return
        
        cur_set.append(nums[i])
        self.worker(i+1, nums, cur_set, subsets)
        cur_set.pop()

        self.worker(i+1, nums, cur_set, subsets)