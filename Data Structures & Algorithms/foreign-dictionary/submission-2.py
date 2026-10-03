class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        for char in set("".join(words)):
            adjList[char] = []
        for word1, word2 in zip(words[:-1], words[1:]):
            prefix = True
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    adjList[char2].append(char1)
                    prefix = False
                    break
            if prefix and len(word1) > len(word2):
                return ""
        
        visit = set()
        path = set()
        topOrder = []
        def dfs(n):
            if n in path:
                return False
            if n in visit:
                return True
            
            visit.add(n)
            path.add(n)
            for m in adjList[n]:
                if not dfs(m):
                    return False
            path.remove(n)
            topOrder.append(n)
            return True
        
        for char in adjList:
            if not dfs(char):
                return ""

        return "".join(topOrder)
