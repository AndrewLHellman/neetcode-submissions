class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        for char in t:
            if char in chars:
                chars[char] -= 1
            else:
                return False
        for val in chars.values():
            if val != 0:
                return False
        return True
