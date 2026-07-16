class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix_product = 1
        for num in nums:
            prefix.append(prefix_product)
            prefix_product *= num

        suffix = []
        suffix_product = 1
        for num in nums[::-1]:
            suffix.append(suffix_product)
            suffix_product *= num
        suffix = suffix[::-1]

        res = []
        for pre, suf in zip(prefix, suffix):
            res.append(pre * suf)

        return res
