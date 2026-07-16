class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1
        for letter in t:
            seen[letter] = seen.get(letter, 0) - 1
        for value in seen.values():
            if value != 0:
                return False
        return True