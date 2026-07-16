class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            if char in [')', ']', '}']:
                try:
                    first = stack.pop()
                except IndexError:
                    return False
                if (first == '(' and char != ')') or (first == '[' and char != ']') or (first == '{' and char != '}'):
                    return False
        if len(stack) > 0:
            return False
        return True