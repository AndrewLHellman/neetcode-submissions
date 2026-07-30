class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            if n & (1 << i):
                res |= (2**(31) >> i)
        return res