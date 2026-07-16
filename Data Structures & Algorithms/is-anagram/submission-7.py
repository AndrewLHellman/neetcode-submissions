class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        for char in t:
            chars[char] = chars.get(char, 0) - 1
        for val in chars.values():
            if val != 0:
                return False
        return True
