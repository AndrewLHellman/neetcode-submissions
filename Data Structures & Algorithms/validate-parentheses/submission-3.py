class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            if char in bracket_map.keys():
                try:
                    first = stack.pop()
                except IndexError:
                    return False
                if bracket_map[char] != first:
                    return False
        if len(stack) > 0:
            return False
        return True