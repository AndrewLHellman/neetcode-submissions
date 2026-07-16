class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strs:
            map[frozenset(Counter(string).items())].append(string)
        return list(map.values())