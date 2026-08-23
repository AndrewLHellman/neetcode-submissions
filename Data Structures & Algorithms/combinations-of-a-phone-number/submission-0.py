class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        num_to_digits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        n = len(digits)
        res = []

        def dfs(cur_str):
            i = len(cur_str)
            if i == n:
                res.append(cur_str)
                return
            
            for char in num_to_digits[digits[i]]:
                dfs(cur_str + char)

        dfs("")
        return res