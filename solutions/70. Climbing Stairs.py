class Solution:
    # review
    # DP
    def climbStairsDP(self, n, steps):
        if n in steps:
            return steps[n]
        steps[n] = self.climbStairsDP(n-1,steps) + self.climbStairsDP(n-2,steps)
        return steps[n]
​
    def climbStairs(self, n: int) -> int:
        steps = {1: 1, 2: 2}
        return self.climbStairsDP(n, steps)
​
