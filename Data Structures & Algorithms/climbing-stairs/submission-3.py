class Solution:
    def climbStairs(self, n: int, cache = { 1: 1, 2: 2}) -> int:
        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return cache[n]