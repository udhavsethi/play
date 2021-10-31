class Solution:
    def hammingWeight(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return int(n%2) + self.hammingWeight(n/2)
       
        # review
        # bitwise shift
        count=0
        while n:
            count += (n & 1)
            n = n >> 1
        return count
