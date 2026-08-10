class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        total = numbers[L] + numbers[R]
        while total != target:
            if total > target:
                R -= 1
            else:
                L += 1
            total = numbers[L] + numbers[R]
        return [L + 1, R + 1]