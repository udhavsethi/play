# works but time limit exceeded
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
​
        def dfs1(row, col):
            if row<0 or row>=rows or col<0 or col>=cols:
                return float("inf")
            if mat[row][col] == 0:
                return 0
            return 1 + min(dfs1(row-1, col), dfs1(row,col-1))
        
        def dfs2(row, col):
            if row<0 or row>=rows or col<0 or col>=cols:
                return float("inf")
            if mat[row][col] == 0:
                return 0
            return min(mat[row][col], 1 + min(dfs2(row+1,col), dfs2(row,col+1)))
​
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = dfs1(r,c)
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                mat[r][c] = dfs2(r,c)
        return mat
​
