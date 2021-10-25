# review
# recursion
​
# solution 2 - without visited array
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row<0 or row>=rows or col<0 or col>=cols:
                return 0
            if grid[row][col]==0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)
​
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(area, max_area)
        return max_area
​
# sol 1 - with visited array
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         max_area = 0
#         rows, cols = len(grid), len(grid[0])
#         visited = [[0 for i in range(cols)] for j in range(rows)]
        
#         def dfs(row, col):
#             if row<0 or row>=rows or col<0 or col>=cols:
#                 return 0
#             if (visited[row][col]==1) or (grid[row][col]==0):
#                 return 0
#             visited[row][col] = 1
#             return 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)
​
#         for row in range(rows):
#             for col in range(cols):
#                 if (grid[row][col] == 1) and (visited[row][col] == 0):
#                     area = dfs(row, col)
#                     max_area = max(area, max_area)
#         return max_area
​
