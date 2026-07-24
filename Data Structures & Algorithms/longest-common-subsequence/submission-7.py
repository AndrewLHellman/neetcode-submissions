class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev_row = [0] * len(text2)

        for r in range(len(text1)-1, -1, -1):
            cur_row = [0] * len(text2)
            if text1[r] == text2[len(text2)-1]:
                cur_row[len(text2)-1] = 1
            else:
                cur_row[len(text2)-1] = prev_row[len(text2)-1]
            for c in range(len(text2)-2, -1, -1):
                if text1[r] == text2[c]:
                    cur_row[c] = prev_row[c+1] + 1
                else:
                    cur_row[c] = max(prev_row[c], cur_row[c+1])
            
            prev_row = cur_row
        
        return prev_row[0]