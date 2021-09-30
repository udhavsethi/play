class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if not (m*n == r*c):
            return mat
​
        result = []
        i,j = 0,0
        for row in range(r):
            temp=[]
            for cols in range(c):
                temp.append(mat[i][j])
                if j == (n-1):
                    j = 0
                    i += 1
                else:
                    j += 1
            result.append(temp)
        return result
