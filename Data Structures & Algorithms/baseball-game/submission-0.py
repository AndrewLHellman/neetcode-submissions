class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == 'C':
                record.pop()
            elif operation == 'D':
                prev_score = record[-1]
                new_score = 2*prev_score
                record.append(new_score)
            elif operation == '+':
                record.append(record[-2] + record[-1])
            else:
                record.append(int(operation))
        return sum(record)