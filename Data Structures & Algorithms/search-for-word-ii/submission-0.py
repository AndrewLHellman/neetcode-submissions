class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        def dfs(row, col, visit, word, cur):
            if min(row, col) < 0 or \
                row >= ROWS or col >= COLS or \
                (row, col) in visit or cur == None:
                return
            if board[row][col] not in cur.children:
                return
            cur = cur.children[board[row][col]]
            word = word + board[row][col]
            if cur.word:
                res.add(word)
            
            visit.add((row, col))

            dfs(row + 1, col, visit, word, cur)
            dfs(row - 1, col, visit, word, cur)
            dfs(row, col + 1, visit, word, cur)
            dfs(row, col - 1, visit, word, cur)

            visit.remove((row, col))


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, set(), "", root)


        return list(res)