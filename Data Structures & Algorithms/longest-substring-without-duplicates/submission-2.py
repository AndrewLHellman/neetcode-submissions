class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        chars = defaultdict(lambda: -1)
        L = 0

        for R in range(len(s)):
            if chars[s[R]] >= L:
                L = chars[s[R]] + 1
            chars[s[R]] = R
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen