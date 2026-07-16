class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for num in nums:
            if num in map:
                return True
            else:
                map.add(num)
        return False