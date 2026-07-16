class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_members = set(nums)
        if (len(nums_members) < len(nums)):
            return True
        return False