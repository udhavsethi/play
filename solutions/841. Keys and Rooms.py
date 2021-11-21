# wrong solution as denoted by example: [[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]
# because the graph can be disconnected
# correct solution - do DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        in_edges = [0]*n
        for roomidx, room in enumerate(rooms):
            for key in room:
                if key != roomidx:
                    in_edges[key] += 1
        print(in_edges)
        for i in range(1,n):
            if in_edges[i] == 0:
                return False
        return True
