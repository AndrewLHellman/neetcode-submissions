class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            if n & 2**(i) != 0:
                res |= 2**(32-i-1)
        return res