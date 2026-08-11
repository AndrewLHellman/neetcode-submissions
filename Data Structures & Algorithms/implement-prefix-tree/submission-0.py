from typing import DefaultDict

class TrieNode:
    children: DefaultDict[str, Optional[TrieNode]]
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.word = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if curr.children[c] == None:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            curr = curr.children[c]
            if curr == None:
                return False
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            curr = curr.children[c]
            if curr == None:
                return False
        return True
        
