# review
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[x for x in range(1,n+1)]]
        if k == 1:
            return [[x] for x in range(1,n+1)]
        res = self.combine(n-1, k-1)
        for lst in res:
            lst = lst.append(n)
        res.extend(self.combine(n-1, k))
        return res
