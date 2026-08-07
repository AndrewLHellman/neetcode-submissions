class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currSum = sum(arr[0:k-1])
        L = 0
        R = k-1
        while R < len(arr):
            currSum += arr[R]
            R += 1
            if currSum / k >= threshold:
                count += 1
            currSum -= arr[L]
            L += 1
        
        return count