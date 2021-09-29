class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [x*x for x in nums]
        squares.sort()
        return squares
