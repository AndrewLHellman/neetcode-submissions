class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 0
        l = 0

        for r in range(len(arr)):
            if r - l + 1 > 2:
                if arr[r - 2] > arr[r - 1]:
                    if arr[r] < arr[r-1]:
                        l = r - 1
                    elif arr[r] == arr[r-1]:
                        l = r
                elif arr[r - 2] < arr[r - 1]:
                    if arr[r] > arr[r-1]:
                        l = r - 1
                    elif arr[r] == arr[r-1]:
                        l = r
            elif r - l + 1 == 2:
                if arr[r] == arr[r-1]:
                    l = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen
                    