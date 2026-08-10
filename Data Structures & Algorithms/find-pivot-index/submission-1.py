class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [0] * (n)
        postfix_sums = [0] * (n)
        
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i-1] + nums[i-1]
            postfix_sums[n-i-1] = postfix_sums[n-i] + nums[n-i]

        print(prefix_sums)
        print(postfix_sums)

        for i in range(0, n):
            if prefix_sums[i] == postfix_sums[i]:
                return i
        
        return -1