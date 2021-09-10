class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        # edges = edges.copy()
        print("checking edges {} with start {} and end {}".format(edges, start, end))
        for edge in edges:
            # print("checking edge {} with start {} and end {}".format(edge, start, end))
            if start in edge:
                # print("found match for start {} in edge {}".format(start,edge))
                if end in edge:
                    return True
​
                edges.remove(edge)
                # print("removed edge {}, remaining edges {}".format(edge,edges))
                edge.remove(start)
                print(edge)
                other = edge[0]
                # print("started from {}, didn't find {}, now checking {}".format(start, end, other))
​
                found = self.validPath(n, edges, other, end)
                if found:
                    return True
            # else:
                # print("didnt find match for start {} in {}".format(start, edge))
        # return False
