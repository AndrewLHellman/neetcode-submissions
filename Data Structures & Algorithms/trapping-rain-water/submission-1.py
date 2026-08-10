class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = 0, 0
        vol = 0
        while l < r:
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)
            if height[l] < height[r]:
                l += 1
                vol += max(0, maxl - height[l])
            else:
                r -= 1
                vol += max(0, maxr - height[r])
        return vol