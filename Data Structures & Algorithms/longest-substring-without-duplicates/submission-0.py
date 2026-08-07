class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        chars = set()
        L = 0

        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            chars.add(s[R])
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen