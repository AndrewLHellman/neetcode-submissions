class SegmentTree:
    
    def __init__(self, nums: List[int], L: int = 0, R: Optional[int] = None):
        self.L = L
        if R == None:
            R = len(nums) - 1
        self.R = R
        self.left = None
        self.right = None
        if self.L == self.R:
            self.val = nums[self.L]
        else:
            M = (self.L + self.R) // 2
            self.left = SegmentTree(nums, self.L, M)
            self.right = SegmentTree(nums, M+1, self.R)
            self.val = self.left.val + self.right.val
    
    def update(self, index: int, val: int) -> None:
        if self.L == self.R:
            self.val = val
            return
        M = (self.L + self.R) // 2
        if index <= M:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        self.val = self.left.val + self.right.val
    
    def query(self, L: int, R: int) -> int:
        M = (self.L + self.R) // 2
        if self.L == L and self.R == R:
            return self.val
        elif L > M:
            return self.right.query(L, R)
        elif R <= M:
            return self.left.query(L, R)
        else:
            return self.left.query(L, M) + self.right.query(M+1, R)

