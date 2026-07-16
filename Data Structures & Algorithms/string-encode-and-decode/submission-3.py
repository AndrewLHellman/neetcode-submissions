class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(f'{len(string)}#{string}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s):
            if s[i] != '#':
                i += 1
            else:
                size = int(s[j:i])
                i += 1
                res.append(s[i:i+size])
                i += size
                j = i 
        return res

