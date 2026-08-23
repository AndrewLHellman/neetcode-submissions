class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        if len(nums) == 0 or target < 2:
            return []
        
        result = self.combinationSum(nums[1:], target)

        for combination in self.combinationSum(nums, target - nums[0]):
            result.append(combination + [nums[0]])
        
        return result