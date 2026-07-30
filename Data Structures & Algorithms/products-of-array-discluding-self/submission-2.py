class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix_prod = 1
        for num in nums:
            prefix.append(prefix_prod)
            prefix_prod *= num

        suffix = []
        suffix_prod = 1
        for num in nums[::-1]:
            suffix.append(suffix_prod)
            suffix_prod *= num
        suffix = suffix[::-1]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        return res