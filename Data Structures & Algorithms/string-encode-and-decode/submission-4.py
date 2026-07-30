class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(string)}#{string}' for string in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[i] != '#':
                i += 1
            else:
                length = int(s[j:i])
                j = i + 1 + length
                res.append(s[i+1:j])
                i = j
        return res
