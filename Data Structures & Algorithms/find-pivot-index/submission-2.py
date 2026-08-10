class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [0] * (n)
        total = sum(nums)
        
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i-1] + nums[i-1]

        print(prefix_sums)

        for i in range(0, n):
            print(total)
            total -= nums[i]
            if total == prefix_sums[i]:
                return i
        
        return -1