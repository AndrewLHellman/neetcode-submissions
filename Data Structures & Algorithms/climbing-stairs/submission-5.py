class Solution:
    def climbStairs(self, n: int) -> int:
        tab = [1, 2]
        if n == 1:
            return tab[0]
        for _ in range(n-2):
            temp = tab[1]
            tab[1] = tab[0] + tab[1]
            tab[0] = temp
        return tab[1]