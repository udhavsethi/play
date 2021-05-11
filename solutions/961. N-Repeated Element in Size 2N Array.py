class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = {}
        for item in A:
            if item in seen:
                return item
            seen[item] = 1
