# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def _merge(self, pairs: List[Pair], s: int, m: int, e: int) -> List[Pair]:
        sorted_pairs = []
        i, j = s, m
        while i < m and j < e:
            if pairs[i].key <= pairs[j].key:
                sorted_pairs.append(pairs[i])
                i += 1
            else:
                sorted_pairs.append(pairs[j])
                j += 1
        while i < m:
            sorted_pairs.append(pairs[i])
            i += 1
        while j < e:
            sorted_pairs.append(pairs[j])
            j += 1

        pairs[s:e] = sorted_pairs

        return sorted_pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._mergeSortHelper(pairs, 0, len(pairs))
    
    def _mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s <= 1:
            return pairs
        
        m = (s + e) // 2
        self._mergeSortHelper(pairs, s, m)
        self._mergeSortHelper(pairs, m, e)
        self._merge(pairs, s, m, e)

        return pairs
