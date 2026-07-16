class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, color, image[sr][sc])
        return image
        
    def dfs(self, image: List[List[int]], r: int, c: int, color: int, scolor: int) -> None:
        ROWS, COLS = len(image), len(image[0])
        if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            image[r][c] != scolor or
            scolor == color):
            return

        image[r][c] = color
        self.dfs(image, r + 1, c, color, scolor)
        self.dfs(image, r - 1, c, color, scolor)
        self.dfs(image, r, c + 1, color, scolor)
        self.dfs(image, r, c - 1, color, scolor)
