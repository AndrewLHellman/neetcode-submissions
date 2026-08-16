class MyCalendar:
    
    def __init__(self, L: int = 0, R: int = 1_000_000_000):
        self.L = L
        self.R = R
        self.M = (self.L + self.R) // 2
        self.left = None
        self.right = None
        self.covered = False
        self.free = True
        
    def _isFree(self, startTime: int, endTime: int) -> bool:
        if self.covered:
            return False
        if self.free:
            return True
        if startTime > self.M:
            return not self.right or self.right._isFree(startTime, endTime)
        elif endTime <= self.M:
            return not self.left or self.left._isFree(startTime, endTime)
        else:
            return ((not self.left or self.left._isFree(startTime, self.M))
                    and (not self.right or self.right._isFree(self.M + 1, endTime)))

    def _reserve(self, startTime: int, endTime: int) -> None:
        if startTime <= self.L and endTime >= self.R:
            self.covered = True
            return
        self.free = False
        if not self.left:
            self.left = MyCalendar(self.L, self.M)
        if not self.right:
            self.right = MyCalendar(self.M + 1, self.R)
        if startTime > self.M:
            self.right._reserve(startTime, endTime)
        elif endTime <= self.M:
            self.left._reserve(startTime, endTime)
        else:
            self.left._reserve(startTime, self.M)
            self.right._reserve(self.M+1, endTime)
        if self.left.covered and self.right.covered:
            self.covered = True

    def book(self, startTime: int, endTime: int) -> bool:
        if not self._isFree(startTime, endTime-1):
            return False
        self._reserve(startTime, endTime-1)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)