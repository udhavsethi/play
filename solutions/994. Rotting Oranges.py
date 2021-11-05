class Solution:
​
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = []
        count = 0
        
        # add 2s to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    grid[r][c] = 1
                    queue.append((r,c,0))
        
        # bfs using each 2
        while len(queue) != 0:
            (r,c, level) = queue.pop(0)
            if grid[r][c] == 2:
                continue
            grid[r][c] = 2
            count = max(count, level)
            if r-1 >= 0 and grid[r-1][c] == 1:
                queue.append((r-1,c, level+1))
            if r+1 < rows and grid[r+1][c] == 1:
                queue.append((r+1,c, level+1))
            if c-1 >= 0 and grid[r][c-1] == 1:
                queue.append((r,c-1, level+1))
            if c+1 < cols and grid[r][c+1] == 1:
                queue.append((r,c+1, level+1))
​
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = -1
        return count
            
