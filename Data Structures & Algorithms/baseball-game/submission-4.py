class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0
        for operation in operations:
            if operation == 'C':
                sum -= record.pop()
            elif operation == 'D':
                prev_score = record[-1]
                new_score = 2*prev_score
                record.append(new_score)
                sum += new_score
            elif operation == '+':
                new_score = record[-2] + record[-1]
                record.append(new_score)
                sum += new_score
            else:
                new_score = int(operation)
                record.append(new_score)
                sum += new_score
        return sum