class Solution:
    # need to mark visited nodes!
    def floodFillIn(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        for r in range(rows):
            if image[r][sc] == oldColor:
                image[r][sc] = newColor
                self.floodFillIn(image, r, sc, newColor, oldColor)
        for c in range(cols):
            if image[sr][c] == image[sr][sc]:
                image[sr][c] = newColor
                self.floodFillIn(image, sr, c, newColor, oldColor)
        return image
​
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.floodFillIn(image, sr, sc, newColor, image[sr][sc])
