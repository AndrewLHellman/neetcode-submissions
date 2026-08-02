class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []
        for char in s:
            if char in bracket_map.keys():
                stack.append(bracket_map[char])
            elif not stack or stack.pop() != char:
                return False
        
        return len(stack) == 0