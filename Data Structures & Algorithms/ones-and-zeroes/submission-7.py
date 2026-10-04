class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        prev_tab = [[0] * (m+1) for _ in range(n + 1)]

        for i in range(1, len(strs) + 1):
            cur_tab = [[0] * (m+1) for _ in range(n + 1)]
            chars = Counter(strs[i-1])
            cur_0s, cur_1s = chars["0"], chars["1"]
            for zeros in range(m+1):
                for ones in range(n+1):
                    if cur_0s > zeros or cur_1s > ones:
                        cur_tab[ones][zeros] = prev_tab[ones][zeros]
                    else:
                        cur_tab[ones][zeros] = max(prev_tab[ones][zeros], prev_tab[ones-cur_1s][zeros-cur_0s] + 1)
            prev_tab = cur_tab

        return prev_tab[-1][-1]
