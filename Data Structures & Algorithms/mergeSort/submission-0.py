# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs_a: List[Pair], pairs_b: List[Pair]) -> List[Pair]:
        pairs = []
        a, b = 0, 0
        while a < len(pairs_a) and b < len(pairs_b):
            if pairs_a[a].key <= pairs_b[b].key:
                pairs.append(pairs_a[a])
                a += 1
            else:
                pairs.append(pairs_b[b])
                b += 1
        while a < len(pairs_a):
            pairs.append(pairs_a[a])
            a += 1
        while b < len(pairs_b):
            pairs.append(pairs_b[b])
            b += 1
        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        pairs_a = self.mergeSort(pairs[:m])
        pairs_b = self.mergeSort(pairs[m:])

        return self.merge(pairs_a, pairs_b)