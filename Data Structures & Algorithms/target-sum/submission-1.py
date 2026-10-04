class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def worker(first_n: int, num: int, memo={}) -> int:
            if (first_n, num) in memo:
                return memo[(first_n, num)]
            if first_n <= 0 and num == 0:
                return 1
            elif first_n <= 0 and num != 0:
                return 0
            memo[(first_n, num)] = worker(first_n - 1, num+nums[first_n-1]) + worker(first_n-1, num-nums[first_n-1])
            return memo[(first_n, num)]
        return worker(len(nums), target)