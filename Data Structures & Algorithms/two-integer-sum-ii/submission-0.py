class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, 1
        while numbers[index1] + numbers[index2] != target:
            index2 += 1
            if index2 >= len(numbers):
                index1 += 1
                index2 = index1 + 1
        return [index1 + 1, index2 + 1]