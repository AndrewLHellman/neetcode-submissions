class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.refs = 0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            cur.refs += 1
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                cur.refs += 1
            cur.word = True
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        def dfs(row, col, visit, word, cur) -> int:
            if min(row, col) < 0 or \
                row >= ROWS or col >= COLS or \
                (row, col) in visit or cur == None:
                return 0 
            if cur.refs <= 0 or board[row][col] not in cur.children:
                return 0 
            cur = cur.children[board[row][col]]
            word = word + board[row][col]
            found = 0
            if cur.word:
                res.add(word)
                found += 1
            
            visit.add((row, col))

            found += dfs(row + 1, col, visit, word, cur)
            found += dfs(row - 1, col, visit, word, cur)
            found += dfs(row, col + 1, visit, word, cur)
            found += dfs(row, col - 1, visit, word, cur)

            visit.remove((row, col))
            cur.refs -= found
            return found


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, set(), "", root)


        return list(res)