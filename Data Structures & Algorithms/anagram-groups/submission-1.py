class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        anagrams = {}
        anagram_list = []
        for string in strs:
            counter = tuple(sorted(collections.Counter(string).items()))
            if counter in anagrams:
                anagram_list[anagrams[counter]].append(string)
            else:
                anagrams[counter] = index
                anagram_list.append([string])
                index += 1
        return anagram_list