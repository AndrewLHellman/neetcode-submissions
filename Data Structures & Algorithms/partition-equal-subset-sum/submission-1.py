class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        def worker(last, remaining, memo = {}):
            if (last, remaining) in memo:
                return memo[(last, remaining)]
            if remaining == 0:
                return True
            elif remaining < 0:
                return False
            elif last < 0:
                return False
            memo[(last, remaining)] = worker(last-1, remaining) or worker(last-1, remaining - nums[last])
            return memo[(last, remaining)]
        
        return worker(len(nums)-1, total/2)
