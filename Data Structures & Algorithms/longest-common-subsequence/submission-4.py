class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        tab = [[0]*len(text2) for _ in range(len(text1) + 1)]

        for r in range(len(text1)-1, -1, -1):
            if text1[r] == text2[len(text2)-1]:
                tab[r][len(text2)-1] = 1
            else:
                tab[r][len(text2)-1] = tab[r+1][len(text2)-1]
            for c in range(len(text2)-2, -1, -1):
                if text1[r] == text2[c]:
                    tab[r][c] = tab[r+1][c+1] + 1
                else:
                    tab[r][c] = max(tab[r+1][c], tab[r][c+1])
        
        return tab[0][0]