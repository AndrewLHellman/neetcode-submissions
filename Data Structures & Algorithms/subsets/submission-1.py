class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            subsets = self.subsets(nums[:-1])
            results = subsets.copy()
            for subset in subsets:
                results.append(subset + [nums[-1]])
            return results
