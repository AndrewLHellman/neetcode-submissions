class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.worker(0, [], combs, n, k)

        return combs

    def worker(self, i: int, cur_comb: List[int], combs:List[List[int]], n: int, k: int):
        if len(cur_comb) == k:
            combs.append(cur_comb.copy())
            return
        
        for j in range(i, n + 1 - (k - len(cur_comb))):
            cur_comb.append(j + 1)
            self.worker(j+1, cur_comb, combs, n, k)
            cur_comb.pop()