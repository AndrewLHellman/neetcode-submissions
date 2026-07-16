class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            counter = frozenset(Counter(string).items())
            map[counter] = map.get(counter, []) + [string]
        return list(map.values())