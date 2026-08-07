class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        L = 0
        mp = defaultdict(int)
        most_freq_char = s[0]
        mp[most_freq_char] = 0
        for R in range(len(s)):
            mp[s[R]] += 1
            for key in mp.keys():
                if mp[key] > mp[most_freq_char]:
                    most_freq_char = key

            if R - L + 1 > mp[most_freq_char] + k:
                mp[s[L]] -= 1
                for key in mp:
                    if mp[key] > mp[most_freq_char]:
                        most_freq_char = key
                L += 1

            maxLen = max(maxLen, R - L + 1)

        return maxLen

