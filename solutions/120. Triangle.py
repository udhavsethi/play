# Recursion + DP
class Solution:
    def minFrom(self, triangle, row, col, mem):
        if (row,col) in mem:
            return mem[(row,col)]
        if row == len(triangle)-1:
            return triangle[row][col]
        mem[(row,col)] = triangle[row][col] + min(self.minFrom(triangle, row+1, col, mem), self.minFrom(triangle, row+1, col+1, mem))
        return mem[(row,col)]
​
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minFrom(triangle, 0, 0, {})
​
# # Simple recursion - TLE
# class Solution:
#     def minFrom(self, triangle, row, col):
#         if row == len(triangle)-1:
#             return triangle[row][col]
#         return triangle[row][col] + min(self.minFrom(triangle, row+1, col), self.minFrom(triangle, row+1, col+1))
​
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         return self.minFrom(triangle, 0, 0)
