# review
# just return the nodes with zero in-edges
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_edges = [0]*n
        res = []
        for [src, tgt] in edges:
            in_edges[tgt] += 1
        for i in range(len(in_edges)):
            if in_edges[i] == 0:
                res.append(i)
        return res
​
​
# # works, but TLE
# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
#         # first use visited to check nodes with 0 incoming edges
#         visited = [0]*n
#         for [src, tgt] in edges:
#             visited[tgt] += 1
#         stack = []
#         res = []
#         # now use prev info from visited and update it to track the visited nodes
#         for i in range(len(visited)):
#             if visited[i] == 0:
#                 stack.append(i)
#                 res.append(i)
#                 visited[i] = 1
