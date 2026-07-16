class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        sizes = []
        for string in strs:
            sizes.append(str(len(string)))
        return ','.join(sizes) + "#" + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        i = 0
        while s[i] != '#':
            i += 1
        sizes = [int(x) for x in s[:i].split(',')]
        res = []
        i += 1
        for size in sizes:
            res.append(s[i:i+size])
            i += size
        return res
