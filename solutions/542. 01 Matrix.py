# work in progress
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
​
        def dfs(row, col):
            if row<0 or row>=rows or col<0 or col>=cols:
                return None
            if mat[row][col] == 0:
                return 0
            if visited[row][col] == 1:
                return values[row][col]
            visited[row][col] = 1
            distances = [dfs(row-1, col),
                         dfs(row+1,col),
                         dfs(row,col-1),
                         dfs(row,col+1)]
            return 1 + min([x for x in distances if x is not None])
​
        visited = [[0 for i in range(cols)] for j in range(rows)]
        values = [[0 for i in range(cols)] for j in range(rows)]
        for r in range(rows):
            for c in range(cols):
                values[r][c] = dfs(r,c)
        visited = [[0 for i in range(cols)] for j in range(rows)]
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                values[r][c] = dfs(r,c)
        return mat
​
