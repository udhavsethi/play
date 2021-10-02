class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i,j = 0,0
        while i<rows:
            if matrix[i][j] == target:
                return True
            elif j == cols-1:
                j = 0
                i +=1
            else:
                j += 1
        return False
​
