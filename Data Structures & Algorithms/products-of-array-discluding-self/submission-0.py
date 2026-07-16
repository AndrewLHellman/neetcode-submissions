class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j, num in enumerate(nums):
                if j != i:
                    product *= num
            res.append(product)
        return res