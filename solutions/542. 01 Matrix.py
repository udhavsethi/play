class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        res = [[float(inf) for i in range(cols)] for j in range(rows)]
        queue = []
​
        # add zeros to the queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    res[r][c] = 0
                    visited[r][c] = 1
                    
        # dequeue cell and enqueue adjacent cells - BFS
        while len(queue) != 0:
            cr, cc = queue.pop(0)
            visited[cr][cc] = 1
            distances = []
            # find neighbours of cur cell and add to the queue
            if cr > 0:
                distances.append(res[cr-1][cc])
                if visited[cr-1][cc] == 0:
                    queue.append((cr-1, cc))
            if cr < rows-1:
                distances.append(res[cr+1][cc])
                if visited[cr+1][cc] == 0:
                    queue.append((cr+1, cc))
            if cc > 0:
                distances.append(res[cr][cc-1])
                if visited[cr][cc-1] == 0:
                    queue.append((cr, cc-1))
            if cc < cols-1:
                distances.append(res[cr][cc+1])
                if visited[cr][cc+1] == 0:
                    queue.append((cr, cc+1))
            if res[cr][cc] == float(inf):
                res[cr][cc] = 1 + min(distances)
        return res
​
# works but time limit exceeded
# class Solution:
