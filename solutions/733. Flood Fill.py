# review
# check recursive method in solutions
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = []
        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
​
        image[sr][sc] = newColor
        stack.append((sr,sc))
​
        while len(stack) != 0:
            (cr,cc) = stack.pop()
            adjacent_pixels = [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]
            for r,c in adjacent_pixels:
                if r>=0 and r<rows and c>=0 and c<cols and (image[r][c] == oldColor):
                    image[r][c] = newColor
                    stack.append((r,c))
        return image
