class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        
        def dfs(row, col, count):
            print("Starting count for row,col:{},{} = {}".format(row, col, count))
            if row<0 or row>=rows or col<0 or col>=cols:
                print("but returned 0 because out of bounds")
                return 0
            if (visited[row][col]==1) or (grid[row][col]==0):
                print("but returned 0 because visited / is 0")
                return 0
            print("setting to visited and adding 1: ", row, col)
            visited[row][col] = 1
            count+=1
            count += dfs(row-1, col, count)
            count += dfs(row+1, col, count)
            count += dfs(row, col-1, count)
            count += dfs(row, col+1, count)
            print("Total count for row,col:{},{} = {}".format(row, col, count))
            return count
​
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == 1) and (visited[row][col] == 0):
                    area = dfs(row, col, 0)
                    max_area = max(area, max_area)
        print(visited)
        return max_area
​
