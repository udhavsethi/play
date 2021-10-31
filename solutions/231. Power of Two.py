class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 2 == 0:
            return self.isPowerOfTwo(n/2)
        return False
    
        # review
        # bit manipulation
        # return n > 0 && ((n & (n-1)) == 0);
