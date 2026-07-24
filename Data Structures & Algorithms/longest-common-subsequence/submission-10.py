class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev_row = [0] * (len(text2) + 1)

        for r in range(len(text1)-1, -1, -1):
            cur_c = 0
            cur_c1 = 0
            for c in range(len(text2)-1, -1, -1):
                if text1[r] == text2[c]:
                    cur_c = prev_row[c+1] + 1
                else:
                    cur_c = max(prev_row[c], cur_c1)
                prev_row[c+1] = cur_c1
                cur_c1 = cur_c
            prev_row[0] = cur_c1
        
        return prev_row[0]