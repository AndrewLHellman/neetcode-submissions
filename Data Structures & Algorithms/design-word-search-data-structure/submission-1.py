class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(word: str, trie: TrieNode) -> bool:
            if word == "":
                return trie.word
            elif word[0] == ".":
                for c in trie.children:
                    res = dfs(word[1:], trie.children[c])
                    if res == True:
                        return True
                return False
            elif word[0] not in trie.children:
                    return False
            else:
                return dfs(word[1:], trie.children[word[0]])
        return dfs(word, self.root)
            
