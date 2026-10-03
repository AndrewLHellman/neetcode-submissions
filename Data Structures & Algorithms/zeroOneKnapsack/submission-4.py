class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        tab = [[0] * (capacity+1) for _ in range(len(weight)+1)]
        n_rows, n_cols = len(tab), len(tab[0])
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                item_weight = weight[row-1]
                if item_weight > col:
                    tab[row][col] = tab[row-1][col]
                else:
                    with_item = tab[row-1][col-item_weight] + profit[row-1]
                    tab[row][col] = max(with_item, tab[row-1][col])
        return tab[n_rows-1][n_cols-1]
