# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        pivot = pairs[-1].key

        left = 0
        for i in range(len(pairs)):
            if pairs[i].key < pivot:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1
        temp = pairs[left]
        pairs[left] = pairs[-1]
        pairs[-1] = temp
        
        pairs[:left] = self.quickSort(pairs[:left])
        pairs[left+1:] = self.quickSort(pairs[left+1:])

        return pairs