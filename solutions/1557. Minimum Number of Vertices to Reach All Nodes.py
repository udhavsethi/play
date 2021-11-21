# works, but TLE
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # first use visited to check nodes with 0 incoming edges
        visited = [0]*n
        for [src, tgt] in edges:
            visited[tgt] += 1
        stack = []
        res = []
        # now use prev info from visited and update it to track the visited nodes
        for i in range(len(visited)):
            if visited[i] == 0:
                stack.append(i)
                res.append(i)
                visited[i] = 1
            else:
                visited[i] = 0
​
        while len(stack) != 0:
            el = stack.pop()
            visited[el] = 1
            for [src, tgt] in edges:
                if src == el:
                    stack.append(tgt)
        
        # check if anything is not visited
        for i in range(len(visited)):
            if visited[i] == 0:
                res.append(i)
        return res
