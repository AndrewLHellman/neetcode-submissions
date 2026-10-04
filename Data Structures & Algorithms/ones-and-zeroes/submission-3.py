class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
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