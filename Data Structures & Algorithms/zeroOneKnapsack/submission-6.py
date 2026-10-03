class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        last_row = [0] * (capacity+1)
        cur_row = [0] * (capacity+1)

        for i, w in enumerate(weight, 1):
            for col in range(1, capacity+1):
                if w > col:
                    cur_row[col] = last_row[col]
                else:
                    with_item = last_row[col-w] + profit[i-1]
                    cur_row[col] = max(with_item, last_row[col])
            last_row = cur_row
            cur_row = [0] * (capacity+1)
        return last_row[capacity]
