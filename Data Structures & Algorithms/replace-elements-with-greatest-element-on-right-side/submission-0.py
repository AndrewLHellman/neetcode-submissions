class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        last_element = arr[0]
        arr[0] = -1
        for i in range(1, len(arr)):
            temp = arr[i]
            arr[i] = max(last_element, arr[i-1])
            last_element = temp

        return arr[::-1]