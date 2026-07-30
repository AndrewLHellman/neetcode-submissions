class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for n in range(0, n+1):
            count = 0
            while n > 0:
                n &= (n-1)
                count += 1
            output.append(count)
        
        return output