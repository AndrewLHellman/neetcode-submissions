class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        tab = [[[0] * (m+1) for _ in range(n + 1)] for _ in range(len(strs)+1)]

        for i in range(1, len(strs) + 1):
            chars = Counter(strs[i-1])
            cur_0s, cur_1s = chars["0"], chars["1"]
            for zeros in range(m+1):
                for ones in range(n+1):
                    if cur_0s > zeros or cur_1s > ones:
                        tab[i][ones][zeros] = tab[i-1][ones][zeros]
                    else:
                        tab[i][ones][zeros] = max(tab[i-1][ones][zeros], tab[i-1][ones-cur_1s][zeros-cur_0s] + 1)

        return tab[-1][-1][-1]

        def backtrack(i: int, zeros: int, ones: int, memo = {}):
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]
            if zeros == 0 and ones == 0:
                return 0
            elif zeros < 0 or ones < 0:
                return -1
            elif i < 0:
                return 0
            chars = Counter(strs[i])
            cur_0s, cur_1s = chars["0"], chars["1"]
            exclude_count = backtrack(i-1, zeros, ones)
            include_count = backtrack(i-1, zeros-cur_0s, ones-cur_1s)
            memo[(i, zeros, ones)] = max(exclude_count, include_count + 1)
            return memo[(i, zeros, ones)]
        
        return backtrack(len(strs)-1, m, n)