# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sort_steps = []
        for i in range(len(pairs)):
            k = i-1
            while k >= 0 and pairs[k+1].key < pairs[k].key:
                temp = pairs[k+1]
                pairs[k+1] = pairs[k]
                pairs[k] = temp
                k -= 1
            sort_steps.append(pairs.copy())
        return sort_steps
