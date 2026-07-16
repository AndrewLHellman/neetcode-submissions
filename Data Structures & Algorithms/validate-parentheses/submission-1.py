class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openp = ['(', '{', '[']
        for char in s:
            if (char in openp):
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                l = stack.pop()
                if (l == '(' and char != ')'):
                    return False
                if (l == '[' and char != ']'):
                    return False
                if (l == '{' and char != '}'):
                    return False
        if (len(stack) > 0):
            return False
        return True