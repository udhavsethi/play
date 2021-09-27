# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bin_search(1, n)
    
    def bin_search(self, left, right):
        if left > right:
            return left
        mid = (left+right) // 2
        if isBadVersion(mid):
            return self.bin_search(left, mid-1)
        else:
            return self.bin_search(mid+1, right)
