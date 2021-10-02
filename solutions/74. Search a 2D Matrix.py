class Solution:
    # sol 2 - more efficient
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # value is outside matrix range
        if matrix[0][0] > target or matrix[rows-1][cols-1] < target:
            return False
        # value is in matrix range
        i,j = 0,0
        while i < rows and j < cols:
            if matrix[i][j] == target:
                return True
            if (i == rows-1) or (matrix[i+1][j] > target):
                if j == cols-1 or matrix[i][j+1] > target:
                    return False
                else:
                    j += 1
            elif (matrix[i+1][j] <= target):
                i = i+1
        return False
​
    # ## sol 1
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     rows, cols = len(matrix), len(matrix[0])
    #     i,j = 0,0
    #     while i<rows:
    #         if matrix[i][j] == target:
    #             return True
    #         elif j == cols-1:
    #             j = 0
    #             i +=1
    #         else:
    #             j += 1
    #     return False
​
