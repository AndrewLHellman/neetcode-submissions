class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, color, image[sr][sc])
        return image
        
    def dfs(self, image: List[List[int]], r: int, c: int, color: int, scolor: int, visited: set = set()) -> None:
        ROWS, COLS = len(image), len(image[0])
        if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            image[r][c] != scolor or
            (r, c) in visited):
            return

        image[r][c] = color
        visited.add((r, c))
        self.dfs(image, r + 1, c, color, scolor, visited)
        self.dfs(image, r - 1, c, color, scolor, visited)
        self.dfs(image, r, c + 1, color, scolor, visited)
        self.dfs(image, r, c - 1, color, scolor, visited)
        visited.remove((r, c))
