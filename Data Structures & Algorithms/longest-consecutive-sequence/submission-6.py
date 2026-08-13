class UnionFind:
    def __init__(self, n: int):
        self.pars = list(range(n))
        self.rank = [1] * n
    
    def find(self, x: int) -> int:
        p = self.pars[x]
        while p != self.pars[p]:
            self.pars[p] = self.pars[self.pars[p]]
            p = self.pars[p]
        return p
    
    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.pars[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.pars[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))
        numToIndex = {}
        for i, num in enumerate(nums):
            numToIndex[num] = i
        
        for num in nums:
            if num - 1 in numToIndex:
                uf.union(numToIndex[num], numToIndex[num-1])
        
        return max([0] + uf.rank)