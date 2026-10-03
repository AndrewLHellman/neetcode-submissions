class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def worker(first_n: int, remaining: int, memo={}):
            if (first_n, remaining) in memo:
                return memo[(first_n, remaining)]
            if first_n == 0 or remaining == 0:
                return 0
            last_weight = weight[first_n-1]
            if weight[first_n-1] > remaining:
                memo[(first_n, remaining)] = worker(first_n-1, remaining)
            else:
                with_last = worker(first_n-1, remaining - last_weight) + profit[first_n-1]
                without_last = worker(first_n-1, remaining)
                memo[(first_n, remaining)] = max(with_last, without_last)
            return memo[(first_n, remaining)]
        return worker(len(profit), capacity)