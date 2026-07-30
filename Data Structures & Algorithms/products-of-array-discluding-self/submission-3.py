class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref_prod = 1
        for i in range(len(nums)):
            res.append(pref_prod)
            pref_prod *= nums[i]
        
        suff_prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suff_prod
            suff_prod *= nums[i]
        
        return res