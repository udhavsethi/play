class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0]*n
        for [truster, trustee] in trust:
            score[trustee-1] += 1
            score[truster-1] -= 1
        for idx in range(len(score)):
            if score[idx] == n-1:
                return idx+1
        return -1
