class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_1 in enumerate(nums):
            for j, num_2 in enumerate(nums[i+1:]):
                if num_1+num_2 == target:
                    return [i, j+i+1]