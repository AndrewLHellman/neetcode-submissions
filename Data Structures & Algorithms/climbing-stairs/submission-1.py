class Solution:
    memo = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n not in Solution.memo:
            Solution.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return Solution.memo[n]