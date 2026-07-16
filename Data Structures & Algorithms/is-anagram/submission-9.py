class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for char in s:
            map[char] = map.get(char, 0) + 1
        for char in t:
            map[char] = map.get(char, 0) - 1
        for val in map.values():
            if val != 0:
                return False
        return True