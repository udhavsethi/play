class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = [lst[::-1] for lst in A]
        A = [[1-val for val in lst] for lst in A]
        return A
​
