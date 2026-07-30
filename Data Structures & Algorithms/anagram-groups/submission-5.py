class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strs:
            key = frozenset(Counter(string).items())
            map[key].append(string)
        return list(map.values())