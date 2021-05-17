class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while not (x == 0 and y == 0):
            if (x % 2) != (y % 2):
                distance += 1
            x = int(x/2)
            y = int(y/2)
        return distance
